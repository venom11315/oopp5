from flask import Flask, render_template, request, session, flash
from loginrem import rem
from wtforms import Form, IntegerField
from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random

cred = credentials.Certificate('cred/library-system-c45f5-firebase-adminsdk-5ar18-7f7c1f0c15.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://library-system-c45f5.firebaseio.com'
})
root = db.reference()

app = Flask(__name__)
firebase = firebase.FirebaseApplication('https://library-system-c45f5.firebaseio.com', None)

class staffWeb(Form):
    numGen =IntegerField('Enter:')

@app.route('/', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        name = str(request.form["username"])
        mail = str(request.form["email"])
        pwd = str(request.form["password"])
        bno = str(request.form["bicnum"])
        amt = str(request.form["amount"])
        ok = root.child('user').push(
            {
                'name': name,
                'email': mail,
                'pwd':pwd,
                'bicno': bno,
                'deposit': amt
            }
        )
        session['sname'] = name
        session['sbicno'] = bno
        session['sdep'] = amt
        return render_template("obikehp.html")

    result = firebase.get('/user', None)
    person = list(result.keys())[-1]
    # get bicno value
    personval = firebase.get('/user', '{}/bicno'.format(person))

    num = firebase.get('/mynum', None)
    bicn = list(num.values())
    bicnumlist = []
    for y in bicn:
        bicnumber = list(y.values())
        #add bicn into list
        bicnumlist.extend(bicnumber)

    nump = list(num.keys())
    for echnum in bicnumlist:
        if int(personval) == int(echnum):
            #each wesdfgerhd in nump
            for enum in nump:
                getrne = firebase.get('/mynum', '{}/bn{}'.format(enum, str(echnum)))
                session['savebns'] = getrne
                rn = firebase.delete('/mynum', '{}/bn{}'.format(enum, str(echnum)))
    # delete echnum from firebase/mynum

    getall = firebase.get('/mynum', None)
    allkey = list(getall.keys())
    add = []
    for m in allkey:
        allseckey = firebase.get('/mynum', m)
        allval = list(allseckey.values())
        add.extend(allval)
    add1 = random.choice(add)

    return render_template("user.html", show=add1)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = str(request.form["username"])
        pwd = str(request.form["password"])
        bno = str(request.form["bicnum"])
        amt = str(request.form["amount"])
        result = firebase.get("/user", None)
        rubbish = list(result.keys())
        namelist = []
        pwdlist = []

        for x in rubbish:
            rubname = firebase.get('/user', '{}/name'.format(x))
            rubpwd = firebase.get('/user', '{}/pwd'.format(x))
            namelist.append(rubname)
            pwdlist.append(rubpwd)
        if name not in namelist and pwd not in pwdlist:
            getall = firebase.get('/mynum', None)
            allkey = list(getall.keys())
            add = []
            for m in allkey:
                allseckey = firebase.get('/mynum', m)
                allval = list(allseckey.values())
                add.extend(allval)
            add1 = random.choice(add)
            message = "Try error"
            return render_template("success.html", show=add1, mes=message)
        if name in namelist and pwd in pwdlist:
            session['name'] = name
            session['bno'] = bno
            session['dep'] = amt

            # deletebicno
            num = firebase.get('/mynum', None)
            bicn = list(num.values())
            enum = list(num.keys())
            bicnumlist = []
            for y in bicn:
                bicnumber = list(y.values())
                # add bicn into list
                bicnumlist.extend(bicnumber)
            for j in bicnumlist:
                if str(j) == str(session["bno"]):
                    for s in enum:
                        getrn = firebase.get('/mynum', '{}/bn{}'.format(s, str(j)))
                        session['savebn'] = getrn
                        rn = firebase.delete('/mynum', '{}/bn{}'.format(s, str(j)))
            return render_template("obikehp.html")
        return render_template("obikehp.html")

    getall = firebase.get('/mynum', None)
    allkey = list(getall.keys())
    add = []
    for m in allkey:
        allseckey = firebase.get('/mynum', m)
        allval = list(allseckey.values())
        add.extend(allval)
    add1 = random.choice(add)
    return render_template("success.html", show=add1)

@app.route('/home', methods=['GET','POST'])
def home():
    if request.method == "POST":
        return render_template("topup.html")
    result = firebase.get('/ls', None)
    rubbish = list(result.keys())[-1]
    lastlast = firebase.get('/ls', '{}/Number'.format(rubbish))

    name = session.get('name', '')
    sname = session.get('sname', '')
    if name != '':
        nlast = session['name']
        diff = session['savebn']
        #numbers not in database
        return render_template("obikehp.html", numbGen=lastlast, sname=nlast, here=diff)
    if sname != '':
        nlast = session['sname']
        diff = session['savebns']
        # numbers not in database
        return render_template("obikehp.html", numbGen=lastlast, sname=nlast, here=diff)


@app.route("/staff", methods=['GET', 'POST'])
def staff():
    if request.method == 'POST':
        num = str(request.form["num"])
        new_user = root.child('ls').push({'Number': num})
        return render_template("numGen.html", variable=num)
    return render_template("staff.html")


@app.route("/balance", methods=['GET', 'POST'])
def balance():
    if request.method == 'POST':
        return render_template("mypayment.html")
    name = session.get('name', '')
    sname = session.get('sname', '')
    if name != '':
        bicno = session['dep']
        return render_template("topup.html", dep=bicno)
    elif sname != '':
        bn = session['sdep']
        return render_template("topup.html", dep=bn)

@app.route("/payment", methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        return render_template("success.html")

    name = session.get('name', '')
    sname = session.get('sname', '')
    checkname = firebase.get('/price', None)
    dump = list(checkname.keys())
    namelist = []
    pricelist = []
    for x in dump:
        good = firebase.get('/price', '{}/name'.format(x))
        good2 = firebase.get('/price', '{}/price'.format(x))
        namelist.append(good)
        pricelist.append(good2)

    if name != '':
        for anoy in namelist:
            if str(name) == str(anoy):
                this = namelist.index(anoy)
                fprice = pricelist[this]
                ori = session['dep']
                return render_template("mypayment.html", ded=fprice, depo=ori)
    elif sname != '':
        for anoy in namelist:
            if str(sname) == str(anoy):
                this = namelist.index(anoy)
                fprice = pricelist[this]
                ori = session['sdep']
                return render_template("mypayment.html", ded=fprice, depo=ori)

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)
