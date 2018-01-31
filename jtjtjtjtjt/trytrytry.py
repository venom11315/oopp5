from firebase import firebase
firebase = firebase.FirebaseApplication('https://library-system-c45f5.firebaseio.com', None)

num = firebase.get('/mynum', None)
bicn = num.values()
biclist = []
for x in bicn:
    bv = list(x.values())
    for i in bv:  # x is a list --> EG) dict_value([0])
        biclist.extend(str(i))
print(biclist)

result = firebase.get('/user', None)
person = result.values()
info = list(person)
infos = list(info[-1].values())
bn = str(infos[0])
print(bn)
