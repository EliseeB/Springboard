from flask import Flask, render_template, request

app = Flask (__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form')
def formx():
    return render_template("form.html")

@app.route('/story', methods=["GET", "POST"])
def story():
    noum = request.form.get('noum')
    verb = request.form.get('verb')
    location = request.form.get('location')
    adjective = request.form.get('adjective')
    plural_noum = request.form.get('plural_noum')

    if noum:
        return render_template("story.html", noum=noum, adjective=adjective, verb=verb, location=location, plural_noum=plural_noum)
    else:
        return render_template("error.html")