

from flask import Flask,render_template,request
'''
It creates an instance of the Flask class,
which will be your WSGI(Web Server Gateway Interface) application.
'''
# WSGI Application #
app=Flask(__name__)

@app.route("/")
def welcome():
    return"<html><h1>Welcome to this page</h1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template("form.html")

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template("form.html") 

# Variable Rule
@app.route("/sucess/<int:score>")
def sucess(score):
    result=""
    if score>50:
        result="PASS"
    else:
        result="FAIL"
    # print("The marks you got is "+ str(score)) 
    return render_template("result.html", results=result)

@app.route("/sucessres/<int:score>")
def sucessres(score):
    result=""
    if score>50:
        result="PASS"
    else:
        result="FAIL"
    exp={"score":score, "result":result}
    return render_template("result1.html", results=exp)

# if condition
@app.route("/sucessif/<int:score>")
def sucessif(score):
    return render_template("result2.html", results=score)
    
# Jinja 2 template engine #
'''
{{}}     expression to print output in html
{%...%}  for conditions and loops
{#...#}  for comments 
'''




if __name__=="__main__":
    app.run(debug=True)