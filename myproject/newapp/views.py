from django.shortcuts import render
from django.http import JsonResponse
from newapp.models import OrderDetails,movieBooking
import json 
from django.views.decorators.csrf import csrf_exempt  

# Create your views here.

@csrf_exempt 
def orderPlacing(request): 
    try: 
        if request.method=="POST": 
            data=json.loads(request.body) 
            order= OrderDetails.objects.create(
                orderid=data["order_id"] ,
                usermail=data["email"] ,
                amount=data["amount"],
                mode=data["mode"]                   
            )
            print(order.transaction_id)
            x=order.transaction_id

            return JsonResponse({"status":"success","message":"payment details updated successfully","transaction_id":x}, status=201)
        else:  
            return JsonResponse({"error":"only post method is allowed"},status=400) 
    except Exception as e: 
        return JsonResponse({"error":str(e)},status=500)     
    

@csrf_exempt
def BookMyShow(request): 
  try:  
    if request.method=="POST": 
        data=json.loads(request.body) 
        movieBooking.objects.create(
            moviename=data["movie_name"] ,
            showtime=data["show_time"],
            screenname=data["screen_name"] 
        )
        return JsonResponse({"status":"success", "message":"records inserted successfully"}) 
    return JsonResponse({"status":"failure","message":"only post method allowed"}) 
  except Exception as e:  
      return JsonResponse({"message":"something went wrong"}) 
  
  # so now we know how to create data, CRUD ---> CREATE COMPLETE 

  # GET---->'R' --READ 
  # no need to create new model we can use for getting data existing table  

def GetOrders(request): 
      try: 
          if request.method=="GET": 
              result=list(OrderDetails.objects.values()) #to get all the values from the table 
              print(result) 
              if len(result)==0: 
                   msg= "No record found" 
              else: 
                    msg= "data retrived successfully"   
              return JsonResponse({"status":"success","message":"msg","data":result,"total no of records":len(result)}) 
          return JsonResponse({"status":"failure","message":"only get method allowed"})
      except Exception as e: 
          return JsonResponse({"message":"something went wrong"}) 


def BookingDetails(request): 
    try: 
        if request.method=="GET": 
            result=list(movieBooking.objects.values()) 
            if len(result)==0: 
                msg="no records found" 
            else: 
                msg="data retrived successfully" 
            return JsonResponse({'status':"success","message":msg,"data":result,"total no of records":len(result)}) 
        return JsonResponse({"status":"failure","message":"only get method allowed"}) 

    except Exception as e: 
        return JsonResponse({"message":"something went wrong"}) 
    
# --------------path params------------------:
# path params: is also one parameter we can pass while making a api --> to get the response parameter 
# query paremater: to pass the extra information to get response as per request we can use for pagination,filteration,validation 
# query params: if we wont provide the value it takes default value 
# path params: we need to get provide the particular id, or category it gives only one object 
#
# url?key=value-----> query params  
# url/value -----> path params 

# url?key=value----->request.GET.get("key") 
# url/value---->  
# this we can read at the url path ---> urlpath/<int:id> 
#                                  ---> urlpath/<str:ctg>   


student_info=[{"id":"vasanth"},{"id":2,"name":"krishna"},{"id":3,"name":"krishna"}] 

def getStudentsById(request,id): 
    filteredStudent=[] 
    
    for student in student_info: 
       if id ==student["id"]:  
           filteredStudent.append(student) 
    return JsonResponse({"data":filteredStudent})

#---------------(26-12-2025)---------GET --& CREATE OPERATIONS----------------------(using path params) 

