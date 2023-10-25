from django.db import models


class Merchant(models.Model):
    name=models.CharField(max_length=200)
    category=models.CharField(max_length=255, null=True)
    country=models.CharField(max_length=255, null=True)
    nif=models.IntegerField()
    
    class Status(models.TextChoices):
        public='pub'
        private='priv'
        mixte='mix'
    
    type=models.CharField(choices=Status.choices, max_length=20, null=True, blank=True)
        
    phone=models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return f"{self.name}"
    
class Product(models.Model):
    title=models.CharField(max_length=200)
    price=models.IntegerField(null=True, blank=True)
    description=models.TextField(max_length=500, null=True, blank=True)
    merchant = models.ForeignKey(Merchant, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
       return f"{self.title}"
    