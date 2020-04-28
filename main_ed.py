import datetime
import os
import time
import webbrowser
import wolframalpha
import requests
import pyttsx3  #pip install pyttsx3==2.71
import speech_recognition as sr
import mysql.connector
from main_mysql_cred import *
from API import weather_api, app_id

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


#brave path
brave_path = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/Brave.exe %s --incognito'
brave_path_normal = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/Brave.exe %s'


#setting text to speech engine and voice rate property
engine = pyttsx3.init("sapi5")
engine.setProperty('rate', 150)


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

#function for greeting the user once the program starts
def greet():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        say("good morning")
    elif 12 <= hour < 18:
        say("good afternoon")
    else:
        say("good evening")


#function for controlling laptop's brightness, monitor, volume.
def nircmd(said):
    if 'increase volume' in said or 'volume up' in said:
        os.system("C:/nircmd.exe changesysvolume 5000")
        say("volume increased")

    if 'decrease volume' in said or 'volume down' in said:
        os.system("C:/nircmd.exe changesysvolume -5000")
        say("volume decreased")

    if 'max volume' in said:
        os.system("C:/nircmd.exe setsysvolume 65535")
        say("max volume") 

    if 'mute' in said:
        os.system("C:/nircmd.exe mutesysvolume 1")

    if 'unmute' in said:
        os.system("C:/nircmd.exe mutesysvolume 0")
        say("volume unmuted")

    if 'stand by' in said:
        os.system("C:/nircmd.exe standby")


#function for closing the program
def quit(said):
    if "goodbye" in said:
        say("okay, goodbye.")
        exit()


#function to add commands and store it in MySQL database
def add_commands(said):
    if "add command" in said:
        say("please add your command")
        command = input("Enter your command: ")
        response = input("Enter the response for your command: ")
        try:
            mycursor.execute("""INSERT INTO commands(command, response) VALUES(%s, %s)""", (command, response))
            say("done")
            mydb.commit()
        finally:

            mydb.close()


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
        print("\t3. what is today / what day is today")
        print("\t4. what's the date today")
        print("\t5. search in google / youtube")
        print("\t6. find location / find the location")
        print("\t7. open (an application)")
        print("\t8. check weather")
        print("\t9. wolfram -> query")
        print("\t10. control sounds, standby")
        print("\t11. shutdown and restart computer ---> cancel to CANCEL")
        print("\t12. write mode --> for nonverbal interaction")
        print("\t13. say goodbye")


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


#function to check the weather
def weather_check(said):
    if "weather" in said:
        try:
            search = said.replace("check the weather in ", "").replace("can you check the weather in ", "").replace(
                "what's the weather in ", "").replace("check weather in ", "")
            url = 'https://api.openweathermap.org/data/2.5/weather?q=' + search + '&appid=' + weather_api #your API
            print("Assistant: " + url)
            loc_url = 'https://openweathermap.org/find?q=' + search
            webbrowser.get(brave_path).open_new(loc_url)
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
        except sr.UnknownValueError:
            say("Sorry, I can't understand you. ")


#function to solve math problems
def wolfram(said):
    if "wolfram" in said:
        data = get_audio()
        client = wolframalpha.Client(app_id) #your own app ID
        res = client.query(data)
        try:
            output = next(res.results).text
            print("Assistant: " + str(output))
            say("The answer is," + str(output))
        except:
            say("Sorry, I dont have an answer for that")
       

#main function that contains the commands of other functions
def main():
    nircmd(said)
    add_commands(said)
    get_db_result(said)
    quit(said)
    snr(said)
    do_commands(said)
    search_google(said)
    search_location(said)
    search_youtube(said)
    weather_check(said)
    wolfram(said)

if __name__ == "__main__":
    greet()
    
    while True:
        print("Assistant: Listening...")
        said = get_audio()
        main()
        
        if "write mode" in said:
            say("write mode activated.")
            while True:
                data = input(">> ")
                said = data.lower()
                if data == "deactivate":
                    break
                else:
                    main()
