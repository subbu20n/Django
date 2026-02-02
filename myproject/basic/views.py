from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import math 
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import UserProfile,Employee,User
from django.db.utils import IntegrityError
from django.contrib.auth.hashers import make_password,check_password
import jwt
from datetime import datetime, timedelta 
from django.conf import settings



# Create your views here. 
def home(request): 
    return render(request,'home.html') 

def about(request): 
    return render(request,'about.html')   

# def sample(request): 
#     return HttpResponse("hello")

# def sample1(request): 
#     return HttpResponse([1,2,3,4]) #1234 
   

# def sample1(request): 
#     return JsonResponse({"data":[1,2,3,4]})   #{"data": [1, 2, 3, 4]}


# def sample1(request): 
#     return JsonResponse({"data":["friz","tv","mixer"]})  #{"data":["friz","tv","mixer"]} 

# if we want tot send a list/array alone in the response 


# def sample1(request): 
#     return JsonResponse({"data":["friz","tv","mixer"]}) 
#     return JsonResponse([1,2,3,4]) 
#     return JsonResponse([1,2,3,4],safe=False) # it will give in json response and by default it have safe='true'

# def sample(request): 
#     info={"data":["akanksha","uma","sri"]} 
#     return JsonResponse(info) # now we call api    #{"data":["akanksha","uma","sri"]}

def sample1(request): 
    info={"data":[{"name":"akanksha","city":"hyd","gender":"female"},{"name":"uma","city":"hyd","gender":"female"},{"name":"sri","city":"hyd","gender":"female"}]} 
    return JsonResponse(info)  # it comes with names 
#{"data": [{"name": "akanksha", "city": "hyd", "gender": "female"}, {"name": "uma", "city": "hyd", "gender": "female"}, {"name": "sri", "city": "hyd", "gender": "female"}]}


#---------now i want to create a view which gives response as per my request------------  

# ------------------------Http methods--------------------- 

# get-->to retrive the data from server  
# post---> to add/insert data through server  
# put/patch---> to update data through server 
# delete ---> to delete data through server 

# get ----> to retrive the data from server  
# which getting some response based on the conditions and filters to that we need to give some instructions as a input 
# these instructions we can give using query params while making a get request  

# syntax---> http://127.0.0.1"8000\sample? name=harish&city=hyd  

def sample(request): 
    print(request) 
    qp1=request.GET.get("name") 
    return HttpResponse(f"hello{qp1}")  # qp1=query parameter 

def sample(request): 
    print(request) 
    qp1=request.GET.get("name") 
    qp2=request.GET.get("city")
    return HttpResponse(f"hello{qp1}")
    #return HttpResponse({qp1}is from {qp2})  # we can use multiple paramenters dynamically 


#--------------(11-12-2025)----****-Dynamic response--Filtering----&pagination-**********---------

# -----------------------Dynamic response-----------------

# [1,2,3,4,5,6,7,8,9,10] 

# 1. need to get numbers which are divisible by 4 
# 2. divisible by 3 


# def result(a): 
#     for x in list: 
#         if x%a==0: 
#             print(x) 

# result(3)
# result(4)
# result(5)  // i am filtering the dynamicall the response 

# 1.dynamic response as per the input in the request 
# {'product name':"","quantity":"price":}

# function: lo pass cheste it call as "parameter" 
# query parameter: lo pass cheste it call as "query parameter" 

#-----------dynamic response using query params------------------ 

def productInfo(request): 
    product_name=request.GET.get("product","mobile") 
    quantity=int(request.GET.get("quantity"))
    price=int(request.GET.get("price",25000))
    data={"product":product_name,"quantity":quantity,"price":price,"totalprice":price*quantity}
    return JsonResponse(data) 

#{"product": "laptop", "quantity": 2, "price": 25000, "totalprice": 50000}

#---------------------------Filtering----------------------------

#---------------------filtering using "query params"------------------------
data=[1,2,3,4,5,6,7,8,9,10]
def filteringData(request): 
    filteredData=[] 
    qp=int(request.GET.get("num",2))  # 2 is default value 
    for x in data: 
        if x%qp==0 : 
            filteredData.append(x) 
   # return JsonResponse(filteredData,safe=False)         #[2, 4, 6, 8, 10]
    return JsonResponse({"data": filteredData})         #{"data": [2, 4, 6, 8, 10]}

