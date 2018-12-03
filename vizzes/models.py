from django.db import models

# Create your models here.

class Dataviz(models.Model):
    """Model definition for Dataviz."""

    viz_id = models.CharField('ID', max_length=8, unique=True)
    viz_name = models.CharField(max_length=100)
    viz_verbose_name = models.CharField(max_length=100, default='---')
    date_added = models.DateTimeField('Date Added')
    viz_description = models.TextField(default='A brief Description of the Viz')
    viz_source = models.URLField(default='Viz Source')
    viz_thumb = models.ImageField(upload_to='images/')

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
