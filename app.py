
import json
from firebase import firebase

url = ""
firebase = firebase.FirebaseApplication(url, None)
result_users = firebase.get('/users', None)
result_pigs = firebase.get('/pig_logs_',None)
#for p in result.read():
#  print(p)

print(result_users,result_pigs)
