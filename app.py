from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
#Added SSLify 
#from flask_sslify import SSLify

from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)

 
app = Flask(__name__)
app.secret_key = os.urandom(12)

#Added path redirect for app feb. 23
#sslify = SSLify(app)
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')
#        return "Hello Boss!  <a href='/logout'>Logout</a>"

@app.route('/mapdownload')
def mapdownload():
    if not session.get('logged_in'):
       return render_template('login.html')
    else:
        return render_template('mapDownloads.html')
      
#country specific download pages


@app.route('/mapdownload/kenya')
def kenya():
    if not session.get('logged_in'):
       return render_template('login.html')
    else:
        return render_template('kenya.html')
      
@app.route('/mapdownload/malawi')
def malawi():
    if not session.get('logged_in'):
       return render_template('login.html')
    else:
        return render_template('malawi.html')
      
@app.route('/mapdownload/tanzania')
def tanzania():
    if not session.get('logged_in'):
       return render_template('login.html')
    else:
        return render_template('tanzania.html')
      
@app.route('/mapdownload/uganda')
def uganda():
    if not session.get('logged_in'):
       return render_template('login.html')
    else:
        return render_template('uganda.html')
      
@app.route('/mapdownload/zambia')
def zambia():
    if not session.get('logged_in'):
       return render_template('login.html')
    else:
        return render_template('zambia.html')
      
@app.route('/mapdownload/cambodia')
def cambodia():
    if not session.get('logged_in'):
       return render_template('login.html')
    else:
        return render_template('cambodia.html')
      
@app.route('/mapdownload/myanmar')
def myanmar():
    if not session.get('logged_in'):
       return render_template('login.html')
    else:
        return render_template('myanmar.html')
      
@app.route('/mapdownload/philippines')
def philippines():
    if not session.get('logged_in'):
       return render_template('login.html')
    else:
        return render_template('philippines.html')
      
@app.route('/mapdownload/srilanka')
def srilanka():
    if not session.get('logged_in'):
       return render_template('login.html')
    else:
        return render_template('srilanka.html')
      
@app.route('/mapdownload/ecuador')
def ecuador():
    if not session.get('logged_in'):
       return render_template('login.html')
    else:
        return render_template('ecuador.html')
      
@app.route('/mapdownload/honduras')
def honduras():
    if not session.get('logged_in'):
       return render_template('login.html')
    else:
        return render_template('honduras.html')
      
# end of 11 country pages
      
      
@app.route('/about')
def about():
    if not session.get('logged_in'):
       return render_template('login.html')
    else:
        return render_template('about.html')
      
@app.route('/contact')
def contact():
    if not session.get('logged_in'):
       return render_template('login.html')
    else:
        return render_template('contact.html')
      
@app.route('/mapviewer')
def mapviewer():
    if not session.get('logged_in'):
       return render_template('login.html')
    else:
        return render_template('mapviewer.html')

 
@app.route('/login', methods=['POST'])
def do_admin_login():
 
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
 
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()
 
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
  

 
if __name__ == "__main__":
#The following line works for local. Uncomment for local only  
#    app.run(debug=True,host='0.0.0.0', port=4000)
#The following line is for app.py to run on EC2 instance.
   app.run(debug=True)

