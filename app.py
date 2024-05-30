from flask import Flask, request, render_template, redirect
from flask_mail import Mail
from dotenv import load_dotenv
from os import environ

from mailManager import sendMail

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = environ["SECRET_KEY"]


#Configuras tus datos según tu servicio de SMTP, colocar estos valores en tu archivo ".env"
app.config['MAIL_SERVER'] = environ["MAIL_SERVER"]
app.config['MAIL_PORT'] = environ["MAIL_PORT"]
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = environ["MAIL_USERNAME"]
app.config['MAIL_PASSWORD'] = environ["MAIL_PASSWORD"]

#Inicias tu servicio de mails
mail = Mail(app)


@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")


@app.route("/sendMessage", methods=["POST"])
def sendMessage():
    if request.method == "POST":
        data = request.form

        try:
            archive = request.files["excel"]
        except:
            archive = None

        try:
            sendMail(mail, data, archive)
            print("ENVIA EL CORREO")
        except Exception as e:
            #En caso de fallo capturamos el error y lo mostramos en consola para ver los detaller
            print(e)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)