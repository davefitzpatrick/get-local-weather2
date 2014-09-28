import json
import requests
import time

weather_url = "http://api.openweathermap.org/data/2.5/weather?q="
#f = open('weatherdata.txt', 'a')

def get_weather(city):
	url = weather_url + city
	
	for ite in range(0,20):
		print ite

		f = open('weatherdata.txt', 'a')

		response = requests.get(url)
		if response.status_code == 200:
			print json.dumps(response.json(), indent=4)
			json_encode = json.dumps(response.json())
			my_data_structure = json.loads(json_encode)

        #print my_data_structure["dt"], my_data_structure["main"]["temp"]
        #print my_data_structure["weather"][0]["main"]
			this_moment_tempK = my_data_structure["main"]["temp"]
			this_moment_temp = 1.8 * (this_moment_tempK - 273.15) + 32
			this_moment_timeEPOCH = my_data_structure["dt"]
			this_moment_time = time.gmtime(this_moment_timeEPOCH)
#    	    print str(this_moment_time) + ", " + '%4.1f' % this_moment_temp + \
#    	        "F, " + my_data_structure["weather"][0]["main"]
			tempd = 0
			this_moment_weatherID = my_data_structure["weather"][0]["id"]

    	    #write out current date, time; then GMT month,day,hour,min of reading;
    	    #temp in Fahrenheit; and WeatherCode

			write_string = (time.strftime("%x") + " "
				+ time.strftime("%X") + " "
				+ str(this_moment_time[1]) + " "
				+ str(this_moment_time[2]) + " " + str(this_moment_time[3])
				+ " " + str(this_moment_time[4]) + " "
				+ str(this_moment_timeEPOCH) + ", "
				+ str(this_moment_temp) + ", " + str(this_moment_weatherID))

			f.write(write_string)
			f.write('\n')
			time.sleep(300)
			f.close()
			time.sleep(300)
		else:
			print "Could not fetch the weather for some reason."

#	f.close()
    	
if __name__ == '__main__':
    get_weather("Washington,D.C.")
