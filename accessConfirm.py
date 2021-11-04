from question1 import *


authorize()
print(acl.check('patient', 'patient_profile', 'read'))
print(acl.check('nurse', 'diagnosis_file', 'write'))
print(acl.check('administrator', 'patient_profile', 'write'))
print(acl.check('physician', 'medical_images', 'read'))
