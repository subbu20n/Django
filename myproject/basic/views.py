from django.shortcuts import render
from django.http import HttpResponse,JsonResponse 
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

page=int(request.GET.get("page"),1) 
limit=int(request.GET.get("limit"),3) 

start=(page-1)*limit  
end=page*limit 
total_pages=math.ceil(len(data)/limit) 

result=data[start:end] 

res={"status":"success","page":"current_page","total_pages":"total_pages","data":"result"}
return JsonResponse(res) 