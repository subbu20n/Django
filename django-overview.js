// -------------------------DJANGO--------------------------------  

// what is web development ? 
// web development is about building websites or web applications that users interact with throw a browser 
// It ususally involves two main sides 
// FRONTEND (client side/user)---> what the users sessionStorage(HTMLAllCollection,CSS,JAVASCRIPT,REACT) 
// BACKEND(server side)---> Handles logic data storage and procesing(PaymentMethodChangeEvent, Django,Nodejs etc) 
// when both both FRONTEND and BACKEND are handled using python , we call it as full stack Developemnt 

// #------3-tier Architecture----
// 1.PRESENTATION LAYESR (FRONTEND UI) 
// what users see interface and interact with  
// made with HTML,CSS,JAVASCRIPT 
// EX: Buttons,Forms,Tables EventCounts. 
// In Django this is actually handled by templates(HTML Files)or through frontend frameworks(React,Angular etc).consuming apis 

// #--------2.APPLICATION LAYER(LOGIC LAYER)BACKEND-------------

// the heart of the apllication 
// Handles logic, validations,request processing 
// InDjango this includes 
//    views (business logic) 
//    models(data structures) 
//    Forms,serializers and middleware  

// #-------3.DATA LAYER--(DATABASE)---------

// Responsible for interacting with the dataabse 
// Django provides ORM (object relation mapper) --we write python code instead of sql queries 
// supported databases , SQLLITE,MYSQL,POSTGRESQL,ORACLE etc . 

// #-----APIs----bridge b/w systems----------
// API: Application peogramming interface is a communication link b/w two software systems  

// It defines how one system can talk to another system using structured requsts and responses  
// EX: 
// your frontend React app calls Django API--> Django fetched data from the database --> sends back a JSON response  

// #----------REQUESTS -Response Life Cycle -----

// 1.client sends request (browser,postman,frontend) 
// 2. server recieves request 
// 3. server validates & process data 
// 4. server fetches data (from DB or LOgic) 
// 5. server sends response (JSON,HTML,etc) 

// All this communication is handled through APIs 

// # -----------Django-----

// Two developers (adrian holovity and simon willison) invented Django frameworks 
// working in newsroom company---> lawrence journel -world,kanasa,usa 
// to overcome challenges ----> 
// 1. unexpected events 
// 2. sudden events 
// 3. urgent deadlines 
// 4. code from scratch everytime   ---> main problems ki solutions findout cheyadame DJANGO FRAMEWORKS 

// why they named as Django 
// 1. improvoised 
// 2.speed 
// 3.accurate
// 4.creativity 

// Library: collection of modules we will choose as per our requirements 
// FRAMEWORK: BLUE print(PLANNING) --like building construction   

// Django: is a web framework --> which can build a fulfilled web application easily and effeciently 
// 1. small kind of app ---> Django we can use completely for that 
// 2. large scale of app ---> FRONTEND + BACKEND (Django) 
 
// # ----------architecture----------
// M--->model----> to communicate with tables in the database from the backend  
// V---> Views---> logic is implemented here  
// T----> Templates ---> To render the content(using HTML) in the browser  

// # ---building an app with FRONTEND + BACKEND ----------   

// MODEL,VIEWS ----> plays very important role 
// T---> optional 

// ----------------virtual environment-------------
// Its a seperate environment for each and every project with indepenedent modules and packages 
// python -m venv name_venv 
// -m ---> is a flag stabds for module  
// -g ---> is a flag stands for global  
// to use venv --> we need to activate ---> .\scripts\venvname\activate 
// to deactivate---> deactivate  






// to create project---> django-admin startproject project_name  
// need to get inside the project 
// to start the server ---> python LockManager.py runserver 
// we got some migration warnings, so we made migrations for default models like AuthenticatorAssertionResponse,session,admin 

// after applying the migratins--> will create tables as per the default models  

// python LockManager.py migrate  
// python LockManager.py --help ---> to give all list of commands  


/// ---------------**process odf steps (Django)**-------------------

// 1.creating repo with readme and .gitignore  
// 2. cloning into any drive/folder through git bash 
// 3.open in vscode and create venv--->python -n venv venv 
// 4.acticate the venv--->.\venc\scripts\activate 
// 5.install Django with ---> pip install Django 
// 6. create project --> django-admin startproject project_name  
// 7.cd project 
// 8.create app---> django-admin startapp project_name  
// 9. add appname  in installed apps inside the 'settings.py' 
// 10. inside the project add 'requirements.txt' --> pip freeze > requireents.txt  
// 11. create 'template','view','url' 
// 12. make migrations---> python LockManager.py makemigrations  
//                 -----> python LockManager.pt migrate  
// 13. push the code into github by checking whether venv is ignoring or not 
// if it is not ignoring need to ignore it by mentioning venv name inside the gitignore 
// 14. check whether our server is working properly or not in local--> developemnt/testing phase 
// 15.need to deploy using render platform 
// 16. create account in render using github 
// 17. choose webservices 
// 18. add the repo url 
// 19. change the name of the app --> should not conatins "-","_" 
// 20. chosse language python3
// 21. branch main or any branch 
// 22. region--> singapore 
// 23. root directory---> .\project_folder 
// 24. build command---> pip install -r requirments.txt 
// 25. start command----> pythom LockManager.py 0.0.0.0:8000 
// 26. deploy the service  
// 27. will get issue with disallowed hosts---> needs to add host name inside the "settings.py" within allowed hosts 
// 28. again push the code  
// 29. automatically deploy will restart with latest commit in render 
// 30. installing, building and service will be live               


// //-------------10-12-2025 ----http and json server -------------------- 
// hello world 
// welcome ----> Http response  

// json response  
// {
//     "message": 'success',
//     "data": [1,2,3,4] 
// }

// // backend lo api build chestam 
// // frontend lo api ni integrate/access chestam

// 1 MVT Architecture  follow avutam 
// models 
// view 
// Templates  

// response can be provided in 3 ways  

// 1.templates----> used whenever we need to show static webpage as a response 
// 2. Http response-----> used whenever we need to send plain text/html text as a response 
//    data in plain text ---> 
//    eg: hello world,welcome to class ----> http response  

// 3. Json response----> json always expects a json object only 
//    by default---> json response allows only objects 
//    data in  json response  
//    {"user":'harish',"city":'hyd'} ---> json response  

//  from Django.http HttpResponse,JsonResponse  ---> we need to import this  




