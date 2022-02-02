from flask import Flask, redirect, url_for, render_template, request

# Flask Server initialisieren
app = Flask(__name__)
# Route für die Hauptseite
@app.route('/')
def index():
    return render_template("index.html")



if __name__ == '__main__':
    # starte Flask-Server
    app.run(host='0.0.0.0', port=4444)