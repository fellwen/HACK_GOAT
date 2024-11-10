import datetime
from flask import Flask, redirect, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os
import matplotlib.pyplot as plt
import matplotlib
import ollama
matplotlib.use('Agg')
app = Flask(__name__)

bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Event(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   date = db.Column(db.Date, nullable=False)
   name = db.Column(db.String(255), nullable=False)

def nerou(prompt, name):
   response = ollama.chat(model='llama3.2', messages=[
               {'role': 'user','content': prompt,},])
   r2 = response['message']['content']
   


   print(prompt)
   r2l2 = r2.split()
   name2 = name.split()
   delsimvol = [',', '.', '!', ':', '?']
   i = 0
   print(name2, " До")
   while i < len(name2):
      for a in delsimvol:
         name2[i] = name2[i].replace(a, '')
      i = i + 1

   print(name2, " После")
 

   if name2.count('TTT') > 0:
      r2 = "ТТТ - это организация для создания атомной бомбы. Это только пример информации"
      print('сработало1')
   if name2.count('ТТТ') > 0:
      r2 = "ТТТ - это организация для создания атомной бомбы. Это только пример информации"
      print('сработало2')
   if name2.count('Шерегеш') > 0:
      r2 = "Шерегеш - сдесь инфа которую должна выдавать нейросеть"
      print('сработало1')
   return r2


def func():
   #file = "data.txt"
   #file = open(file, encoding='UTF-8')
   #text = file.read()
   #print(text, "--------------------------------------")
   #text = ""
   #x1 = file.readline()
   #x1 = int(x1)
   #x2 = file.readline()
   #x2 = int(x2)
   #y1 = file.readline()
   #y1 = int(y1)
   #y2 = file.readline()
   #y2 = int(y2)
   #t1 = file.readline()
   #t2 = file.readline()

   left = [2, 1]
   height = [2, 4]
   tick_label  = ['ФАКТ', 'ПЛАН']
   plt.bar(left, height, tick_label=tick_label, width=0.6, color=['#00AF00'])
   plt.ylabel('y - axis')
   plt.xlabel('x - axis')
   plt.title('Название бара')
   return plt
 
   


@app.route('/', methods=['POST'])
def add_event():
   name = request.form['searchMenu']
   print(name, sep='\n')

   sheregesh = "Если я задам вопрос который не относится к Шерегешу то отвечай 'Об этом нет информации'.\nИ так... "
   prompt = sheregesh + name
   r2=nerou(prompt, name)
   plot = func()
   plot.savefig('static/src/img/plot.png')
   plot.close()

   return render_template("index.html", h1 = r2)



@app.route("/")
def index():
   plot = func()
   plot.savefig('static/src/img/plot.png')
   plot.close()
   return render_template("index.html")






@app.route("/index2.html", methods=['POST'])
def get_page_about2():
   name = request.form['searchMenu2']
   print(name, sep='\n')

   sheregesh = "Если я задам вопрос который не относится к Шерегешу то отвечай 'Об этом нет информации'.\nИ так... "
   prompt = sheregesh + name
   r2=nerou(prompt, name)
   return render_template("static/index2.html", h1=r2)

@app.route("/index2.html")
def get_page_about():
   name = request.form['searchMenu2']
   print(name, sep='\n')

   sheregesh = "Если я задам вопрос который не относится к Шерегешу то отвечай 'Об этом нет информации'.\nИ так... "
   prompt = sheregesh + name
   r2=nerou(prompt, name)
   return render_template("static/index2.html", h1=r2)



if __name__ == "__main__":
   with app.app_context():
       db.create_all()  
   app.run(debug=True)