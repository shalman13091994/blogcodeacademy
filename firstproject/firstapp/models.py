from django.db import models
from django.urls import reverse
from datetime import datetime,date

class student(models.Model):
    name=models.CharField(max_length=100)
    standard=models.CharField(max_length=100)
    address=models.TextField(max_length=1600)
    #this is for to set the blog upddate date 
    update_date=models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.name + " | "+ self.standard


    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
        # return reverse('home')
    


    

