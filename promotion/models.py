from django.db import models

# Create your models here.
class Promotion(models.Model):
    promotion = models.CharField(max_length=40)  # Вид поощерения
    personal_id = models.IntegerField()

