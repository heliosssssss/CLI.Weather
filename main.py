import requests
import json
import os 
from statistics import mean
from statistics import mode 

from pprint import pprint

base_url = 'https://api.open-meteo.com'

whitelist_cities = [
  "Portlaoise", 
  "Moutmellick", 
  "Portargliton"
]

class Utility():
  def getJSON(ctx):
    return ctx.json()

  def GetStatus(): 
    ctx = requests.get(base_url)
    print(ctx)

  def degToCompass(num):
    val=int((num/22.5)+.5)
    arr = [
      "North", 
      "North of North East", 
      "North East", 
      "East of North East",
      "East", 
      "East of South East",
      "South East", 
      "South of South East", 
      "South", 
      "South of South West", 
      "South West",
      "West of South West", 
      "West", 
      "West of North West", 
      "North West", 
      "North West of West"
    ]
    return arr[(val % 16)]

  def ReturnMenu():
    os.system('clear')
    MenuHandler.init()


class WeatherHandler:
  
  def GetTempature(apply_avg = None):

    ctx = requests.get(f"{base_url}/v1/forecast?latitude=53.03&longitude=-7.30&hourly=temperature_2m")
    ctxJSON = Utility.getJSON(ctx)
    
    if apply_avg == False:
     return ctxJSON
      
    if apply_avg == True: 
      before_average = ctxJSON["hourly"]["temperature_2m"]
      average_temp = round(mean(before_average))

      return str(average_temp)

  def GetWindspeeds(apply_avg = None):

    ctx = requests.get(f"{base_url}/v1/forecast?latitude=53.03&longitude=-7.30&hourly=windspeed_10m&forecast_days=1")
    ctxJSON = Utility.getJSON(ctx)

    if apply_avg == False: 
      return ctxJSON

    if apply_avg == True: 
      before_average = ctxJSON["hourly"]["windspeed_10m"]
      average_temp = round(mean(before_average))

      return str(average_temp)

  def GetWindDirection(apply_avg = None):
    
    ctx = requests.get(f"{base_url}/v1/forecast?latitude=53.03&longitude=-7.30&hourly=winddirection_10m&forecast_days=1")
    ctxJSON = Utility.getJSON(ctx)

    if apply_avg == False: 
      return ctxJSON

    if apply_avg == True: 
      before_average = ctxJSON["hourly"]["winddirection_10m"]
      average_tenp = round(mean(before_average))

      return str(average_tenp)

  def GetRainfall(apply_avg = None): 
    ctx = requests.get(f"{base_url}/v1/forecast?latitude=53.03&longitude=-7.30&hourly=rain&forecast_days=1")
    ctxJSON = Utility.getJSON(ctx)

    if apply_avg == False:
      return ctxJSON
    if apply_avg == True:
      return ctxJSON["hourly"]["rain"]

  def GetVisibility(apply_avg = None):
    ctx = requests.get(f"{base_url}/v1/forecast?latitude=53.03&longitude=-7.30&hourly=visibility&forecast_days=1")
    ctxJSON = Utility.getJSON(ctx)

    if apply_avg == False:
      return ctxJSON
    if apply_avg == True:
      return ctxJSON["hourly"]["visibility"]

class MenuHandler: 
  def init():
    menu = """

  Real Time Weather Information of Portlaoise 
  Information is sourced from a realtime API

  Made by Adam 

  [1] - Temperature 
  [2] - Windspeeds
  [3] - Wind Direction 
  [4] - Rainfall 
  [5] - Visibility
  
  """

    print(menu)

    data_needed = input("Please choose what data you would to gather (1-5): ")

    if data_needed == str(1): 
      os.system('clear')
      data = WeatherHandler.GetTempature(apply_avg=True)

      print(f"The average temperature in Portlaoise today: {data} degrees")

      state = input("Would you like to return to Menu? (y/n): ")
      if state == "y": 
        Utility.ReturnMenu()
      if state == "n": 
        return

    if data_needed == str(2): 
      os.system("clear")
      data = WeatherHandler.GetWindspeeds(apply_avg=True)

      print(f"The average windspeeds in Portlaoise today: {data} km/h")

      state = input("Would you like to return to Menu? (y/n): ")
      if state == "y": 
        Utility.ReturnMenu()
      if state == "n": 
        return

    if data_needed == str(3):
      os.system('clear')
      data = WeatherHandler.GetWindDirection(apply_avg=True)

      print(f"The wind direction in Portlaoise today: {Utility.degToCompass(float(data))} ({data} degrees)")

      state = input("Would you like to return to Menu? (y/n): ")
      if state == "y": 
        Utility.ReturnMenu()
      if state == "n": 
        return

    if data_needed == str(4): 
      os.system('clear')
      data = WeatherHandler.GetRainfall(apply_avg=True)
      common = mode(data)

      if common == 0.0: 
        print("There is no current rainfall in portlaoise")
        state = input("Would you like to return to Menu? (y/n): ")
        if state == "y": 
          Utility.ReturnMenu()
        if state == "n": 
           return
        return
      if common <= 0.4: 
        print("There is slight rainfall in portlaoise")
        state = input("Would you like to return to Menu? (y/n): ")
        if state == "y": 
          Utility.ReturnMenu()
        if state == "n": 
           return
        return        
      if common == 0.5: 
        print("There is rainfall in portlaoise")
        return
        state = input("Would you like to return to Menu? (y/n): ")
        if state == "y": 
          Utility.ReturnMenu()
        if state == "n": 
           return
        return
      if common >= 0.6: 
        print("There is alot of rainfall in portlaoise")
        state = input("Would you like to return to Menu? (y/n): ")
        if state == "y": 
          Utility.ReturnMenu()
        if state == "n": 
           return
        return
        state = input("Would you like to return to Menu? (y/n): ")
        if state == "y": 
          Utility.ReturnMenu()
        if state == "n": 
           return
        return
      if common >= 1.5: 
        print("There is severe rainfall in portlaosie")
        state = input("Would you like to return to Menu? (y/n): ")
        if state == "y": 
          Utility.ReturnMenu()
        if state == "n": 
           return
        return


    if data_needed == str(5):
      os.system("clear")
      data = WeatherHandler.GetVisibility(apply_avg=True)
      common = mode(data) 

      print(f"The average view distance is {common} meters")

      state = input("Would you like to return to Menu? (y/n): ")
      if state == "y": 
        Utility.ReturnMenu()
      if state == "n": 
        return

class LoadingScreen: 
  def DisplayLoader():

    print("Weather Information - Today")
    
    print("Please wait for the API to load")

    print("")

MenuHandler.init()

#LoadingScreen.DisplayLoader()
