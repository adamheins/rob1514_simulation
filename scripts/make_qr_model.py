#!/usr/bin/env python3
import sys

import qrcode


def make_qr_code(word):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(word)
    qr.make(fit=True)
    img = qr.make_image()
    name = word + '.png'
    img.save(word + '.png')
    print('Created QR code image: {}'.format(name))
    return name

def main():
    if len(sys.argv) < 2:
        print('Argument required.')
        return 1

    word = sys.argv[1]

    img_name = make_qr_code(word)
    model_name = word + '.dae'

    # modify the collada data file to take the texture from the newly generated
    # QR code image
    with open('../models/qr.dae') as f:
        data = f.read()
    data = data.replace('Image.png', img_name)
    with open(model_name, 'w') as f:
        f.write(data)
    print('Created QR code model: {}'.format(model_name))


if __name__ == '__main__':
    main()
