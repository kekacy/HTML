# -*- coding:utf-8 -*-  
#encoding:utf-8


from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
   #1.判断请求方式
   if request.method == 'POST':

      #2.获取请求参数
      username=request.form.get('username')
      password=request.form.get('password')
      password2=request.form.get('password2') 
      print (username)
      #3.验证是否填写相同
      if not all ([username,password,password2]):
         print ('参数不完整')
      elif password != password2:
         print ('密码不一致')
      else:
         return "success"
   return render_template('index.html')


if __name__ == '__main__':
   app.run()



mmmmm

远程版本