students_data = [{"name":'subbu',"city":"hyd"},{"name":"raju","city":"blr"}] 

def filterStudentsByCity(request): 
    filteredStudents=[] 
    city=request.GET.get("city","hyd") 

    for student in students_data: 
        if student["city"]==city: 
            filteredStudents.append(student) 
    return JsonResponse({"status":"success","data":filteredStudents})  

# {"status": "success", "data": [{"name": "subbu", "city": "hyd"}]}        

#-------------(13-12-2025)----------(Pagination--api--& -postman-)------------------- 

# as per limit ---> split the pages  
# as per the page num----> show the page content  

# page=1   limit=3 
# page=2   limit=3 

# start---->(page-1)*limit---->0 
# end------>page*limit---->3 

# page=2    limit=3 

# start--->3 
# end----> 6 

# page=3  limit=3 

# start--->6 
# end----->9 

#-----online compiler  

# import math 
# x = ['apple','banana','carrot','grapes'  #1st page 
#      'watermelon','kiwi','pineapple','custardapple', #2page
#      'strawberry','blueberry','dragonfruit'] #3page 

# page =1 #2
# limit =3 #2 
# start=(page-1)*limit  
# end=page*limit  

# op=x[start:end]      #['apple','banana','carrot'] 
# print(op)            #['carooot','grapes'] 
# total_pages=math.ceil(len(x)/limit)  
# print(total_pages)  #6 

import math 

def pagination(request): 
      data = ['apple','banana','carrot','grapes','watermelon','kiwi','pineapple','custardapple','strawberry','blueberry','dragonfruit'] 

      page=int(request.GET.get("page",1)) 
      limit=int(request.GET.get("limit",3))  
 
      start=(page-1)*limit  
      end=page*limit 
      total_pages=math.ceil(len(data)/limit) 

      result=data[start:end] 

      res={"status":"success","page":"current_page","total_pages":"total_pages","data":result}
      return JsonResponse(res,status=202)  

#{"status": "success", "page": "current_page", "total_pages": "total_pages", "data": ["apple", "banana", "carrot"]}


# we know how to build APi now 
# now we need to test the api in postman/ thunder  

#-------------------------postman---------------------

#postman: api tesing platform, frequently used by the backend developers 
# we can use the how can use the through the "web app"

# as a backend developer  
# 1.how to build apis 
# 2. hot to test them 
# 3. how to make documentation 

# api url----> 

# postman---->signup---->verification---->proceed 

# create workspace 
# make new http request by clicking new 
# make api call 
# if any error---> then download postman desktop agent 
# errors will resolve and postman will works 
 


# -----------(17-12-2025)---models & insert data into the table using ORM"-------- 

@csrf_exempt 
def createData(request): 
   if request.method=="POST":
       data=json.loads(request.body) 
       print(data) 
       return JsonResponse({"status":"success","data":data,"statuscode":201})    
   

@csrf_exempt 
def createProduct(request): 
   if request.method=="POST":
       data=json.loads(request.body) 
       print(data) 
       return JsonResponse({"status":"success","data":data,"statuscode":201})   
   
# ORM methods instead of manual queries  
#1. need to create object(row) with multiple fields(columns) and insert it in the table 

#---------to insert 'data' in table ' write logic 

@csrf_exempt 
def createData(request):
    try: 
        if request.method=="POST": 
            data=json.loads(request.body) #dictionary 
            name=data.get("name") 
            age=data.get("age") 
            city=data.get("city") 
            UserProfile.objects.create(name=name,age=age,city=city)
            print(data) 
            
        return JsonResponse({"status":"success","data":data,"statuscode":201},status=201)
    except Exception as e: 
        return JsonResponse({"statuscode":500,"message":"internal server error"})   
   


