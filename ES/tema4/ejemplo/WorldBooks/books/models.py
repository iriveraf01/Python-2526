from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'books'