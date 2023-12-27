from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date
#import user model 

# Create your models here.


# request_type=(
#     ("--PLEASE CHOOSE A SERVICE--","--Please choose a service--"),
#     ("laptop","LAPTOP"),
#     ("tv","TV"),
#     ("smart phone","SMART PHONE"),
#     ("wifi","WIFI"),
#     ("ac","AC"),
# )

class customer_request(models.Model):
    customer_name=models.CharField(max_length=10)
    email_ID=models.EmailField()
    phone_number=models.CharField(max_length=10)
    address=models.TextField()
    city=models.CharField(max_length=10)
    state=models.CharField(max_length=10)
    pin_code=models.PositiveIntegerField()
    request_Type=models.CharField(max_length=50, choices=(('english','arduino'),('history','motor'),('electro','battery')), default=" ")
    description=models.TextField()
    date=models.DateField()
    connect=models.ForeignKey(User,default=None, on_delete=models.CASCADE, null=True)
    cdate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name
    
    
    
# class customer_message(models.Model):
#     name=
#     email_ID=
#     phone_number=
#     subject=
#     message=
#     author=models.ForeignKey(User,default=None, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return self.name



class subscriber(models.Model):
    email_ID =models.EmailField()

    def __str__(self):
        return self.email_ID
    
    
    

class review(models.Model):
    review_message=models.TextField()
    boss=models.ForeignKey(User,default=None, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.boss.username