import hashlib
import bcrypt

#add to userinfo to password file
def pswdToHashPswd(username, password, role):
    
    #to get the salt using bcrypt and store in a variable called salt. 
    #by default it is storing 16 bits
    salt = bcrypt.gensalt()

    #using bcrypt.hashpw to create hash code; the hashpw returns the salted function
    #and with this, note that only the first couple of characters of hashed are used for salt 
    #not the entire string 
    hashcode = bcrypt.hashpw(password.encode("utf8"), salt)

    #to store in text file
    userInfo = username + ";" + role + ";" + salt.decode('utf-8') + ";" + hashcode.decode('utf8') 
    
    with open("passwd.txt", "a") as txt_file:
        txt_file.write(userInfo + "\n") 

#retrieve information from password file using username 
def retrievePswd(username):
    received_pswd = []
   
    f = open("passwd.txt","r")

    for line in f:
        userReceivedInfo = line.split(";")

        username_stored = userReceivedInfo[0]
        if username_stored == username:
            userRole = userReceivedInfo[1]
            userpswd = userReceivedInfo[3]
            received_pswd = username_stored + " " + userpswd + " " + userRole
    
    return received_pswd
       
         



