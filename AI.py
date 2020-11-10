import pyautogui
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import cv2
import pywhatkit
import time

# Setting up the TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voices = engine.setProperty('voice', voices[1].id)
engine.setProperty("language","hi")

#Setting chrome path for webbrowser
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

#Function for getting text and converting it to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Function for wishing the user and taking the login info
def login():
    # Wishing the User
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")

    else:
        speak('Good Evening Sir')
    
    # Software Information
    speak('This is the Series One Processor Hyper Intelligent Encrypter')
    speak('Please login to confirm your identity')

    # Login Option
    user = str(input('Username : '))
    speak('Welcome')
    time.sleep(0.05)
    speak(user)
    
#  Function to take speech (commands) from the user   
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print('User said:\n', query)
    except Exception as e:
        speak("Say that again Please")
        return 'None'
    return query

# Function to automate sending emails
def mailto(content,mail):

    # Setting the server
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()

    # Fetching Mail Id and password w.r.t. User
    if(user == "RK"):
        with open('C:\\Users\\RUSHIKESH\\Desktop\\rushi.txt','r') as f:
            usrinfo = f.readlines()
            f.close()

    # Logging in with user id and password
    server.login(usrinfo[0],usrinfo[1])

    # Sending the email
    server.sendmail(usrinfo[0],mail,content)

    # Closing the server
    server.close()


if __name__ == "__main__":
    print('S.O.P.H.I.E\n')
    login()
    state = 1

    while(state == 1):
        query = takecommand().lower()

        # Searching the wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...Please wait')
            query = query.replace('Wikipedia','')
            results = wikipedia.summary(query,sentences = 2)
            speak('According to Wikipedia')
            speak(results)
        
        # Opening the regularly used websites
        elif 'youtube' in query:
            speak('Opening.Please Wait')
            webbrowser.get(chrome_path).open('youtube.com')

        elif 'whatsapp' in query:
            speak('Opening. Please Wait')
            webbrowser.get(chrome_path).open('web.whatsapp.com') 

        elif 'open moodle' in query:
            speak('Opening. Please Wait')
            webbrowser.get(chrome_path).open('moodle.coep.org.in')           
                
        elif 'google' in query:
            speak('Opening.  Please Wait')
            webbrowser.get(chrome_path).open('google.com')
        
        elif 'github' in query:
            speak('Opening.  Please Wait')
            webbrowser.get(chrome_path).open('github.com')
        
        # Playing Music
        elif 'play music' in query:
            speak('Processing')
            music_dir = 'T:\\Music\\'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[92]))
        
        # Speak Time
        elif 'time' in query:
            strTime = datetime.datetime.now()
            speak("The time is ")
            speak(strTime)   

        # Opening Basic Executables
        elif 'excel' in query:
            excel_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
            os.startfile(excel_path)
        
        elif 'power' in query:
            ppt_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'
            os.startfile(ppt_path)
        
        elif 'word' in query:
            word_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
            os.startfile(word_path)

        elif 'calculator' in query:
            speak('Opening Piezon 1.0.0')
            os.startfile('.\piezon.exe')                

        # Opening Code Editors
        elif 'editor' in query:
            speak('Which Editor?')
            editor = takecommand()
            
            try:
                if 'notepad' in editor:
                    speak('Opening Notepad')
                    editor_path = 'C:\\Windows\\System32\\notepad.exe'
                    os.startfile(editor_path)
                    
                elif 'code' in editor:
                    speak('Opening Visual Studio')
                    editor_path = 'C:\\Users\\RUSHIKESH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                    os.startfile(editor_path)
            
            except Exception as e:
                print(e)
        

        # Opening Built In game
        elif 'game' in query:
            import MyGame
            MyGame.gameloop()
            speak('Done')

        # Sending emails
        elif 'email' in query:
            try:
                speak('Say your message here')
                content = takecommand()

                with open('C:\\Users\\RUSHIKESH\\Desktop\\mailids.txt') as mailid:
                    emails = mailid.readlines()

                speak('Which mail?')
                emailid = takecommand()

                if 'dad' in emailid:
                    mail = emails[0]
                elif 'sister' in emailid:
                    mail = emails[1]
                
                status = mailto(content,mail)
                speak('Mail Sent')

            except Exception as e:
                print(e)
                speak('Sending Failed')   

        # Taking a photo
        elif 'photo' in query:
            try:
                camera = cv2.VideoCapture(0)
                read_value,image = camera.read()
                cv2.imwrite('selfie' + str(selfie_number) + '.png',image)
                speak('Photo Saved')
                del(camera)
            
            except Exception as e:
                print(e)
        
        # Exitting the Assistant
        elif 'exit' in query:
            speak('Exitting. Please Wait')
            state = 0

        # Taking a Screenshot
        elif 'shot' in query:
            shot = pyautogui.screenshot()
            number_of_shots += 1
            shot.save('Screenshot' + str(number_of_shots) + '.png')
            speak('Screenshot saved')
        
        # Automating whatsapp
        elif 'message' in query:
            hour = int(datetime.datetime.now().hour)
            minute = int(datetime.datetime.now().minute)
            
            speak('Message to whom?')
            receiver = takecommand()

            with open('C:\\Users\\RUSHIKESH\\Desktop\\contacts.txt') as sim:
                contacts = sim.readlines()
            
            speak('Say your message')
            message = takecommand()

            if 'dad' in receiver:
                pywhatkit.sendwhatmsg(contacts[0], message, hour,minute+2)
            elif 'sister' in receiver:
                pywhatkit.sendwhatmsg(contacts[1], message, hour,minute+2)
            speak('Message Sent')

        # Shutting Down the System  
        elif 'shutdown' in query:
            speak('You are about to shutdown the system')
            speak('PLease be certain')
            speak('Shall I shut down?')
            stat = takecommand()

            if 'yes' in stat:
                shutdelay = 5
                speak('Shutting the system in')
                while(shutdelay>0):
                    countdown =  str(shutdelay) + 'seconds'  
                    speak(countdown)
                    shutdelay += -1
                os.system("shutdown /s /t 1")
        
        # Rebooting the System
        elif 'reboot' in query:
            speak('You are about to reboot the system')
            speak('PLease be certain')
            speak('Shall I reboot?')
            print('Shutdown?')
            stat = takecommand()

            if 'restart' in stat:
                shutdelay = 5
                speak('Shutting the system in')
                while(shutdelay>0):
                    countdown =  str(shutdelay) + 'seconds'  
                    speak(countdown)
                    shutdelay += -1
                os.system("shutdown /r /t 1")        