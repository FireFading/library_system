from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    year = models.IntegerField(default=2022)
    number = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = "books"
        
    def __str__(self):
        return f"{self.title} by {self.author}, {self.year}"
    
    
