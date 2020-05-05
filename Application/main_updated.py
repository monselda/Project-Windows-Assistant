'''
FINAL PROJECT 
GROUP5
B3
'''
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import datetime
import os
import time
import webbrowser
import requests
import wolframalpha
import inspect
import pyttsx3  #pip install pyttsx3==2.71
import speech_recognition as sr
from API import app_id, weather_api
import pytz
from main_API import host, user, passwd, database, weather_api, app_id
import mysql.connector


try:
    #mysql connector and cursor
    mydb = mysql.connector.connect(
        host=host, 
        user=user, 
        password=passwd, 
        database=database,
        # Important!!!
        auth_plugin='mysql_native_password'
        # Important!!!
        )
    mycursor = mydb.cursor(buffered=True)
except:
    print("Please add your credentials to main_mysql_cred.")


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october", "november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]


#setting text to speech engine and voice rate property
engine = pyttsx3.init("sapi5")
engine.setProperty('rate', 150)


#brave path
brave_path = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/Brave.exe %s --incognito'
brave_path_normal = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/Brave.exe %s'


#function for synthesizer
def say(text):

    print("Assistant: " + text)

    engine.say(text)
    engine.runAndWait()


#getting input from microphone
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        query = ""
    try:
        query = r.recognize_google(audio, language='en')
        print("User: " + query)
    except sr.UnknownValueError:
        print("Sorry, I did not get that.")
    return query.lower()


#choose voice for windows assistant
def choose_voice(said):
    ASSISTANT = {
        'hey david': ['david', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'],
        'hey ashi': ['ashi', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0']
    }
    if "david" in said:
        choice = ASSISTANT['hey david'][1]
        name = ASSISTANT['hey david'][0]
        engine.setProperty('voice', choice)
        say("hello, sir. I am " + name + ", how may i help you")

    elif "ashi" in said:
        choice = ASSISTANT['hey ashi'][1]
        name = ASSISTANT['hey ashi'][0]
        engine.setProperty('voice', choice)
        say("hello, sir. I am " + name + ", how may i help you")


#function for greeting the user once the program starts
def greet():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        say("good morning")
    elif 12 <= hour < 18:
        say("good afternoon")
    else:
        say("good evening")


#function for closing the program
def quit(said):
    if "goodbye" in said:
        say("okay, goodbye.")
        exit()


#function for controlling laptop's brightness, monitor, volume.
def nircmd(said):
    try:
        if 'increase volume' in said or 'volume up' in said:
            f = open("C:/nircmd.exe")
            f.close()
            os.system("C:/nircmd.exe changesysvolume 5000")
            say("volume increased")

        if 'decrease volume' in said or 'volume down' in said:
            f = open("C:/nircmd.exe")
            f.close()
            os.system("C:/nircmd.exe changesysvolume -5000")
            say("volume decreased")

        if 'max volume' in said:
            f = open("C:/nircmd.exe")
            f.close()
            os.system("C:/nircmd.exe setsysvolume 65535")
            say("max volume") 

        if 'mute' in said:
            f = open("C:/nircmd.exe")
            f.close()
            os.system("C:/nircmd.exe mutesysvolume 1")

        if 'unmute' in said:
            f = open("C:/nircmd.exe")
            f.close()
            os.system("C:/nircmd.exe mutesysvolume 0")
            say("volume unmuted")

        if 'stand by' in said:
            f = open("C:/nircmd.exe")
            f.close()
            os.system("C:/nircmd.exe standby")
    except:
        say("Please install nircmd to use this command")




#function to paste and read something in notepad
def notepad(said):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'notes', 'notes.txt')
    if "paste in notepad" in said:
        say("i am ready")
        text = get_audio()
        file = open(my_file, "w+") 
        file.write(text)
        file.close()
        say("done")
    
    if "show text" in said:
        say("opening notepad")
        os.startfile(my_file)
        with open(my_file,"r") as f:
            data = f.readlines()
            say(str(data))


#function to get google calendar account
def authenticate_user():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service

#fuction to get reminders
def get_reminder(day, service, said):
    if "what do i have" in said or "reminders" in said or "schedule" in said:
        # Call the Calendar API
        date = datetime.datetime.combine(day, datetime.datetime.min.time())
        end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
        utc = pytz.UTC
        date = date.astimezone(utc)
        end_date = end_date.astimezone(utc)

        events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(), timeMax=end_date.isoformat(),
                                            singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            say('No upcoming events found.')
        else:
            say(f"You have {len(events)} events on this day.")
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])
                start_time = str(start.split("T")[1].split("+")[0])
                if int(start_time.split(":")[0]) < 12:
                    start_time = start_time + "am"
                else:
                    start_time = str(int(start_time.split(":")[0])-12)
                    start_time = start_time + "pm"

                say(event["summary"] + " at " + start_time)

