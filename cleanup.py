import os
import time

QR_FOLDER = "static/qrcodes"
TIME = 3600   # for 1hr

def clean_qr_codes():
    now = time.time()


    for filename in os.listdir(QR_FOLDER):
        filepath = os.path.join(QR_FOLDER, filename)

        if os.path.isfile(filepath):

            file_age = now - os.path.getmtime(filepath)
            if file_age > TIME:
                os.remove(filepath)
                print(f"Cleanup complete. {filepath} old QR code(s) removed.")


