from flask import Flask,render_template,request

api = "AIzaSyCaWXSq-kOenXykQ_Qu3cG6AHO-xlvGk4U"
palm.configure(api_key=api)
model = {"model": "models/chat-bison-001"}

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def DBS():
    return(render_template("DBS.html"))

if __name__ == "__main__":
    app.run()
