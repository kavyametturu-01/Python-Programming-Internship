import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

print("Voice Assistant Started")
speak("Hello, I am your voice assistant")

while True:
    command = input("Enter command (time, date, search, exit): ").lower()

    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print("Time:", time)
        speak(f"The time is {time}")

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        print("Date:", date)
        speak(f"Today's date is {date}")

    elif "search" in command:
        query = input("What should I search: ")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak("Searching Google")

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        print("Exiting assistant")
        break

    else:
        print("Unknown command")
        speak("Sorry, I did not understand the command")
