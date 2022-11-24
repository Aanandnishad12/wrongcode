
from flask import Flask, flash, render_template, url_for,flash,redirect,request
import requests
# from flask import request, url_for
from flask_sqlalchemy import  SQLAlchemy
# from requests import request
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from forms import RegistrationForm,LoginForm
from datetime import datetime
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash,check_password_hash
from flask_api import status
import pandas as pd
import re
import json

# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)
Bootstrap(app)



# db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:Anishad#123@localhost/flaskproject'
app.config["SECRET_KEY"]="IMAPROGRAMERALSOMATHMATACIANPHYSICIST"





db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "Login"

# migrate = Migrate(app, db)
from models import *


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))








# def 
# def totalcount():
#     count = MobileNumber.query.count()
#     return count



# @app.route("/date",methods=["POST","GET"])
# def download_report():
#     dictionay = {"customer_number":[],
#                  "zone":[],
#                  "customer_call_time":[]}
#     start_date = request.args.get("ChannelID",default=datetime.utcnow())
#     end_date = request.args.get("ChannelID",default=datetime.utcnow())

#     print(start_date,)
#     data = MobileNumber.query.filter(MobileNumber.customer_call_time.between("2022-07-11","2022-07-18")).all()


#     for i in data:

#         # print(i.customer_number)
#         dictionay["customer_number"].append(i.customer_number)
#         dictionay["zone"].append(i.customer_number)
#         dictionay["customer_call_time"].append(i.customer_call_time)

#         df = pd.DataFrame(dictionay)
#         df.to_excel("output.xlsx")

#     return "hello"



# @app.route("/sendmissedcalldetails",methods=["POST"])
# # @login_required
# def send_missed_call_details():
#     dic = {}
#     if request.method== "POST":
#         print("Hiiii___________________________________________________________")
#         who = request.args.get("who")
#         print(who)
#         ChannellD = request.args.get("ChannelID")
#         circle = request.args.get("Circle")
#         operator = request.args.get("Operator") 
#         datetim = request.args.get("DateTime")
#         print(who,ChannellD,circle,operator,datetim,"11"*25)
#         # try:
#         me = DATA(who=str(who),ChannellD=str(ChannellD),circle=str(circle),operator=str(operator),datetim=str(datetim))
#         db.session.add(me)
#         db.session.commit()
#         yourapicode = ""
#         TESTIN = ""
#         channl = "2"
#         DCS = "0"
#         flashsms = "0"
#         number = ""
#         textmessage = ""
#         route = "1"
#         register_entity_id = ""
#         register_dlt_id = ""
#         # veribale = requests.get(f""""https://www.smsgatewayhub.com/api/mt/SendSMS?APIKey=kueTbRNzm0SmJNH6XHyM0g&senderid=SAPATD&channel=2&DCS=8&flashsms=0&number=918898616379&text=माफ करा! आपण या क्रमांकावरून जास्त वेळा मिस कॉल दिला आहे. Regards- Sapat&route=1"""")
#         # return veribale.
#         pass

#         # except:
#         # # db.session.add(me)
#         # # db.session.commit()
#         #  return status 
    

