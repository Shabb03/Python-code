#!/usr/bin/env python3

import qrcode

image = qrcode.make('https://bit.ly/3jkjUo8')
image.save('QRcode.png')
image.show()