#function to get date from reminders
def get_date(said):
    said = said.lower()
    today = datetime.date.today()

    if said.count("today") > 0:
        return today

    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in said.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

    if month < today.month and month != -1:  # if the month mentioned is before the current month set the year to the next
        year = year+1

    # This is slighlty different from the video but the correct version
    if month == -1 and day != -1:  # if we didn't find a month, but we have a day
        if day < today.day:
            month = today.month + 1
        else:
            month = today.month

    # if we only found a dta of the week
    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if said.count("next") >= 1:
                dif += 7

        return today + datetime.timedelta(dif)

    if day != -1:  # FIXED FROM VIDEO
        return datetime.date(month=month, day=day, year=year)



#function to shutdown and restart computer
def snr(said):
    if "shutdown computer" in said:
        say("computer will shutdown in 60 seconds")
        os.system("shutdown /s /t 60")

    if "restart computer" in said:
        say("computer will restart in 60 seconds")
        os.system("shutdown /r /t 60")

    if "cancel" in said:
        say("scheduled shutdown or restart has been cancelled")
        os.system("shutdown /a")


#function to check the weather
def weather_check(said):
    if "weather" in said:
        try:
            search = said.replace("check the weather in ", "").replace("can you check the weather in ", "").replace(
                "what's the weather in ", "").replace("check weather in ", "").replace("weather in ", "")
            
            url = 'https://api.openweathermap.org/data/2.5/weather?q=' + search + '&appid=' + weather_api #your API
        
            if weather_api != '':
                loc_url = 'https://openweathermap.org/find?q=' + search
                webbrowser.get(brave_path).open_new(loc_url)
            else:
                pass
            try:
                json_data = requests.get(url).json()
                weather_type = json_data['weather'][0]['main']
            
                if weather_type == "Clouds":
                    weather_type = "cloudy"
                elif weather_type == "Haze":
                    weather_type = "hazy"
                elif weather_type == "Snow":
                    weather_type = "snowy"
                elif weather_type == "Rain":
                    weather_type = "rainy"
                temp = json_data['main']['temp']
                temp = round(temp - 273.15)
                temp = str(temp) + " degree celcius"
                say(
                    "the weather in " + search + " is " + weather_type + ". " + "And the temperature is " + temp)
            except:
                say("Error! weather api is missing")
        except sr.UnknownValueError:
            say("Sorry, I can't understand you. ")


#function to solve math problems
def wolfram(said):
    if "wolfram" in said:
        said = said.replace("wolfram ", "").replace("wolfram, ", "")
        try:
            try:
                client = wolframalpha.Client(app_id) #your own app ID
                res = client.query(said)
            except:
                say("Wolfram app id is missing")
        
            output = next(res.results).text
            print("Assistant: " + str(output))
            say("The answer is " + str(output))
        except:
            if app_id != '':
                say("Sorry, I dont have an answer for that")
            else:
                pass


