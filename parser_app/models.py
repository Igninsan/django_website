from django.db import models

class TsModel(models.Model):
    title = models.CharField(max_length=100)
    info = models.CharField(max_length=500)

    def str(self):
        return self.title

class RezkaModel(models.Model):
    title = models.CharField(max_length=500)

    def str(self):
        return self.title