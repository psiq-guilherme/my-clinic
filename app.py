from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data analyst",
        "location": "Tangamandapio",
        "salary": 1234.56
    },
    {
        "id": 2,
        "title": "Data scientist",
        "location": "Tangamandapio",
        "salary": 1234.56
    },
    {
        "id": 3,
        "title": "Data enginner",
        "location": "Tangamandapio"
    },
    {
        "id": 4,
        "title": "Cleaner",
        "location": "Tangamandapio",
        "salary": 1000000.56
    },

]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)