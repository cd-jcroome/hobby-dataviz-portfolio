import importlib
import os

import pandas as pd
from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.utils.text import slugify

DTYPE_TO_MODEL_FIELD = {
    "object": "models.TextField()",
    "int64": "models.IntegerField()",
    "float64": "models.FloatField(default='')",
    "bool": "models.BooleanField()",
    "datetime64": "models.FloatField(default='')",
    "timedelta[ns]": "models.FloatField(default='')",
    "category": "models.TextField()"
}

MODEL_TEMPLATE = """

class {class_name}(models.Model):
    {model_fields}
    class Meta:
        verbose_name_plural: '{class_name}'
"""

def file_to_model_name(filename):
    base_name, _ = os.path.splitext(filename)
    return slugify(base_name).replace("_"," ").title().replace(" ", "")

def model_exists(module_str, model_name):
    models_module = importlib.import_module(module_str)
    return hasattr(models_module, model_name)

def reload_module(module_str):
    models_module = importlib.import_module(module_str)
    importlib.reload(models_module)

def write_model(model_class_str):
    with open("vizzes/models.py", "a+") as fd:
        fd.write(model_class_str)
    fd.close()

def col_to_field_name(col_label):
    return slugify(col_label).replace("-","_")

def df_to_model_str(class_name, df):
    model_fields = []
    for i, (col_label, col_type) in enumerate(zip(df.columns, df.dtypes), 1):
        field_name = col_to_field_name(col_label)
        field_type = DTYPE_TO_MODEL_FIELD.get(str(col_type))
        if not field_type:
            CommandError('Can\'t translate datatype "{}" at column {}'.format(col_type, i))
        model_fields.append("{} = {}".format(field_name, field_type))
    rendered_model_fields = "\n    ".join(model_fields)
    rendered_class = MODEL_TEMPLATE.format(class_name=class_name, model_fields=rendered_model_fields)
    return rendered_class

def load_model_data(model_class, df):
    model_instances = []
    for index,row in df.iterrows():
        instance = model_class()
        for col_name in df.columns:
            field_name = col_to_field_name(col_name)
            setattr(instance, field_name, row[col_name])
        model_instances.append(instance)
    model_class.objects.bulk_create(model_instances)

def register_model(model_desc):
    with open('vizzes/admin.py', 'r') as ad_r:
        index = ad_r.readlines()
    ad_r.close()
    with open('vizzes/admin.py', 'w') as ad_a:
        for line in index:
            if line.startswith("from .models import "):
                line = line.strip() + (", %s\n" % model_desc)
            ad_a.write(line)
        ad_a.close()
    with open('vizzes/admin.py', 'a+') as ad_a2:
        ad_a2.write("\nadmin.site.register(%s)" % model_desc)
        ad_a2.close()
    with open("vizzes/models.py","r") as vm1:
        lines = vm1.readlines()
    vm1.close()
    with open("vizzes/models.py", "w") as vm2:
        for i, line in enumerate(lines):
            if i == 10:
                vm2.write("\n(\'%s\',\'%s\')," % (model_desc, model_desc))
            vm2.write(line)
    vm2.close()

class Command(BaseCommand):
    help = 'Adds New Data from the specified url to the vizzes Models. enter the url, followed by the data description'

    def add_arguments(self, parser):
        parser.add_argument('data_url', type=str)
        parser.add_argument('data_desc')
        parser.add_argument('data_type')

    def handle(self, *args, **options):
        data_desc = options['data_desc']
        data_url = options['data_url']
        data_type = options['data_type']
        if data_type.lower() == 'csv':
            data = pd.read_csv(data_url)
        elif data_type.lower() == 'xls':
            data = pd.read_excel(data_url)
        elif data_type.lower() == 'json':
            data = pd.read_json(data_url)
        elif data_type.lower() == 'tsv':
            data = pd.read_csv(data_url, delimiter='\t')
        else:
            print("We can\'t process %s data yet. Sorry!"% data_type)
        if model_exists('vizzes.models', data_desc):
            raise CommandError("{} Model Already Exists".format(data_desc))
        model_str = df_to_model_str(data_desc, data)
        
        register_model(data_desc)
        
        write_model(model_str)
        reload_module('vizzes.models')
        call_command("makemigrations", "vizzes")
        call_command("migrate", "vizzes")

        model_class = apps.get_model('vizzes', data_desc)
        load_model_data(model_class, data)       

        self.stdout.write(self.style.SUCCESS('Successfully Added Model %s from %s' % (data_desc, data_url)))
