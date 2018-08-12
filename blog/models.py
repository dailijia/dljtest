from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    create_date = models.DateField(auto_now = True)
    modify_date = models.DateField(auto_now = True)
    context = models.TextField()
    is_show = models.BooleanField()

    class Meta:
        db_table = "ariticle"

    def __str__(self):
        return self.title
