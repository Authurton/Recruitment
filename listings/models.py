from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Listing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    listing_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photos/%Y/%m/&d')

    def __str__(self):
        return self.name
    
class Company(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    company_logo = models.ImageField(upload_to='photos/%Y/%m/&d', null=True, blank=True)

    def __str__(self):
        return self.name

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  
    location = models.CharField(max_length=250, null=True, blank=True)
    job_name = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)  
    years_of_exp = models.IntegerField()  
    listed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_name
