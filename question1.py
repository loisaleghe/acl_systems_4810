from miracle import Acl


acl = Acl()
roles = ["radiologist", "physician", "nurse", "patient", "administrator", "technical_support"]
resources = ["patient_profile", "physician_contact", "diagnosis_test", "medical_images", "diagnosis_file", "prescription_file"]
time = ''
permission_Value = {}

#this function is for my abac model within the administrator to check the time interval is between 9am -5pm
def checkTime(time):
    #to check for values greater than 10, i did this because i didn't want complications when splitting
    if (int(time[:-2]) >= 10):
        if time[-2:].lower() == "pm":
            if (int(time[:-2]) == 12):
                return True
            time = int(time[:-2]) + 12
            if time >= 9 and time <= 17 :
                return True
            else:
                return False
        elif time[-2:].lower() == "am":
            if int(time[:-2]) >= 9 and int(time[:-2]) <= 17 :
                return True
            else:
                return False

    #to check for values less than 10
    elif (int(time[:-2]) <= 9):
        if time[-2:].lower() == "pm":
            time = int(time[:1]) + 12
            if time >= 9 and time <= 17 :
                return True
            else:
                return False
        elif time[-2:].lower() == "am":
            if (int(time[:1]) >= 9 and int(time[:1]) <= 17):
                return True
            else:
                return False


#Define a role.
#role: the role to define.
#The role will have no permissions granted, but will appear in get_roles().   

def addRole(role_name):
    acl.add_role(role_name)

#Define a resource.

#resources: the resource to define.
#The resource will have no permissions defined but will appear in get_resources()

def addResource(object):
    acl.add_resource(object)

#Define a permission on a resource.

#resource: the resource to define the permission on. Is created if was not previously defined.
#permission: the permission to define.    
#The defined permission is not granted to anyone, but will appear in get_permissions(resource).

def addPermission(role_name, permission):
    acl.add_permission(role_name, permission)

#Revoke a permission over a resource from the specified role
#role: The role to grant the access to
#resource: The resource to grant the access over
#permission: The permission to grant with

def revokePermission(role, resource, permission):   
    acl.revoke(role, resource, permission)
       
#to grant a permission over resource to the specified role.
#role: The role to grant the access to
#resource: The resource to grant the access over
#permission: The permission to grant with
#syntax for this is acl.grant(role, resource, permission)

def grantPermission(role, resource, permission):
    acl.grant(role, resource, permission)

#to view the permissions for a resource
#resource: the resource to get the permissions for

def getPermissions(resource):
    acl.get_permissions(resource)
            
#to update role if more roles need to be added 

def updateRole():
    for role in roles:
        addRole(role)

#to update resouurces if more need to be added 

def updateResources():
    for resource in resources:
        addResource(resource)

#the purpose of this function is to check what role is given and to grant that role permissions depending on the onject
#this is done using the miracle-acl grant function which is defined and explained above:

def authorize():
    for role in roles:
        if role == "radiologist" or role == "physician" or role =="nurse" or role == "patient":
            for resource in resources:
                if (resource == "patient_profile"):
                    addPermission(role, "read")
                    grantPermission(role, resource, "read")
                    permission_Value['patient_profile_for_radiologist_and_physician_and_nurse_and_patient:'] = 'read'


        
        if role == "administrator":
            print("Time of entry for Admin: format xam. for example ->10am, 2pm etc")
            inputTime = input()
            val = checkTime(inputTime)
            for resource in resources:
                if resource == "patient_profile":
                    if (val == True):
                        addPermission(role, "write")
                        grantPermission(role, resource, "write")
                        permission_Value['client_profile_for_aadministrator:'] ='write'
                    else:
                        revokePermission(role, resource, "write")
                
                if resource == "patient_profile":
                    if (val == True):
                        addPermission(role, "read")
                        grantPermission(role, resource, "read")
                        permission_Value['client_profile_for_administrator:'] = 'read'
                    else:
                        revokePermission(role, resource, "read")
                
                if resource == "diagnosis_file":
                    if (val == True):
                        addPermission(role, "read")
                        grantPermission(role, resource, "read")
                        permission_Value['diagnosis_file_for_administrator:'] = 'read'
                    else:
                        revokePermission(role, resource, "read")
                
                if resource == "prescription_file":
                    if (val == True):
                        addPermission(role, "read")
                        grantPermission(role, resource, "read")
                        permission_Value['prescription_file_for_administrator:'] = 'read'
                    else:
                        revokePermission(role, resource, "read")
       
        
        if role == "patient":
            for resource in resources:
                if resource == "physician_contact":
                    addPermission(role, "read")
                    grantPermission(role, resource, "read")
                    permission_Value['physician_contact_for_patient:'] =  'read'

        if role == "physician":
            for resource in resources:
                if resource == "physician_contact":
                    addPermission(role, "own")
                    grantPermission(role, resource, "own")
                    permission_Value['physician_contact_for_physician:'] = 'own'

                if resource == "prescription_file":
                    addPermission(role, "write")
                    grantPermission(role, resource, "write")
                    permission_Value['prescription_file_for_phyisician:'] = 'write'
                
        
        if role == "radiologist" or role == "physician" or role == "nurse":
            for resource in resources:
                if resource == "medical_images":
                    addPermission(role, "read")
                    grantPermission(role, resource, "read")
                    permission_Value['medical_images_for_radiologist_and_physician_and_nurse:'] = 'read'
        
        if role == "physician" or role == "radiologist":
            for resource in resources:
                if resource == "diagnosis_file":
                    addPermission(role, "write")
                    grantPermission(role, resource, "write")
                    permission_Value['diagnosis_file_for_physician&radiologist:'] = 'write'

        if role == "technical_support" :
            for resource in resources:
                if resource == "diagnosis_test":
                    addPermission(role, "execute")
                    grantPermission(role, resource, "execute")
                    permission_Value['diagnosis_test_for_technicalSupport:'] = 'execute'
                   
                
             
   #the purpose of this function is to get the values that i stored in the dictonary when i ran my authorize function         
def detailedInfo(role_name):
  
    for key, value in permission_Value.items():
        if role_name in key:
            print(key + " " + value)
    
            
   
    
    
   