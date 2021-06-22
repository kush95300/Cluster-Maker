from flask import Flask, render_template
from flask import request
from random import randint


app = Flask("Cluster Maker")

@app.route("/")
def home():
    print("cluster ")
    #return "Cluster Maker"
    return render_template("index.html")


@app.route("/setdefault")
def setdefaults():
    return render_template("default.html")


@app.route("/selectpage")
def slectpage():
    return render_template("selectpage.html")


@app.route("/createdefaultcluster")
def defaultsclustermaker():
    return "Creating Default Cluster"

@app.route("/createadvancecluster")
def advanceclustermaker():
    return render_template("advanceform.html")

@app.route("/defaultcost")
def defaultcost():
    return "Default cost Output"

@app.route("/login")
def accountauth():
    return "login Page"

@app.route("/signup")
def createaccount():
    return "Signup Page"




@app.route("/findcost")
def findcost():
    return render_template("cost_analyser.html")

@app.route("/chooseform")
def chooseform():
    return render_template("choice.html")



@app.route("/costanalysis")
def analysecost():
    nn = request.args.get("nn_instance_type")  
    dn = request.args.get("dn_instance_type")
    jt = request.args.get("jt_instance_type")
    tt = request.args.get("tt_instance_type")
    dnc = request.args.get("dn_count")
    ttc = request.args.get("tt_count")
    ebs = request.args.get("ebs")
    if ebs == "yes":
        size = request.args.get("ebssize")
    else:
        size=0
    usr_m = (int(dnc) + int(ttc) +2) * 0.5 + int(size) * 0.1
    inr_m = usr_m*73
    return " data : Cost Analysis {} {} {} {} {} {} {} {} <br> <br> Total Cost: {} $  or Rs {} ".format(nn,dn,dnc,jt,tt,ttc,ebs,size,usr_m,inr_m)


@app.route("/defaultform")
def defaultform():
    print("Default Form")
    return "Default Form"


@app.route("/advanceform")
def advanceform():
    print("Advance Form")
    return "Advance Form"

def sendotpmail(otp,email):
    #ansible mail
    
    print("send mail")
    


@app.route("/loginotp")
def getotp():
    otp=randint(100000,999999)
    email = request.args.get("email")  
    sendotpmail(otp,email)
    return "ok"