#----------------------------regex(regular expressions)--------------------

# x=12345
# y=25.45 
# a="hello"
# ip="har123....123com" 

#regex is used to validate ,extract,replace a specific patterns 
# pancard="kihjo3987r" 
# "5a1phabets4numberssinglealphabet"
# r"[a-z]{5}[0-9]{4}[a-z]{1}"   # regex pattern 

# match()
# search()
# fullmatch()
# find()
# findall()
# sub()
 
# to define the patterns using regex 
# r"pattern" 
#1.every string should starts with IND 
#eg: INDhello,INDWELcome,IND1234,INDok 

#---------match()----------
import re 
#re.match(pattern,input)
# x=re.match(r"IND","IND123")
# if x: 
#     print("it is valid input only") 
# else: 
#     print("invalid input") 

# match method will check only at the starting of the input string 
# to check the prefix of given string 
# "SBIN98737"
# "ICICI0098"
# "AXIS97887" 

# ifsc="SBIN12345"
# sbivalidate=re.match(r"SBIN",ifsc) 
# if sbivalidate: 
#     print("it is valid sbi ifsc") 
# else: 
#     print("invalid sbi ifsc") 

# ifsc="AXIS12345"
# sbivalidate=re.match(r"SBIN",ifsc) 
# iciciValidate=re.match(r"ICICI",ifsc) 
# axisValidate=re.match(r"AXIS",ifsc) 

# if sbivalidate:
#     print("it is valid sbi ifsc") 
# elif iciciValidate:
#     print("it is valid icici ifsc") 
# elif axisValidate: 
#     print("it is valid axis ifsc") 
# else: 
#     print("it is valid axis ifsc") 

#-------search()------  

# bio="Akhil knows python and sql" 
# x=re.search(r"python",bio) 
# print(x)  


# bio="Akhil knows python and sql" 
# x=re.search(r"python",bio) 

# if x: 
#     print("will hire the person") 
# else: 
#     print("will not hire") 


#---

ip1="cat"
ip2="cut"
ip3="clt"
ip4="blt"
ip5="catch" 

x=re.match(r"c.t",ip1) #cat
x=re.match(r"c.t",ip2) #cut
x=re.match(r"c.t",ip3) #clt 
x=re.match(r"c.t",ip4)  #none  

print(x) 

# . is basic regex pattern indicates any character can be present 
# ^ indicates pattern/string should starts with 
# $ indicates patterns/string should ends with 
# [a-z] indicates string should contains any alphatetes range 
# input should always starts with any numbers 
# ^ 
# [0-9] 
# {m} indicates length of string
# {m,} --> indicates minimum should be 'm' and maximum anything 
# {m,n} --> indicates max and min length of string 
# [0-9] --> indicates the range of numbers from 0-9 

ip1 = "10000coders" 
ip2 = "10000coders" 
ip3 = "10000coders" 
ip4 = "10000coders" 
ip5 = "10000"

x=re.match(r"6[0-9]{1,}[a-z]{2,}$",ip5) 
print(x) 

pan1="DEPLM9067T" 
validate=re.match(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$".pan1) 
print(validate) 

# next we will do regex pattern to 'strong email password,username we see 'now'----

# mobile_num_patterns=r"^[7-8]{1}[0-9]{9}$" 
# ip="75241179632" 
# op = re.match(mobile_num_pattern,ip) 
# print(op) 


#----------user name------------- 
# username can contains LC,UC, DIGITS_ and length 
# should be in b/w 8 and 15 

username_pattern = r"6[A-Za-z0-9_\.]{8,15}" 
ip="James.999" 
op=re.match(username_pattern,ip) 
print(op) 

# -----strong password ---------- 
password=r"^(?=.[A-Z])(?=.*[a-z])(?=.*[0-9])(A-Za-z0-9@._){9,12}$" 

#(?=.*[A-Z]) --> assure atleast one uppercase in string 
# (?=.*[a-z]) --> assure atleast one lowercase in string 
# (?=.*[0-9]) --> assure atlest one digit in string 
# 
pswd='india@123' 
pswd='InDIA@123' 

pop=re.match(password_pattern,pswd) 
print(pop) 

#------------email-----------  

email1=harish.tech@gmail.com 
# email2=subbu123.tech@yahoo.in 
# email3=_kiran.mgr@10000coders.in 
# # 1.pattern before@  
# 2. pattern after@
# 3 . pattern for domain name before and after  

email_pattern = r"^[A-Za-z0-9._]+@[A-Za-z0-9]+\.[a-zA-Z]{2,}$" 
op=re.match(email_pattern,email1) 
print(op) 

