from django.db import models

# Create your models here.

class Dataviz(models.Model):
    """Model definition for Dataviz."""
    D3_SCROLL = 'D3L'
    D3_STATIC = 'D3T'
    WORDS = 'WRD'
    TABLEAU = 'TBX'
    IMAGE = 'IMG'
    VIZ_TYPE_CHOICES = (
        (D3_SCROLL,'D3 w/ Scrollytelling'),
        (D3_STATIC,'Static D3'),
        (TABLEAU,'Embedded Tableau Workbook'),
        (IMAGE,'Image'),
        (WORDS,'Just Words')
    )
    viz_name = models.CharField(max_length=500,unique=True)
    viz_type  = models.CharField(max_length=3,choices=VIZ_TYPE_CHOICES,default=D3_STATIC)
    viz_verbose_name = models.CharField(max_length=500, default='---')
    date_added = models.DateTimeField('Date Added')
    viz_description = models.TextField(default='A brief Description of the Viz')
    viz_source = models.URLField(default='Data Source')
    viz_file = models.TextField(max_length=1000, default='Paste CDN URL or Tableau Workbook and sheet name (e.g., "workbook/sheetname") here')
    viz_thumb = models.URLField(default='https://cdn.jsdelivr.net/gh/jasparr77/d3/[Folder]/[PNG File]')
    author = models.CharField(max_length=25, default='')
    class Meta:
        """Meta definition for Dataviz."""

        verbose_name =  'Dataviz'
        verbose_name_plural =  'Datavizzes'

    def __str__(self):
        """Unicode representation of Dataviz."""
        return self.viz_name
