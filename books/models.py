from django.db import models


class Book(models.Model):    
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=150, unique=True)
    year = models.IntegerField(default=2022)
    number = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    about_author = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "books"
        
    def __str__(self):
        return f"{self.title} by {self.author}, {self.year}"
    
    def get_absolute_url(self):
        return f"/book/{self.title}"
    
