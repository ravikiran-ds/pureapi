from django.db import models
from django.core.serializers import serialize
import json

# Create your models here.
class StuQuerySet(models.QuerySet):
    def serialize(self):
        list_values=list(self.values("name","score","type"))
        return json.dumps(list_values)

class StuDataManager(models.Manager):
    def get_queryset(self):
        return StuQuerySet(self.model,using=self._db)

class StuData(models.Model):
    name=models.CharField(max_length=256,blank=True)
    score=models.IntegerField()
    type=models.CharField(max_length=100,blank=False)

    objects=StuDataManager()

    def serialize(self):
        data={
        #"id":self.id,
        "name":self.name,
        "score":self.score,
        "type":self.type}

        return json.dumps(data)

    def __str__(self):
        return self.name
