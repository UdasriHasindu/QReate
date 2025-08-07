from flask import Flask, render_template, request, redirect, url_for
from generator import Generate_QR
from datetime import datetime

YEAR = datetime.now().year


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', year=YEAR)


@app.route("/generate", methods=['POST'])
def generate():

    info = request.form['qrdata']
    img_uid = Generate_QR(info)
    return redirect(url_for('view_qr', qr_id=img_uid))


@app.route('/view/<qr_id>')
def view_qr(qr_id):
    return render_template('view.html', qr_id=qr_id)


if __name__ == "__main__":
    app.run(debug=True)
