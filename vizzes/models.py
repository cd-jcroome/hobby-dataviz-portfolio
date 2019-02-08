from django.db import models

# Create your models here.

class Dataviz(models.Model):
    """Model definition for Dataviz."""

    viz_name = models.CharField(max_length=500,unique=True)
    viz_verbose_name = models.CharField(max_length=500, default='---')
    date_added = models.DateTimeField('Date Added')
    viz_description = models.TextField(default='A brief Description of the Viz')
    viz_source = models.URLField(default='Data Source')
    viz_file = models.URLField(max_length=500, default='https://cdn.jsdelivr.net/gh/jasparr77/d3/[Folder]/[JS File]')
    viz_thumb = models.URLField(default='thumbnail for Viz Card')
    author = models.CharField(max_length=25, default='')
    class Meta:
        """Meta definition for Dataviz."""

        verbose_name =  'Dataviz'
        verbose_name_plural =  'Datavizzes'

    def __str__(self):
        """Unicode representation of Dataviz."""
        return self.viz_name
