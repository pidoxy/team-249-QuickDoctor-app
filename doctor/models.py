from django.db import models  

class Doctor(models.Model):    
    name = models.CharField(max_length=100)
    field = models.CharField(max_length=100)  
    email = models.EmailField()  
    contact = models.CharField(max_length=20 )  
    address = models.CharField(max_length=100)
    area = models.CharField(max_length=100, default= "Lagos")
    class Meta:  
        db_table = "doctor"  

    
    def __str__(self):
        return self.name

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
"""

class Patient(models.Model):    
    name = models.CharField(max_length=100) 
    contact = models.IntegerField(max_length=15)  
    address = models.TextField(max_length=100)
    doctors = models.ManyToManyField(Doctor)
    class Meta:  
        db_table = "doctor"  
"""
