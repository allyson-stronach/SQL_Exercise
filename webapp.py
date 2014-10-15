import hackbright_app

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def get_github():
    return render_template("get_github.html")

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    row_of_projects_and_grades = hackbright_app.get_grades_by_github(student_github)
    html = render_template("student_info.html", projects_and_grades=row_of_projects_and_grades, student_github=student_github)
    return html

if __name__ == "__main__":
    app.run(debug=True)