@csrf_exempt 
def createEmployee(request): 
    try: 
        if request.method=="POST": 
            data=json.loads(request.body)
            Employee.objects.create(emp_name=data.get("name"),emp_salary=data.get("sal"),emp_email=data.get("email")) 
            print(data) 
            return JsonResponse({"status":"success","data":data,"statuscode":201},status=201) 
    except IntegrityError as e: 
        return  JsonResponse({"status":"error","message":"inputs are invalid or not acceptable"})
  
    except Exception as e: 
        return JsonResponse({"status":"error","message":str(e)},status=500)  
    #finally("done") 


#-------(30-12-2025)--------------Update and Delete operation--------------------     

# CRUD 

# c and r 

# create DATA in TABLE 
# modelname.objects.create()
# GETDATA from table ----> modelname.objects.values() 
# Get Filtereddata ---> modelname.objects.filter(FIELD=VALUE).values()  

#-----------update----------------- 
# ID, Name, CITY 
# with reference of ID ---> want tp update city wih new value 

# modelname.objects.filter(REF_ID=VALUE).UPDATE(CITY=NEW_CITY) 
# modelname.objects.filter(ref_field_value).UPDATE(UPDATING_FIELD_VALUE) 

# this will update the all matched records  

# we need to send the data of "usersprofile" 

# # ----now i want to update city name as per ID --- 

@csrf_exempt  
def UpdateUserCityId(request): 
   try: 
       if request.method=="PUT":  
           input_data=json.loads(request.body)
           ref_id=input_data["id"] 
           new_city=input_data["new_city"] 
           update=UserProfile.objects.filter(id=ref_id).update(city=new_city) 
           if update==0: 
               msg="no records found" 
           else: 
               msg="record update" 
           print(update) 
           return JsonResponse({"status":"success","msg":msg},status=200) 
       return JsonResponse({"status":"failure","msg":"only put method is allowed"},status=400) 
   except Exception as e: 
       return JsonResponse({"status":"error","message":"something went wrong"}) 
 

@csrf_exempt
def updateUseragebyId(request,ref_id): 
    try: 
        if request.method=="PUT": 
            input_data=json.loads(request.body)
            ref_id=input_data["id"] 
            new_age=input_data["new_age"] 
            
            update = UserProfile.objects.filter(id=ref_id).update(age=new_age)
            if update == 0:
                msg="no record found with referrence of id"
            else:
                msg="record is updated successfully"
            return JsonResponse({"status":"success","msg":msg},status=200)
        return JsonResponse({"status":"failure",":msg":"only put method is allowed"},status=400)
    except Exception as e:
        return JsonResponse({"status":"error","message":"something went wrong"},status=500) 
    
# #----------------------DELETE--------------------
# modelname.objets.filter(ref_field=value).delete() 
@csrf_exempt 
def DeleteUserById(request,ref_id): 
    try: 
        if request.method=="DELETE":
            delete=UserProfile.objects.filter(id=ref_id).delete()
            print(delete[0]) 
            if delete[0]==0: 
                msg="no record is found to delete" 
            else: 
                msg="record is delete successfully" 
            return JsonResponse({"status":"success","msg":msg},status=200) 
        return JsonResponse({"status":"failure","msg":"only DELETE method is allowed"},status=400) 
    except Exception as e: 
        return JsonResponse({"status":"error","message":"something went wrong"},status=500) 

# #----------------CRUD apis completed ----------------
# task 
# # 1.create a model books  
# fields---> bookname, price,author,type 
# make migrations 
# 2. create api to insert data into the book model 
# 3. create api to retrive all records from book table  
# 4. create api to update book details by id or author 
# 5. create api to delete book from table by id 

#-------(07-01-2026)---------------middleware-------------------

@csrf_exempt  
def job1(request): 
    try: 
        if request.method=="POST": 
            return JsonResponse({"status":"success","message":"job1 applied successfully"}) 
        return JsonResponse({"status":"failure","message":"only post method allowed"}) 
    except Exception as e: 
        return JsonResponse({"status":"error","message":"something went wrong"},status=500)     
 
@csrf_exempt 
def job2(request):
    try: 
        if request.method=="POST": 
            return JsonResponse({"status":"success","message":"job2 applied successfully"}) 
        return JsonResponse({"status":"failure","message":"only post method allowed"}) 
    except Exception as e: 
        return JsonResponse({"status":"error","message":"something went wrong"},status=500)     

