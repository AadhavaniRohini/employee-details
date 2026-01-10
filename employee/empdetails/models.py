from django.db import models

# Create your models here.
class department(models.Model): 
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class employees(models.Model):
        full_name = models.CharField(max_length=30)
        email = models.EmailField(unique=True)
        age = models.IntegerField()
        department = models.ForeignKey(department, on_delete=models.CASCADE)

        def __str__(self):
            return self.full_name