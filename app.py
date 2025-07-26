from flask import Flask, render_template

app = Flask(__name__)

projects_list = [
    {
        'title': 'Сайт по продаже газоблоков',
        'description': 'Flask, SQL, Bootstrap',
        'status': 'Завершён',
        'link': '#'
    },
    {
        'title': 'Приложение учёта часов работников',
        'description': 'В разработке',
        'status': 'В процессе',
        'link': '#'
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html", projects=projects_list)

if __name__ == "__main__":
    app.run(debug=True)