#function to ask AI
def do_commands(said):
    if "what time is it" in said:
        say(time.strftime("%I%M:%p"))

    if "date" in said:
        say(datetime.datetime.now().strftime("%m-%d-%Y"))

    if 'today' in said:
        say("today is " + datetime.datetime.now().strftime("%A"))

    if 'what can you do' in said:
        say("just say the following commands: ")
        print("Assistant: Just say the following commands:")
        print("\t1. choose / change to: [david, ashi]")
        print("\t2. who are you")
        print("\t3. what is today / what day is today / what's the date today")
        print("\t4. shutdown computer/ restart computer. CANCEL to cancel.")
        print("\t5. search in google / youtube")
        print("\t6. find location of / find the location of")
        print("\t7. open (chrome,  brave, garena, word, powerpoint, notepad, calculator)")
        print("\t8. check the weather in / can you check the weather in / what's the weather in / check weather in / weather in")
        print("\t9. wolfram, 'query' ")
        print("\t10. increase volume / volume up")
        print("\t11. decrease volume / volume down")
        print("\t12. max volume")
        print("\t13. mute")
        print("\t14. ummute")
        print("\t15. standby")
        print("\t16. paste in notepad / show text")
        print("\t17. what do i have .. / reminders .. / schedule ..")
        print("\t18. add command ")
        print("\t19. close {app name}")
        print("\t20. say goodbye")


#function to search inputs on google
def search_google(said):
    if "google" in said:
        indx = said.lower().split().index('google')
        query = said.split()[indx + 1:]
        url = "http://google.com/search?q=" + "+".join(query)
        webbrowser.get(brave_path).open_new(url)
        say("here is what I found on " + str(query))


#function to search videos on youtube
def search_youtube(said):
    if 'youtube' in said.lower():
        say("Opening in youtube")
        indx = said.lower().split().index('youtube')
        query = said.split()[indx + 1:]
        url = "https://www.youtube.com/results?search_query=" + "+".join(query)
        webbrowser.get(brave_path).open_new(url)
        say("here is what I found on " + str(query))


#function to search location
def search_location(said):
    if "find location of" in said or "find the location of" in said:
        indx = said.lower().split().index('of')
        query = said.split()[indx + 1:]
        url = "http://google.com/maps/place/" + "+".join(query) + "/&amp"
        webbrowser.get(brave_path).open_new(url)
        say("here is the location of " + str(query))


#function that opens an application
def open_application(said):
    if "chrome" in said:
        say("opening Google Chrome")
        os.startfile('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')
        
    elif "brave" in said:
        say("opening brave browser")
        os.startfile("C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe")
        
    elif "garena" in said:
        say("opening garena")
        os.startfile("C:/Program Files (x86)/Garena/Garena/Garena.exe")
        
    elif "word" in said:
        say("opening M S word")
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE")
        
    elif "powerpoint" in said:
        say("opening powerpoint")
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/POWERPNT.EXE")
    
    elif "notepad" in said:
        say("opening notepad")
        os.startfile("notepad")

    elif "calculator" in said:
        say("opening calculator")
        os.startfile("calculator")
        
    else:
        say("sorry, that application is not installed in the system. or I wasn't programmed to open "
              "that application")


#function to close an application
def close_app(said):
    data = said.replace("close ", "")
    try:
        os.system(f"TASKKILL /F /IM {data}.exe")
        say(f"closing {data}")
    
    except:
        say(f"sorry, {data} is not running.")
        


#fetch the database and check if there's a result from query
def get_db_result(said):
    data = said
    try:
        mycursor.execute("SELECT response FROM commands WHERE command='%s'" % (data))
        row = mycursor.fetchone()[0]
        mydb.commit()
        say(row)
    except:
        print("Assistant: Error! No data found in the database.")
    finally:
        mydb.close


#main function that contains the commands of other functions
def main(said):
    service = authenticate_user()
    choose_voice(said)
    notepad(said)
    nircmd(said)
    wolfram(said)
    weather_check(said)
    snr(said)
    do_commands(said)
    search_google(said)
    search_location(said)
    search_youtube(said)
    get_db_result(said)
    date = get_date(said)
    get_reminder(date, service, said)
    quit(said)

    if "open" in said:
        open_application(said)

    if "write mode" in said:
        say("write mode activated.")

    if "close" in said:
        close_app(said)


def main_write(said):
    service = authenticate_user()
    choose_voice(said)
    notepad(said)
    nircmd(said)
    wolfram(said)
    weather_check(said)
    snr(said)
    do_commands(said)
    search_google(said)
    search_location(said)
    search_youtube(said)
    get_db_result(said)
    date = get_date(said)
    get_reminder(date, service, said)
    quit(said)
        
    if "open" in said:
        open_application(said)

    if "close" in said:
        close_app(said)


greet()
