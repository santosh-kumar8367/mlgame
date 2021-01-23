from flask import request,Flask,render_template
app=Flask(__name__)
@app.route("/")
def introduce():                                                         
    return render_template("index.html")

if(name=="__main__"):
    app.run(threaded=True,port=5000)