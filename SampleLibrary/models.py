from django.db import models

# Create your models here.


class Sample(models.Model):
    name = models.CharField(max_length=200);
    location = models.CharField(max_length=200);

    #Need this so admin tools display it correctly
    def __unicode__(self):
        return self.name;


