import qrcode
import uuid
import os


def Generate_QR(data):

    # check if qrcodes directory exists
    qr_dir = os.path.join("static", "qrcodes")
    os.makedirs(qr_dir, exist_ok=True)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # generate file path
    img_uid = uuid.uuid4().hex[:12]
    file_name = f"{img_uid}.png"
    file_path = os.path.join(qr_dir, file_name)

    img.save(file_path)
    return img_uid