@app.route("/")
@login_required
def Dash_Board():
        data = requests.post('http://15.206.107.10/login', json={'username': "office", 'password': "123456"})



        # print(data.text)
        reading = 400
        token = re.search(r'"token":"(.*?)","unique_uuid"',data.text).group(1)
        headers = {"Auth": str(token)}
        entirewhat = requests.get(f'http://15.206.107.10/entireWhat?per_page=1000&page=1',headers=headers)
        smsoffer = requests.get(f'http://15.206.107.10/sms-offer-all-page?per_page=1000&page=1',headers=headers)
        mydelta = json.loads(entirewhat.text)
        smsofferallpage = json.loads(smsoffer.text)
        all_conrect_code = set()
        correctcode = set()
        correctcode.add(1)
        correctcode.add(4)
        correctcode.add(5)
        correctcode.add(6)
        correctcode.add(7)

        my_list_of_data = []
        for i in smsofferallpage["listSms"]:
            if i["messeage_key"] in correctcode:
                if i["mobile_number"] not in all_conrect_code:
                    all_conrect_code.add(i["mobile_number"])
        for i in mydelta["listEntry"]:
        
            if i["mobile_number"] not in all_conrect_code:

                my_list_of_data.append(i)

        df = pd.DataFrame.from_dict(my_list_of_data)
        df1 = df[["id","mobile_number","sms_code"]]
        # def anand_aman(x):
        #     return x[:10]
        # delta_bro = df["created_at"].apply(anand_aman)
        df1["created_at"] = pd.to_datetime(df["created_at"])


        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d")
        # date_time = "2022-11-14"

        df2 = df1[df1["created_at"]>date_time]
        df2 = df2[(df2["mobile_number"] != "917058837748") & (df2["mobile_number"] != "919970755118") & (df2["mobile_number"] != "919144554411")]

    # df2.to_excel(f"wrong_code{date_time}.xlsx")
        # print(df2)
        dictionary = {}
        l = []
        for index, row in df2.iterrows():
            small_dictionary = {}
            small_dictionary["mobile_number"] = row["mobile_number"]
            small_dictionary["sms_code"] = row["sms_code"]
            small_dictionary["created_at"] = row["created_at"]
            l.append(small_dictionary)
        dictionary["list"] = l
        


        return render_template('dashboard1.html',dictionary=dictionary)


# @app.route("/totalgift")
# @login_required
# def Totalgift():
#     data = TotalGift.query.all()
#     return render_template('totalgift.html',data=data)




# @app.route("/zonewisenumber")
# @login_required
# def Zonewisenumber():

#     page = request.args.get("page", 1, type=int)
#     operator = request.args.get("Operator",default="9869258011")
#     data =MobileNumber.query.filter_by(zone=operator).paginate(page=page, per_page=5)

#     return render_template('zonewise.html',data=data)


@app.route("/login",methods = ["POST","GET"])
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        # return redirect(url_for("Dash_Board"))
    #     print(user,"3"*50)
        if user: 
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    #         # print(form.password.data)
    #         # print(user.passsword)
            # print("sha256$2pi8BpnTQXhTFALg$d0453a9b331fed69c01a7ef1c5d1acf683125cb0258265afaf4e61ba8456898f")
    #         return redirect(url_for("Dash_Board"))
            print(user.passsword,"============================================")
            print(form.password.data,"000000000000000000000000000000000000000000000")

            # if check_password_hash(user.passsword,form.password.data):
            if user.passsword==form.password.data:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                login_user(user,remember=form.remember.data)
            # print(user.passsword)
            # if user.passsword == form.password.data:
                # print("sha256$2pi8BpnTQXhTFALg$d0453a9b331fed69c01a7ef1c5d1acf683125cb0258265afaf4e61ba8456898f")

                return redirect(url_for("Dash_Board"))
    #     # newuser = 
    #     print(form.email.data,"------------------------------------")
    return render_template('login.html',title = "Login",form=form)


@app.route("/register",methods = ["POST","GET"])
def Register():
    form  = RegistrationForm()
    # if request.method== "POST"
    # print(form.email.data,"-----1111111111111111111---",form.username.data,form.password.data)
    if form.validate_on_submit():
        # print(hello)
        # print(form.email.data,"------------------------------------",form.username.data,form.password.data)
        hassed_passward = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data,email=form.email.data,passsword=hassed_passward)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("Dash_Board"))
        # flash(f"accont create for {form.username.data}!")
        # return redirect(url_for("Login"))
    return render_template('register.html',title="Registraion",form=form)


@app.route('/logout',methods=["GET","POST"])
@login_required
def logout():
    logout_user()
    flash("You have Been Out Thanks")
    return redirect(url_for("Login"))


@app.route('/creating-user',methods=["GET","POST"])
def createuser():
    data = request.get_json()
    _username = data["username"]
    _email = data["email"]
    _password = data["password"]

    delta = User(username=_username,email=_email,passsword=_password)
    db.session.add(delta)
    db.session.commit()

    # flash("You have Been Out Thanks")
    return "user has been created"


if __name__ == "__main__":
    app.run(debug=True,)
