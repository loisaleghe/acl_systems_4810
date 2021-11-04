import pwinput
import bcrypt
from question2 import retrievePswd
from question1 import *
from miracle import Acl


def accessInformation():
    authorize()
    userRole = info[2]
    print("-----------------------")
    print("UserId: " + username)
    print("role: " + userRole)
    print("-------------------")
    print("attributes below:" )
    if userRole.lower() in acl.get_roles():      
        detailedInfo(userRole.lower())
    else:
        print("role doesn't exist")



print("Medview Imaging")
print("Medical Information Management System ")
print("-------------------------------------------")
print("Enter username: ")
username = input()
print("Enter password: ")
password = pwinput.pwinput()
print(password)



f = open("passwd.txt","r")

# setting flag and index to 0
flag = 0
index = 0

# Loop through the file line by line
for line in f:  
    index += 1 
      
    # checking string is present in line or not
    if username in line:       
      flag = 1
      break 
          
# checking condition for string found or not
if flag == 0: 
   print("You are not a registered user")
else: 
    value = retrievePswd(username)
    info = value.split()
    booleanValue = bcrypt.checkpw(password.encode('utf8'), info[1].encode('utf8'))

    if(booleanValue):
        print("Grant Access")   
        accessInformation()
    else:
        print("You have no access")
  
# closing text file    
f.close()



   




