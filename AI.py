import pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser

#Setting Up Sapi Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voices = engine.setProperty('voice', voices[1].id)
engine.setProperty("language","hi")

#This Speak function speaks a string.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Wishme command wishes the user according to data and time.
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")

    else:
        speak('Good Evening Sir')
    
    speak('I am sophie')

#This function converts speech to text        
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print('User said',query)
    except Exception as e:
        print("Say that again Please")
        return 'None'
    
    return query

#Main Code
if __name__ == "__main__":
    clear = lambda: os.system('cls')

    clear()
    wishMe()
    
    while True:
        query = takeCommand().lower()
        
        if 'excel' in query:
            speak("Opening Excel")
            excel_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
            os.startfile(excel_path) 
        
        elif 'word' in query:
            speak("Opening Word")
            word_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
            os.startfile(word_path)
        
        elif 'powerpoint' in query:
            speak("Opening Powerpoint")
            power_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'
            os.startfile(power_path)

        elif 'paint' in query:
            speak("Opening Paint")
            paint_path = 'C:\\Windows\\system32\\mspaint.exe'
            os.startfile(paint_path)

        elif 'editor' in query:
            speak("Which editor you want to open ?")
            editor = takeCommand()
            try:
                if 'notepad' in editor:
                    editor_path = 'C:\\Windows\\system32\\notepad.exe'
                    os.startfile(editor_path)
                elif 'code' in editor:
                    editor_path = 'C:\\Users\\RUTUJA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                    os.startfile(editor_path)
            
            except Exception as e:
                print(e)
                
        
        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("Here is the location") 
            speak(location) 
            webbrowser.open("https://www.google.nl/maps/place/" + location + "") 
        

        