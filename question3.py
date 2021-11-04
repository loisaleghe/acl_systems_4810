import pwinput
from question2 import pswdToHashPswd

print("Medview Imaging")
print("Medical Information Management System ")
print("Enrollment")
print("-------------------------------------------")
print("Enter username: ")
username = input()
print("Enter role: ")
role = input()
print("Enter password: ")
password = pwinput.pwinput()
print(password)

def passwordValidation(passwd):
    SpecialSym =['!', '@', '#', '$', '%', '?' '*']
    val = True
      
    if len(passwd) < 8:
        print('length should be at least 8')
        val = False
          
    if len(passwd) > 12:
        print('length should be not be greater than 12')
        val = False
          
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False
          
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#!%?*')
        val = False
    if val:
        return val
  

      
if (passwordValidation(password)):
    print("Password is valid")
    pswdToHashPswd(username, password, role)
else:
    print("Invalid Password !!")
               



