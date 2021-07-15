from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

#===========Flask Templates - Custom Filters===========
def power(x, y):
    return x**y

app.jinja_env.filters['powww'] = power

def reverse(str):
    return str[::-1]

app.jinja_env.filters['revvv'] = reverse
#===========Flask Templates - Custom Filters===========

@app.route("/")
def index():
    title = 'RICE' 
    return render_template("index.html", title = title)

@app.route("/Link1")
def Link1():
    title = 'RICE Link 1 test page' 
    return render_template("Link1.html", title = title, List_of_Builtin_Filters_1 = -3, List_of_Builtin_Filters_2 = 'webb')

@app.route("/Link2")
def Link2():
    title = 'RICE Link 2 HTML'
    return render_template("Link2.html", title = title)

@app.route("/Link3")
def Link3():
    title = 'RICE Link 3' 
    return render_template("Link3.html", title = title)

@app.route("/Link5")
def Link5():
    title = 'RICE Link 5' 
    return render_template("Link5.html", title = title)

@app.route("/Link6")
def Link6():
    title = 'RICE Link 6' 
    return render_template("Link6.html", title = title)

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)
