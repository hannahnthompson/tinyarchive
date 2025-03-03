from django.db import models
from archive.models import Document

class Exhibit(models.Model):
    title = models.CharField(max_length=200)
    short_description=models.CharField(max_length=1000)
    items_in_exhibit=models.ManyToManyField(Document)
    exhibit_text = models.TextField(blank=True, null=False)
    def __str__(self):
        return self.title