#---1.-create a account-------------->(signup)---------
# 1. string username --> 1 middle ware
# 2. correct email   --> 1-->1. middleware 
# 3. strong password  ---> 1.middleware

# for each one one seperate middleware middleware 
# -------------------------2.login --------------
# 1.correct username/email 
# 2. correct password

#-----------------(08-01-2026)----PERMONRMING (SIGNUP API) ----------------- 

#---SIGNUP API -----

# username --> a proper valid username and also unique 
# email ----> a proper valid email and also unique 
# password ---> a strong password 

# using regex 

# 1.username pattern 
# 2. email regex pattern 
# 3. password regex pattern  

# url----> signup 
# 1.model ---> username,email,password 
# 2.middleware ---> username,email,password 
# 3. view ---> signup ---> if al  3 'middlewares' validate then insert data into table  

# this is task for u 

#---------------(20-01-2026)----------AUTHENTICATION MIDDLEWARES-----------------------

# 1. signup view 
# 2. login view 

# Authentication 
# 1. signup 
# 2. validation ---> username,email, and password 

# middlware

# username ----> set of rules ---> regex 
# email --->set of rules --------> regex 
# passwords ---> set of rules---> regex 

# 3. it will create an account to the user as per user details 
# to insert data imto the table (pure business logic) 
# i will implement it inside the view  

# 1. model ---> username , email and password  
# 2. middleware -->  
# 3. view ---> 
# 4. url ---> 

@csrf_exempt
def signup(request):
    data = json.loads(request.body)
    hashed_password=make_password(data["password"])
    user = User.objects.create(
        username=data["username"],
        email=data["email"],
        password=hashed_password,
        role=data["role"]
    )

    return JsonResponse({
        "status": "success",
        "msg": "User registered successfully"
    }, status=201)

@csrf_exempt
def login(request):
    user_info=json.loads(request.body)
    username=user_info.get("username")
    user_existing_info=list(User.objects.filter(username=username).values())
    print(user_existing_info)
    
    payload={
        "username":username,
        "iat": datetime.utcnow(),
        "role":user_existing_info[0].get("role"),
        "exp": datetime.utcnow() + timedelta(seconds=settings.JWT_EXP_TIME)}

    token=jwt.encode(payload,settings.JWT_SECRET_KEY,algorithm=settings.JWT_ALGORITHM)

    return JsonResponse({

        "status": "success",
        "msg": "Login successful",
        "greetings":f"welcome {username}",
        "token":token
    })


#----------(28-1-2026)------------JWT token decoding&protected apis building -------------

@csrf_exempt
def protected_api(request):
    try:
        if request.method=="POST":
            auth_header = request.headers.get("Authorization")
            token=auth_header.split(" ")[1]
            print(token[1]) #readig token from input
            if not auth_header:
                return JsonResponse(
                    {"msg": "Authorization header missing"},
                    status=401
                )
            try:
                # print(auth_header)
                decoded_payload = jwt.decode(
                                    token,
                                    settings.JWT_SECRET_KEY,
                                    algorithms=[settings.JWT_ALGORITHM]
                                    )
                print(decoded_payload)
                if decoded_payload.get("role")=="admin":
                    return JsonResponse({"msg":"u have access for this api"})
                else:
                    return JsonResponse({"msg":"u have not access for this api"},status=401) 
                return JsonResponse({"msg":"successfully token recieved"})
            except Exception as e:
                return JsonResponse({"msg":"something went wrong","error":e})
        return JsonResponse({"msg":"done"})
    except:
        return JsonResponse({"msg":"only post method allowed"})
    
#--------Authorization ----> from client/postman  

# request.header.get("authorization")  ---> "bearer token"---> 
# auth = "bearer token" 
# auth.split("") 
# ["bearer","token"]   
# auth[1] --->token 
# 
# whenever we are building protected apis ---> need to validate the user information 
# whether he is having access or not 
# for taht we will use tokens 
# while login  ...token will generate 
# we need to send those tokens while making api requests through authorization with bearer token      

   