import requests
import win32com.client as wincom
import json


city=input("Enter the name of the city:")
# api url
url=f"http://api.weatherapi.com/v1/current.json?key=22affd327b4c47d2b18150548243101&q={city}"
r=requests.get(url)
# print(r.text)
weatherDic=json.loads(r.text)

speak = wincom.Dispatch("SAPI.SpVoice")

text = f"The current weather in the {city} is {weatherDic['current']['temp_c']} degrees"

print(f"The current weather in the {city} is {weatherDic['current']['temp_c']} degrees")
speak.Speak(text)

