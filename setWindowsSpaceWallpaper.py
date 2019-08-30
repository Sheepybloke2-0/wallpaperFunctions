import requests
import urllib
from datetime import date
import ctypes 
import os

from PIL import Image

today = date.today()

SPI_SETDESKTOPWALLPAPER=20

# TODO maybe have this be the day of the week so that only 7 are stored?
image_name = today.strftime("%m-%d-%Y") + "_space_image.jpg"

path_to_file = os.path.join( os.getcwd(), image_name)

# TODO get yesterday's date and delete the old image

# nasa_api_key = aezGeKFhtJpOMPO82IhRPnJGQXvTeKJIxZguJ8Ct
request = requests.get('https://api.nasa.gov/planetary/apod?api_key=< Add YOUR KEY HERE >')

if request.status_code != 200:
    print("Error recieving the image!")

# Find the HD link
apod_returned_json = request.json()

urllib.request.urlretrieve(apod_returned_json["hdurl"], image_name)

ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER, 0, path_to_file, 0)