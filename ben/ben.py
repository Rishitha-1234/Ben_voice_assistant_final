import pyttsx3
import pywin32_system32
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import time
import threading
import requests


def search_youtube(song_name):
    api_key = 'AIzaSyAO5ISFDxLLcj4h4jf6I0vqNbJvpk-ehEU'
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={song_name}&key={api_key}&type=video"
    response = requests.get(url).json()
    if response['items']:
        video_url = f"https://www.youtube.com/watch?v={response['items'][0]['id']['videoId']}"
        wb.open(video_url)  # Opens the video URL in the default web browser and plays it
    else:
        speak("Sorry, I couldn't find the song.")
        print("Sorry, I couldn't find the song.")

def speak(audio) -> None:
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


def time() -> None:
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)


def date() -> None:
    day: int = datetime.datetime.now().day
    month: int = datetime.datetime.now().month
    year: int = datetime.datetime.now().year
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print(f"The current date is {day}/{month}/{year}")


def wishme() -> None:
    print("Ben,Initialising...")
    speak("Ben,Initialising...")
    print("Hi there!! ")
    speak("Hi there!!  ")

    hour: int = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning!!")
        print("Good Morning!!")
    elif 12 <= hour < 16:
        speak("Good Afternoon!!")
        print("Good Afternoon!!")
    elif 16 <= hour < 24:
        speak("Good Evening!!")
        print("Good Evening!!")
    else:
        speak("Good Night, See You Tommorrow")

    print("I am Ben,How Can I assist You today!!")
    speak("I am Ben,How Can I assist You today!!")



def screenshot() -> None:
    # """Take a screenshot and save it with a timestamp."""
    # Take the screenshot
    img = pyautogui.screenshot()
    
    # Get the current time for the filename
    current_time = datetime.datetime.now().strftime("%I-%M-%S %p")
    
    # Define the path to the OneDrive Pictures Screenshots directory
    screenshots_path = r"C:\Users\singa\OneDrive\Pictures\Screenshots 1"
    
    # Ensure the directory exists
    if not os.path.exists(screenshots_path):
        os.makedirs(screenshots_path)
    
    # Construct the full file path with timestamp
    img_path = os.path.join(screenshots_path, f"screenshot_{current_time}.png")
    
    # Save the screenshot
    img.save(img_path)
    
    # Print the path where the screenshot is saved
    print(f"Screenshot saved to {img_path} as screenshot {current_time}")
    
    # Announce the file save with timestamp
    speak("I have taken screenshot")
    speak(f"Screenshot has been saved as screenshot {current_time}")



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query




from jokeapi import Jokes
import asyncio

async def print_joke(categories=None):
    j = await Jokes()  
    joke = await j.get_joke(category=categories)  
    
    if joke["type"] == "single":
        print(joke["joke"])
        speak(joke["joke"])
    else:
        print(joke["setup"])
        speak(joke["setup"])
        print(joke["delivery"])
        speak(joke["delivery"])


def get_weather(city):
    api_key = '49b4b24fce8f4cb5861fd43caf98f6b2'  # Replace with your Weatherbit API key
    url = f"https://api.weatherbit.io/v2.0/current?city={city}&key={api_key}"
    response = requests.get(url).json()
    if response['data']:
        temp = response['data'][0]['temp']
        weather_description = response['data'][0]['weather']['description']
        weather_report = f"Current weather in {city} is {weather_description} with a temperature of {temp}°C."
        return weather_report
    else:
        return "Sorry, I couldn't fetch the weather data right now."
    
