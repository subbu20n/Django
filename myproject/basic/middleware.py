#-------------------------MIDDLEWARE-------------------

#middleware is responsible for accepting requests and providing response in b/w views and user
# once we make a request immediately middleware will trigger by default 
# we will implement middleware using 'class based'
# while implementeing middleware using class, need to use two different methods which are mandatory  

# 1.__init__() --> whenever we start a server, this method will trigger by default 
# 2. __call__() --> whenever we make a api request/call then this method will trigger by default  

# this will be the responsible for taking user request and getting response from the view as per the request 

# 1.global middleware ---> triggers for every views 
# 2.specific middlewares ---> triggers for a specific view 

# we need to implement these middlewares inside a file by file by naming middlewares.py within the app 

# need to include them in middle wares[] within the settings.py file  

# class middleware1: 
#     def __init__(self,get_response):   # it starts when server start s it triggers  
#         print("middleware1 is inititing") 
#         self.get_response=get_response 

#     def __call__(self,request): # when you make api request 
#         print("middleware1 is accepting requests") 

#         response=self.get_response(request) 
#         return response 
import json 
from django.http import HttpResponse,JsonResponse
import re
from basic.models import User
from django.contrib.auth.hashers import make_password,check_password
    
# class middleware1:  
#     def __init__(self,get_response): 
#         print("middleware is initiating")   
#         self.get_response=get_response 

#     def __call__(self,request): 
#         if request.path=="/home/": 
#             print("Middleware1 is accepting requests only for home")
#         response=self.get_response(request) 
#         return response 
                
# class middleware2: 
#     def __init__(self,get_response): 
#         print("middleware is initiating")   
#         self.get_response=get_response 

#     def __call__(self,request): 
#         if request.path=="/about/": 
#             print("Middleware2 is accepting requests only for about")
#         response=self.get_response(request) 
#         return response 

# -----(07-01-2026)------------

# middlewares we can use for many purposes 
# 1. validation 
# 2. data encryption 
# 3. data formatting and cleaning 

# job application 
# q1.ssc 
# q2. medical fit 
# q3. age 21 

class sscMiddleware:
    def __init__(self,get_response):        
        self.get_response=get_response
    def __call__(self,request):  
        if request.path=="/job1/" and request.method=="POST":
            incoming_data=json.loads(request.body) 
            ssc_status=incoming_data.get("ssc_status")     
            if ssc_status:
                response=self.get_response(request)
                return response
        return JsonResponse({"status":"failure","msg":"u should qualify ssc to apply for this job"})
  

class medicallyFitMiddleware:
    def __init__(self,get_response):        
        self.get_response=get_response
    def __call__(self,request):  
        if request.path=="/job1/" and request.method=="POST":
            incoming_data=json.loads(request.body) 
            medical_status=incoming_data.get("medically_fit")     
            if medical_status:
                response=self.get_response(request)
                return response
        return JsonResponse({"status":"failure","msg":"u should medically fit  to apply for this job"}) 
    
class ageValidationMiddleware:
    def __init__(self,get_response):        
        self.get_response=get_response
    def __call__(self,request):  
        if request.path=="/job1/" and request.method=="POST":
            incoming_data=json.loads(request.body) 
            age=incoming_data.get("age")     
            if age>21:
                response=self.get_response(request)
                return response
        return JsonResponse({"status":"failure","msg":"u should have atleast 21 years to apply for this job"})
    

class authMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        self.username_pattern = re.compile(r'^[a-zA-Z0-9_]{5,15}$')
        self.password_pattern = re.compile(r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d@#]{8,}$')
        self.email_pattern = re.compile(r'^[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]{2,}$')
    def __call__(self,request):
        if request.path in ["/signup/", "/login/"] and request.method == "POST":
             try:
                data = json.loads(request.body)
             except json.JSONDecodeError:
                return JsonResponse({"error": "Invalid JSON data"}, status=400)
             if request.path == "/signup/":
                username = data.get("username")
                email = data.get("email")
                password = data.get("password")
                role=data.get("role")
                if not all([username, email, password,role]):
                    return JsonResponse({"error": "All fields are required"}, status=400)

                if not self.username_pattern.match(username):
                    return JsonResponse({"error": "Invalid username format"}, status=400)

                if not self.email_pattern.match(email):
                    return JsonResponse({"error": "Invalid email format"}, status=400)

                if not self.password_pattern.match(password): 
                    return JsonResponse({"error": "Weak password"}, status=400)

                if User.objects.filter(username=username).exists():
                    return JsonResponse({"error": "Username already exists"}, status=400)

                if User.objects.filter(email=email).exists():
                    return JsonResponse({"error": "Email already exists"}, status=400)
 
             if request.path == "/login/":
                username = data.get("username")
                password = data.get("password")
                print(password)

                if not all([username, password]):
                    return JsonResponse({"error": "Username & password required"}, status=400)

                try:
                    user = User.objects.get(username=username)
                    print(user)
                except User.DoesNotExist:
                    return JsonResponse({"error": "Invalid username"}, status=401)

                # if user.password != password:
                if not check_password(password,user.password):
                    return JsonResponse({"error": "Invalid password"}, status=401)

        response=self.get_response(request)
        return response