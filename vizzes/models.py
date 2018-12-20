from django.db import models

# Create your models here.

class Dataviz(models.Model):
    """Model definition for Dataviz."""

    viz_name = models.CharField(max_length=100,unique=True)
    viz_verbose_name = models.CharField(max_length=100, default='---')
    date_added = models.DateTimeField('Date Added')
    viz_description = models.TextField(default='A brief Description of the Viz')
    viz_source = models.URLField(default='Viz Source')
    viz_file = models.FileField(upload_to='vizzes/static/vizzes/js')
    viz_thumb = models.ImageField(upload_to='vizzes/static/vizzes/images')
    author = models.CharField(max_length=25, default='')
    class Meta:
        """Meta definition for Dataviz."""

        verbose_name =  'Dataviz'
        verbose_name_plural =  'Datavizzes'

    def __str__(self):
        """Unicode representation of Dataviz."""
        return self.viz_name
