from django.db import models

# Create your models here.

class Dataviz(models.Model):
    """Model definition for Dataviz."""

    viz_id = models.CharField('ID', max_length=4, unique=True)
    model = models.CharField(max_length=200,
        choices=[
        ('mlb_beer','mlb_beer'),
        ('women_congress','women_congress')
        ])
    viz_name = models.CharField(max_length=100)
    viz_verbose_name = models.CharField(max_length=100, default='---')
    date_added = models.DateTimeField('Date Added')
    viz_description = models.TextField(default='A brief Description of the Viz')
    viz_source = models.URLField(default='Viz Source')
    viz_thumb = models.ImageField(upload_to='images/')
    author = models.CharField(max_length=25, default='')

    class Meta:
        """Meta definition for Dataviz."""

        verbose_name =  'Dataviz'
        verbose_name_plural =  'Datavizzes'

    def __str__(self):
        """Unicode representation of Dataviz."""
        return self.viz_name

class women_congress(models.Model):
    congress = models.TextField()
    years = models.TextField()
    women_total = models.IntegerField()
    republican = models.IntegerField()
    of_women_rep = models.FloatField(default='')
    of_party_rep = models.FloatField(default='')
    democratic = models.IntegerField()
    of_women_dem = models.FloatField(default='')
    of_party_dem = models.FloatField(default='')
    
    class Meta:
        verbose_name_plural: 'women_congress'

    def __str__(self):
        return self.years + ' | ' + self.congress + ' congress'


class mlb_beer(models.Model):
    year = models.IntegerField()
    team = models.TextField()
    nickname = models.TextField()
    city = models.TextField()
    price = models.FloatField(default='')
    size = models.FloatField(default='')
    price_per_ounce = models.FloatField(default='')
    class Meta:
        verbose_name_plural: 'mlb_beer'
