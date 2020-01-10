'''
	Riley Knybel
	Program 1: Zeller's Congruence Weekday Calculator
	CSIS1101
	16 December 2019 (a Monday)
'''
import PySimpleGUI as sg
import math

#Selector lists - the Combo box and Spinner UI elements of PySimpleGUI take lists as acceptable values for the inputs.
#Creating these here makes the layout 2D List easier to read.

#holds the months for the month combo box
monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#creates a list containing numbers 1-31 for the days of the month spin-box
dayList = [i for i in range(1, 32)]

#creates a list containing numbers from 0-9999 for the year spin-box
yearList = [i for i in range(0, 9999)]

sg.change_look_and_feel('Dark Blue 3') #set a nice theme so the GUI isn't boring dull and gray

layout = [	[sg.Combo(monthList, default_value='January', font='Courier` 16'), sg.Spin(dayList, initial_value=1, size=(2,1), font='Courier` 16'), sg.Spin(yearList, initial_value=2019, size=(4,1), font='Courier` 16'), sg.Button('Calculate', font='Courier` 16')],
			[sg.Text('Hit "Calculate" to get the weekday :)', key='infoText', font='Courier` 16')]]

def ZCong(month, day, year): #function to calculate the weekday

	daysOfWeek = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
	yearOfCentury = year % 100
	zBasedCentury = year // 100 #the algorithm won't work with a float, so truncate the decimal points and convert to int

	returnString = month + ' ' + str(day) + ' ' + str(year) + ' is a '

	#convert month string to the appropriate integer for the algorithm
	if month is "March":
		if day > 31:
			return "Invalid date, please try again."
		month = 3
	elif month is "April":
		if day > 30:
			return "Invalid date, please try again."
		month = 4
	elif month is "May":
		if day > 31:
			return "Invalid date, please try again."
		month = 5
	elif month is "June":
		if day > 30:
			return "Invalid date, please try again."
		month = 6
	elif month is "July":
		if day > 31:
			return "Invalid date, please try again."
		month = 7
	elif month is "August":
		if day > 31:
			return "Invalid date, please try again."
		month = 8
	elif month is "September":
		if day > 30:
			return "Invalid date, please try again."
		month = 9
	elif month is "October":
		if day > 31:
			return "Invalid date, please try again."
		month = 10
	elif month is "November":
		if day > 30:
			return "Invalid date, please try again."
		month = 11
	elif month is "December":
		if day > 31:
			return "Invalid date, please try again."
		month = 12
	elif month is "January":
		if day > 31:
			return "Invalid date, please try again."
		month = 13
		yearOfCentury -= 1
	elif month is "February":
		if day > 29:
			return "Invalid date, please try again."
		month = 14
		yearOfCentury -= 1

	#Fixed my bug with info from this site https://www.geeksforgeeks.org/zellers-congruence-find-day-date/
	#The actual Zeller's Congruence algorithm - The star of the show!!

	weekday = (day + (13*(month+1)//5) + yearOfCentury + (yearOfCentury//4) + (zBasedCentury//4) - 2*zBasedCentury) % 7

	returnString += daysOfWeek[weekday] + '.'

	print("{} {}/{}/{}".format(weekday, month, day, year))

	return returnString

#Now that everything's defined, let's actually do things.

window = sg.Window('Day of Week Calculator', layout) #opens the window and creates the GUI elements in the order defined in layout 2D List

while True: #event loop - responds if the user clicks Calculate or the close button

	event, values = window.Read() #Get the values of all input elements in the GUI, values is a list of the inputs and event is the button that was clicked

	if event is None: #this occurs when the user clicks the close button in the title bar
		break

	if event is "Calculate": #this occurs when the user clicks "Calculate"
		window.Element('infoText').Update(ZCong(values[0], values[1], values[2]))

window.close() #close the window when the event loop is broken via clicking the close button
