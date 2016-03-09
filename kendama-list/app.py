from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("base.html") 


@app.route("/kendamas")
def kendama_list():
    
    return "Hey, you currently have no kendamas"


if __name__ == "__main__":
    app.run(debug=True)

