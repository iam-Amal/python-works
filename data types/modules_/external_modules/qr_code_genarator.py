import pyqrcode
from pyqrcode import QRCode
s ="Achi pattye...nannayikoode..?"


url = pyqrcode.create(s)
url.svg("testqrcode.svg",scale=8)