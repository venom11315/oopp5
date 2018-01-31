import random
from firebase import firebase
firebase = firebase.FirebaseApplication('https://library-system-c45f5.firebaseio.com', None)

#get through list
'''result = firebase.get('/user', None)
person = result.values()
info = list(person)
infos = list(info[-1].values())
bn = str(infos[0])
print(bn)'''

#delete num
'''result = firebase.get('/user', None)
person =list(result.keys())[-1]
#get bicno value
personval = firebase.get('/user', '{}/bicno'.format(person))
print(personval)

num = firebase.get('/mynum', None)
bicn = list(num.values())
bicnumlist = []
for y in bicn:
    bicnumber = list(y.values())
    bicnumlist.extend(bicnumber)
print(bicnumlist)
for echnum in bicnumlist:
    if int(personval) == int(echnum):
        #delete echnum from firebase/mynum
    #remember to add the value back after html click clear interval'''

#delete format
'''num = firebase.get('/mynum', None)
nump = list(num.keys())
numlist = []

x = str(1)
for j in nump:
    justnum = firebase.delete('/mynum', '{}/bn{}'.format(j, x))
    numlist.append(justnum)
print(numlist)
print(nump)'''

#addnum
'''res = firebase.get('/mynum', None)
allnum = list(res.values())
jk = []
for f in allnum:
    xv = list(f.values())
    jk.extend(xv)
ranges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
diff = list(set(ranges) - set(jk))
for need in diff:
    justadd = firebase.post('/mynum', {
        'bn'+str(need):need
    })'''

'''getall = firebase.get('/mynum', None)
allkey = list(getall.keys())
add = []
for m in allkey:
    allseckey = firebase.get('/mynum', m)
    allval = list(allseckey.values())
    add.extend(allval)
print(add)'''

'''res = firebase.get('/mynum', None)
allnum = list(res.values())
jk = []
for f in allnum:
    xv = list(f.values())
    jk.extend(xv)
ranges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
diff = list(set(ranges) - set(jk))
print(diff)'''

'''et = firebase.get('/user', None)
        userdep = list(et.keys())[-1]
        getn = firebase.get('/user', '{}/deposit'.format(userdep))
        deduct = firebase.get('/price', None)
        deductkey = list(deduct.keys())[-1]
        dval = firebase.get('/price', '{}/price'.format(deductkey))'''
result = firebase.get('/ls', None)
firstchild = result.values()
lastchild = list(firstchild)
last = list(lastchild[-1].values())
lastlast = last[-1]
print(lastlast)
