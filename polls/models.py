from django.db import models


class Dados(models.Model):
    local = models.CharField(max_length=40)
    data = models.DateTimeField()
    temperatura = models.IntegerField()
    umidade = models.IntegerField()
    def __str__(self):
        return self.local
