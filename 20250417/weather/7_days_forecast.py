# This program fetch the weather data from the smg website
# Using untangle

# url: https://xml.smg.gov.mo/c_7daysforecast.xml

# weather_status_code url: https://xml.smg.gov.mo/#WeatherStatus

import untangle

data = untangle.parse("https://xml.smg.gov.mo/c_7daysforecast.xml")

# Get the weather status code

weather_status_codes = {
    "01": "天晴",
    "a1": "天晴",
    "02": "間晴",
    "a2": "間晴",
    "03": "多雲",
    "04": "密雲",
    "05": "浮塵",
    "06": "霧",
    "07": "煙霞",
    "08": "薄霧",
    "09": "煙幕",
    "10": "毛毛雨",
    "11": "冰雹",
    "12": "雨",
    "13": "大雨",
    "14": "雪",
    "15": "大雪",
    "16": "驟雨",
    "17": "大驟雨",
    "18": "雷雨",
    "19": "塵暴",
    "20": "大塵暴",
    "21": "乾燥",
    "22": "沙暴",
    "23": "大沙暴",
    "24": "狂風雷暴",
    "25": "雷暴",
    "26": "潮濕",
    "27": "大風",
    "28": "雨",
    "c8": "雨",
    "29": "驟雨",
    "c9": "驟雨",
    "30": "水龍捲"
}

# Get the weather forecasts

weather_forecasts: list[untangle.Element] = data.SevenDaysForecast.Custom.WeatherForecast

for weather_forecast in weather_forecasts:
    date = weather_forecast.ValidFor.cdata
    temperatures: list[untangle.Element] = weather_forecast.Temperature

    for temperature in temperatures:
        if temperature.Type.cdata == "1":
            min_temp = temperature.Value.cdata
        elif temperature.Type.cdata == "2":
            max_temp = temperature.Value.cdata

    weather_status = weather_status_codes[weather_forecast.WeatherStatus.cdata]
    weather_desc = weather_forecast.WeatherDescription.cdata

    print(f"{date}: {min_temp} ~ {max_temp}°C {weather_status}，{weather_desc}")