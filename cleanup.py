import os
import time

QR_FOLDER = "static/qrcodes"
TIME = 60   # for 1hr

def clean_qr_codes():
    now = time.time()
    deleted = 0

    for filename in os.listdir(QR_FOLDER):
        filepath = os.path.join(QR_FOLDER, filename)

        if os.path.isfile(filepath):

            file_age = now - os.path.getmtime(filepath)
            if file_age > TIME:
                os.remove(filepath)
                deleted += 1

    print(f"Cleanup complete. {deleted} old QR code(s) removed.")


