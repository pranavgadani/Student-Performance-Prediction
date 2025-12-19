from flask import Flask, render_template, request 
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    values = [
        int(request.form["attendance"]),
        int(request.form["study"]),
        int(request.form["marks"]),
        int(request.form["assign"]),
        int(request.form["sleep"])
    ]

    prediction = model.predict([values])[0]
    return render_template("index.html", result=prediction)

if __name__ == "__main__":
    app.run(debug=True)
