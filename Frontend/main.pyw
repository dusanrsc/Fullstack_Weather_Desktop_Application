# importing modules
import tkinter
import requests

# importing sub-modules
from tkinter import *
from time import strftime
from PIL import Image, ImageTk

# IPv4 address
ipv4_address = "http://localhost:8000/"

# fetching API from localhosted API Endpoints
response = requests.get(ipv4_address)
data = response.json()

# simple message for fetching data
data_successfully_fetched_message = f"Data Successfully Fetched From: '{ipv4_address}'"
no_fetched_data_message = f"Server From: '{ipv4_address}' NOT RESPONDING!"

# variable section
# fetched item id/pk number
pk = 0

# custom function section
# next city
def next_city():
	# global variable section
	global pk

	# primary key +1
	pk += 1

	# error primary key catcher
	# primary key / pk is less then cities id
	if pk > (len(data) -1):
		pk = (len(data) -1)

# previous city
def previous_city():
	# global variable section
	global pk

	# primary key -1
	pk -= 1

	# error primary key catcher
	# primary key / pk is greather then cities id
	if pk < (len(data) - len(data)):
		pk = (len(data) - len(data))


# global update function
# this function update all data by button press according to proper id/pk (primary key)
def global_update():

	# update city by primary key
	def city_update():
		# configuring data
		city_name.config(text=f" {data[pk]["name"]} ")

		# update data after
		city_name.after(50, city_update)

	# update weather condition image
	def weather_condition_image_update():

		# weather condition image
		# if condition of city is sunny render sun image 
		if data[pk]["cond"] == "Sunny":
			condition_image.config(image=sun_photo)
			condition_temperature.config(fg=DEFAULT_FONT_COLOR)

		# else if condition of city is rain render rain image 
		elif data[pk]["cond"] == "Rain":
			condition_image.config(image=rain_photo)
			condition_temperature.config(fg=DEFAULT_FONT_COLOR)

		# else condition
		else:
			condition_temperature.config(fg=DEFAULT_FONT_COLOR)

		# update data after
		condition_temperature.after(50, weather_condition_image_update)

	# update condition temperature data
	def condition_temperature_update():

		# configuring data
		condition_temperature.config(text=f" {data[pk]["temp"]} ")

		# update data after
		condition_temperature.after(50, condition_temperature_update)

	# update wind data
	def wind_update():

		# wind condition
		# if is there a wind
		if data[pk]["wind"]:
			wind_label.config(text=" WIND ")

		# if there isn't a wind
		else:
			wind_label.config(text=" CALM ")

		# update data after
		condition_temperature.after(50, wind_update)

	# calling all inner update functions section
	city_update()
	weather_condition_image_update()
	condition_temperature_update()
	wind_update()

# specific/thunder variable (metadata)
__version__ = "v1.0.0"
__updated__ = "13.10.2024"
__tag__ = "@dusanrsc"
__by__ = "Dusan Rosic"

# CONSTANT section
TITLE = "Fullstack Weather Desktop Application"

ROOT_WIDTH = "800"
ROOT_HEIGHT = "600"
ROOT_SIZE = f"{ROOT_WIDTH}x{ROOT_HEIGHT}"

# image path section
BACKGROUND_IMAGE_PATH = "assets/images/background.jpg"
SUN_IMAGE_PATH = "assets/images/sun.png"
RAIN_IMAGE_PATH = "assets/images/cloud_and_rain.png"

# hexadecimal color tuples
RED = "#FF0000"
GREEN = "#00FF00"
BLUE = "#0000FF"

BLACK = "#000000"
WHITE = "#FFFFFF"

ORANGE = "#FFA500"
DEFAULT_FONT_COLOR = "#5E8BC0"

# root window settings
root = Tk()
root.title(f"{TITLE} | {__version__} | by: {__tag__}")
root.config(bg=WHITE)
root.geometry(ROOT_SIZE)
root.resizable(False, False)

# initialization of images
# background image
background_img = Image.open(BACKGROUND_IMAGE_PATH)
background_photo = ImageTk.PhotoImage(background_img)

# sun image
sun_img = Image.open(SUN_IMAGE_PATH)
sun_photo = ImageTk.PhotoImage(sun_img)

# rain image
rain_img = Image.open(RAIN_IMAGE_PATH)
rain_photo = ImageTk.PhotoImage(rain_img)

# backgound image label
background_label = Label(root, image=background_photo)
background_label.place(x=-150, y=-190)

# data fatching message label
message_label = Label(root, text=None, bg=None, fg=None)
message_label.place(x=0, y=0)

# city name
city_name = Label(root, text=f" {data[pk]["name"]} ", font=("Arial Bold", 30), fg=DEFAULT_FONT_COLOR)
city_name.place(x=310, y=150)

# current time
current_time_label = Label(root, text=strftime(" %d.%m.%Y "), font=("Arial Bold", 12), fg=DEFAULT_FONT_COLOR)
current_time_label.place(x=410, y=195)

# condition image
condition_image = Label(root, image=None)
condition_image.place(x=350, y=242)

# condition temperature
condition_temperature = Label(root, text=f" {data[pk]["temp"]} ", font=("Arial Bold", 30), fg=DEFAULT_FONT_COLOR)
condition_temperature.place(x=360, y=350)

# condition temperature metric
condition_temperature_metric = Label(root, text="°C", font=("Arial Bold", 15), fg=DEFAULT_FONT_COLOR)
condition_temperature_metric.place(x=420, y=353)

# wind label
wind_label = Label(root, text=None, font=("Arial Bold", 25), fg=DEFAULT_FONT_COLOR)
wind_label.place(x=343, y=420)

# change current city to previous
previous_city_button = Button(root, text=" < ", font=("Arial Bold", 15), fg=DEFAULT_FONT_COLOR, command=lambda: previous_city())
previous_city_button.place(x=140, y=155)

# change current city to next
next_city_button = Button(root, text=" > ",  font=("Arial Bold", 15), fg=DEFAULT_FONT_COLOR, command=lambda: next_city())
next_city_button.place(x=625, y=155)

# calling function section
global_update()

# conditions section
# if there is any data (data fetched successfully)
if data is not None:
	message_label.config(text=data_successfully_fetched_message, bg=BLACK, fg=GREEN)
	message_label.after(15000, message_label.destroy)

# starting program (mainloop)
root.mainloop()