def get_news():
    api_key = '14dd272fbbff4e328b068e18ce1c0c28'  # Replace with your NewsAPI key
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url).json()
    if response['status'] == 'ok' and response['articles']:
        headlines = [article['title'] for article in response['articles'][:5]]  # Get top 5 headlines
        news_summary = "Here are the top news headlines: " + ", ".join(headlines)
        return news_summary
    else:
        return "Sorry, I couldn't fetch the news right now."

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speak("I'm your voice assistant, How can I assist you today!!.")
            print("I'm your voice assistant, How can I assist you today!!.")

        elif "how are you" in query:
            speak("I'm fine, What about you?")
            print("I'm fine, What about you?")

        elif "fine" in query:
            speak("I'm Glad to hear that, How can I assist you today!!")
            print("I'm Glad to hear that, How can I assist you today!!")

        elif "good" in query:
            speak("I'm Glad to hear that, How can I assist you today!!")
            print("I'm Glad to hear that, How can I assist you today!!")

        elif "okay" in query:
            speak("It’s good to hear you’re okay. Let me know if there’s anything I can do to make your day better!")
            print("It’s good to hear you’re okay. Let me know if there’s anything I can do to make your day better!")

        elif "bad" in query:
            speak("I hope things improve for you soon. How can I help you?!")
            print("I hope things improve for you soon. How can I help you?!")

        

        elif "wikipedia" in query:
            try:
                speak("Ok wait, I'm searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page, please ask something else")

        elif "open youtube" in query:
            wb.open("https://www.youtube.com/")

        elif "open google" in query:
            wb.open("https://www.google.com/")
        
        elif "open instagram" in query:
            wb.open("https://www.instagram.com/")
            
        elif "open facebook" in query:
            wb.open("https://www.facebook.com/")

        elif "open stack overflow" in query:
            wb.open("https://www.stackoverflow.com/")

        
        elif "search on google" in query:
            try:
                speak("What should I search?")
                print("What should I search?")
                search = takecommand()
                # Construct the Google search URL
                google_search_url = f"https://www.google.com/search?q={search}"
                # Open the search URL in a new tab
                wb.open_new_tab(google_search_url)
                print(search)

            except Exception as e:
                speak("Can't perform the search now, please try again later.")
                print("Can't perform the search now, please try again later.")


        elif "search on youtube" in query:
            try:
                speak("What should I search for on YouTube?")
                print("What should I search for on YouTube?")
                search = takecommand()
                # Construct the YouTube search URL
                youtube_search_url = f"https://www.youtube.com/results?search_query={search}"
                # Open the search URL in a new tab
                wb.open_new_tab(youtube_search_url)
                print(search)

            except Exception as e:
                speak("Can't perform the search now, please try again.")
                print("Can't perform the search now, please try again.")
                
                
        elif "weather" in query:
            try:
                speak("Which city?")
                print("Which city?")
                city = takecommand()
                weather_report = get_weather(city)
                speak(weather_report)
                print(weather_report)
            except Exception as e:
                speak("Can't fetch the weather now, please try again later.")
                print("Can't fetch the weather now, please try again later.")


        elif "screenshot" in query:
            screenshot()
            
        elif "tell me a joke" in query:
            print("Sure")
            speak("Sure")
            asyncio.run(print_joke(categories=['programming', 'dark']))

                
        elif "play song" in query:
            try:
                speak("Which song?")
                print("Which song?")
                song_name = takecommand()
                search_youtube(song_name)
                speak(f"Playing {song_name} on YouTube.")
                print(f"Playing {song_name} on YouTube.")
            except Exception as e:
                speak("Can't perform the search now, please try again later.")
                print("Can't perform the search now, please try again later.")
                
        elif "news" in query:
            try:
                news_summary = get_news()
                speak(news_summary)
                print(news_summary)
            except Exception as e:
                speak("Can't fetch the news now, please try again later.")
                print("Can't fetch the news now, please try again later.")
    
        elif "go offline" in query:
            speak("Goodbye! Have a great day!")
            print("Goodbye! Have a great day!")
            quit()
        elif "quit" in query:
            speak("Goodbye! Have a great day!")
            print("Goodbye! Have a great day!")
            quit()
        elif "good bye" in query:
            speak("Goodbye! Have a great day!")
            print("Goodbye! Have a great day!")
            quit()
        elif "bye" in query:
            speak("Goodbye! Have a great day!")
            print("Goodbye! Have a great day!")
            quit()
        
        