student_info=[{"id":1,"name":"vasanth","degree":"EEE",},{"id":2,"name":"subbu","degree":"ECE",},{"id":3,"name":"bhanu","degree":"EEE",},{"id":4,"name":"arun","degree":"cse",}]
def getStudentsByDegree(request,degree): 
    try: 
        if request.method=='GET': 
            DegreeBasedFilteration=[]
            
            for student in student_info: 
                if degree.lower()==student["degree"].lower():  
                    DegreeBasedFilteration.append(student) 
                    if len(DegreeBasedFilteration)==0: 
                        msg= "no results found"
                    else: 
                        msg= "students record fetched succesfully" 
                    
                    return JsonResponse(
                        {"status":"success",
                         "no of records":len(DegreeBasedFilteration),
                         "data":DegreeBasedFilteration,
                         "msg":msg}
                    )
                return JsonResponse({"status":"failure","message":"only get method alowed"},status=400) 
    except Exception as e: 
        return JsonResponse({"status":"error","msg":"something went wrong,check code once"}) 


def getStudentsbyId(request,id): 
    filteredStudent=[] 
    for student in student_info: 
        if id==student["id"]: 
            filteredStudent.append(student) 
        return JsonResponse({"data":filteredStudent})     
    
# if we are expecting only single record is available  

def getOrderByStatus(request,status_param): 
    try: 
        if request.method=="GET": 
            data=OrderDetails.objects.get(status=status_param) # it works only single object 
            print(data.orderid) 
            print(data.mode) 
            ResponseObject={"id":data.orderid,"amount":data.amount,"mode":data.mode} 
            return JsonResponse({"status":"success","msg":"records fetched successfully","data":ResponseObject})
        return JsonResponse({"status":"failure","msg":"only get method allowed"},status=500) 
    except Exception as e: 
        return JsonResponse({"status":"error","msg":"something went wrong"},status=500) 
    
#-------we are expecting multiple records,based on filteration-----------

def getMultipleOrdersByStatus(request, status):
    try:
        if request.method == "GET":
            data = OrderDetails.objects.filter(status=status)

            final = list(
                data.values(
                    "id",
                    "useremail",
                    "orderid",
                    "amount",
                    "currency",
                    "transaction_id"
                )
            )

            if len(final) == 0:
                msg = "no records found"
            else:
                msg = "records fetched successfully"

            return JsonResponse(
                {"status": "success", "msg": msg, "data": final},
                status=200
            )

        return JsonResponse(
            {"status": "failure", "msg": "only get method is allowed"},
            status=400
        )

    except Exception as e:
        return JsonResponse(
            {"status": "error", "msg": "something went wrong"},
            status=500
        )

# -------(27-12-2025)----------GET data by using Filteration------using path params -----------
# 
# document cheyali for every api 
#  
# url: http:127.0.0.1:8000 
# 1. to book a movie ticket  
# urlpath---> bookticket/ 
# path pattern----> no 
# query param----> no 
# Body---> sample data=
# {
#     "movie_name":"eesha",
#     "show_time": "8pm",
#     "screen_name": "screen1" 
# }
# postman scrrenshot json paste here 

# document cheyali everything for every api 

#----------- now i want to get the "movie details" as per the screen------*

def getMoviesByScreenname(request,screen): 
    try: 
        if request.method=="GET": 
            data=movieBooking.objects.filter(screenname=screen).values() 
            final_data=list(data) 
            if len(final_data)==0: 
                msg="no records found" 
            else: 
                msg="records fetched successfully"  
            return JsonResponse({"status":"success","data":final_data},status=200)         
        return JsonResponse({"status":"failure","msg":"only get method allowed"},status=400) 
    except Exception as e: 
        return JsonResponse({"status":"error","msg":"something went wrong"}) 
    
#-----------------get multiple screens----------

  
def getMoviesByMultipleScreens(request,first,second):
    try:
        if request.method=="GET":
            data1=movieBooking.objects.filter(screenname=first).values()
            data2=movieBooking.objects.filter(screenname=second).values()
            first_data=list(data1)
            second_data=list(data2)            
            return JsonResponse({"status":"success",first:first_data,second:second_data},status=200)
        return JsonResponse({"status":"failure","msg":"only get method allowed"},status=400)
    except Exception as e:
        return JsonResponse({"status":"error","msg":"something went wrong"})    