"""Code	chi_desc	por_desc	eng_desc	Usage
01	天晴	Pouco nublado	Fine	Day
a1	天晴	Pouco nublado	Fine	Night
02	間晴	Muito nublado com abertas	Sunny periods	Day
a2	間晴	Muito nublado com abertas	Sunny periods	Night
03	多雲	Muito nublado	Cloudy	 
04	密雲	Encoberto	Overcast	 
05	浮塵	Poeira	Dust	 
06	霧	Nevoeiro	Fog	 
07	煙霞	Bruma seca	Haze	 
08	薄霧	Neblina	Mist	 
09	煙幕	Fumo	Smoke	 
10	毛毛雨	Chuvisco	Drizzle	 
11	冰雹	Saraiva	Hail	 
12	雨	Chuva	Rain	 
13	大雨	Chuva intensa	Heavy rain	 
14	雪	Neve	Snow	 
15	大雪	Neve intensa	Heavy snow	 
16	驟雨	Aguaceiros	Showers	 
17	大驟雨	Aguaceiros fortes	Heavy showers	 
18	雷雨	Aguaceiros e trovoadas	Thundershowers	 
19	塵暴	Tempestade de poeira	Duststorm	 
20	大塵暴	Tempestade forte de poeira	Severe duststorm	 
21	乾燥	Seca	Dry	 
22	沙暴	Tempestade de areia	Sandstorm	 
23	大沙暴	Tempestade forte de areia	Severe sandstorm	 
24	狂風雷暴	Vento intenso com trovoada	Squall thunderstorm	 
25	雷暴	Trovoadas	Thunderstorms	 
26	潮濕	Hmido	Wet	 
27	大風	Ventos fortes	Windy	 
28	雨	Chuva	Rain	Day
c8	雨	Chuva	Rain	Night
29	驟雨	Aguaceiros	Showers	Day
c9	驟雨	Aguaceiros	Showers	Night
30	水龍捲	Tromba maritima	Funnel	 """

# Format the weather status code according to the table above

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