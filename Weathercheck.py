import requests

while True:
	
	print()
	user_input = input('What is city name for which to check temperature: ')    # takes input from user for a city value
	response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+user_input+'&APPID=eba1d2a48d8ef5168c95997d840b2fd2') # connectcs to openweathermap.org API to get data

	print()
	print ('Establishing Connection to API.....')
	print()


	if response.status_code == 200:
		print(' Connection Sucesfull\n')
		 
		jason_data = response.json()
		
		jason_temp = jason_data['main']['temp'] # extraction of temperature from Json

		
		celcius_temp = jason_temp - 273
		print("Current temperature in "+user_input+" is: " +str(celcius_temp)[:3]+" °C\n")
	else:
		print(' Check Connection, unable to connnect')
