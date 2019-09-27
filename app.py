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
def academic_info():
    return render_template("acedemic-info.html", data=data)


@app.route("/labor-experience")
def labor_xp():
    return render_template("labor-experience.html", data=data)




if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug)
