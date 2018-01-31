from firebase import firebase
firebase = firebase.FirebaseApplication('https://library-system-c45f5.firebaseio.com', None)

'''result = firebase.get('/user', None)
firstchild = result.values()
lastchild = list(firstchild)
last = list(lastchild[-1].values())
print(type(last[-1]))'''

result = firebase.get('/price', None)
#get -L3x-nMl8_Kv0NdHZHii
firstchild = list(result.keys())[-1]
#get random eg --> -L3x-nMl8_Kv0NdHZHii
#becomes '-L3x-nMl8_Kv0NdHZHii/name'
getname = firebase.delete('/price', '{}/name'.format(firstchild))
print(getname)
