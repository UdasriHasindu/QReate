from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from cleanup import clean_qr_codes, TIME
from generator import Generate_QR
from datetime import datetime
import threading
import time
import os

YEAR = datetime.now().year

app = Flask(__name__)

def schedule_cleanup(interval):
    while True:
        clean_qr_codes()
        time.sleep(interval)

@app.route("/")
def home():
    return render_template('index.html', year=YEAR)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@app.route("/generate", methods=['POST'])
def generate():

    info = request.form['qrdata']
    img_uid = Generate_QR(info)
    return redirect(url_for('view_qr', qr_id=img_uid))


@app.route('/view/<qr_id>')
def view_qr(qr_id):
    return render_template('view.html', qr_id=qr_id)


if __name__ == "__main__":
    cleanup_thread = threading.Thread(target=schedule_cleanup ,args=(TIME,), daemon=True)
    cleanup_thread.start()
    app.run(debug=True)
