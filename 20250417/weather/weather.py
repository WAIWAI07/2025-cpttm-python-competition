# This program fetch the weather data from the smg website
# Using untangle

import untangle

url = "https://xml.smg.gov.mo/c_actualweather.xml"
data = untangle.parse(url)

# Get the first temperature value

temp = data.ActualWeatherBrief