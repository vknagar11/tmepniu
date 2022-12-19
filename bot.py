import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am teddy. Please tell me how may I help you")       

def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")   
        r.pause_threshold = 0.68
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
            
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to,teddy):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('v.k.nagar100@gmail.com', 'vknagar13')
    server.sendmail('v.k.nagar100@gmail.com', to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
   
        query = takeCommand().lower()

        
        if 'what is' in query:
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'class 10 chapter 1' in query:
            webbrowser.open("youtube.com")

        elif 'class 10 chapter 2' in query:
            webbrowser.open("google.com")

        if 'class 10' in query:
            speak("https://vknagar11.github.io/git_vs/mathematics.html")


        if 'class 9' in query:
            speak("tell chapter name")
        
        if 'class 7' in query:
            speak("tell chapter name")
        
        if 'class 8' in query:
            speak("tell chapter name")
        if 'chapter 1' in query:
                webbrowser.open("youtube.com") 
                speak("opening") 

        if 'tell me a joke' in query:
            speak("joke s ghar nai chalta hai phad le") 


        elif 'kill yourself' in query:
            speak("aww")
            speak("goodbye")
            print("quting...")
            break 
 
            
