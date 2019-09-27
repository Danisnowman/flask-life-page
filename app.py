#FLASK
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
import os,optparse
import yaml

# developer = os.getenv("DEVELOPER", "Me")
environment=os.getenv("ENVIRONMENT","development")

with open("info.yml", 'r') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


@app.route("/")
def home():
    return render_template("about.html", data=data)




@app.route("/academic-info")
def api_students():
    return render_template("acedemic-info.html", data=data)


# @app.route("/ages")
# def ages():
#     edades=[edad for estudiante,edad in alumnos.items()]
#     average=int(sum(edades)/len(edades))
#     return render_template("ages.html", alumnos=alumnos, average=average)


# @app.route("/students")
# def students():
#     return render_template("students.html", alumnos=alumnos)


# def search_student(student):
#     """
#     A function that searches in data source
#     """
#     result=[]
#     for name,age in alumnos.items():
#         if student.lower() in name.lower():
#             result.append(name)

#     print(f"Result {result}")
#     return result


# @app.route("/search",methods=["GET"])
# def search():
#     """
#     /search route, to search from an input form.
#     """
#     student_to_find=request.args.get("student", None)
#     print(f"A buscar: {student_to_find}")
#     student_list=search_student(student_to_find)
#     return render_template("search.html",student_list_result=student_list)

# @app.route("/")
# def home():
#     foo="bar"
#     return render_template("home.html", mivariable=foo ,developer=developer)

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug)
