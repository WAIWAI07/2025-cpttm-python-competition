# This program fetch the weather data from the smg website
# Using untangle

import untangle

url = "https://xml.smg.gov.mo/c_actual_brief.xml"
data = untangle.parse(url)

# Get the first temperature value

temperatures: list[untangle.Element] = data.ActualWeatherBrief.Custom.Temperature

for temperature in temperatures:
    print(temperature.Value.cdata)