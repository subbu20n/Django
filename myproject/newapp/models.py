from django.db import models
import uuid 
# Create your models here.

class OrderDetails(models.Model): 
    usermail=models.CharField(max_length=150,unique=True) 
    orderid=models.CharField(max_length=100,unique=True) 
    amount=models.DecimalField(max_digits=10,decimal_places=2) 
    mode=models.CharField(max_length=80) 
    dataandtime=models.DateTimeField(auto_now_add=True) 
    currency=models.CharField(default="INR",max_length=50)
    transaction_id=models.UUIDField(default=uuid.uuid4,editable=False,unique=True) 


#uuid1 --> generates a random number based on time and mac  
 
#------------(23-12-2025)----CREATING,INSERTING & get all recording into table in db------------------

#create an api to book a movie ticket with fields --> movie name, showtime, screen name,date and time, transactionid 

class movieBooking(models.Model): 
    moviename=models.CharField(max_length=150)
    showtime=models.CharField(max_length=100)
    screenname=models.CharField(max_length=100)
    dateandtime=models.DateTimeField(auto_now_add=True) 
    transaction_id=models.UUIDField(default=uuid.uuid4,editable=False,unique=True)   