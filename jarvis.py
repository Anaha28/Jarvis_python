import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import pywhatkit

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak (audio):
    engine.say(audio)
    engine.runAndWait()#spek it out loud


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("good morning.Have a nice day!")
    
    elif hour >=12 and hour < 18:
        speak("good afternoon")
    

    else:
        speak("good evening")
    speak("I am jarvis ,how can i assist you !?")



def play_music(song_name):
    speak(f"Playing {song_name} on YouTube")
    pywhatkit.playonyt(song_name)


def takecommand():
    #takes microphone input
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening,wait a min...")
        r.pause_threshold=1#non speaking audio seconds
        audio=r.listen(source)

    
    

    try:
        print("recognizing....")
        query=r.recognize_google(audio, language='en_in')
        print(f"user said :{query}\n")

    except Exception as e :
        print (e)   

        print ("cant get it,say that again ,please...") 
        return "none"
    return query
    try:
        results = wikipedia.summary(query, sentences=1, auto_suggest=True, redirect=True)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find anything on Wikipedia for that.")
    except wikipedia.exceptions.DisambiguationError as e:
        speak("That term is too vague. Can you be more specific?")
        print("Options:", e.options)



if __name__=="__main__":
   
    wishMe()
    #while True:
    if 1:
        query =  takecommand().lower()
        
        if 'wikipedia' in query :
            speak("searching  wikipedia.....")
            query = query.replace("wikipedia", "").strip()
            query = query.replace(".", "")  # remove dots
            query = query.title()  # capitalize properly
            results = wikipedia.summary(query, sentences=1, auto_suggest=True, redirect=True)
            
            speak("according to wikipedia")
            
            print(results.encode('ascii', errors='ignore').decode())
            speak (results)
        elif 'open youtube'in query:
            webbrowser.open("youtube.com")
        elif 'open google'in query:
            webbrowser.open("google.com")
       
        elif 'play music'in query:
            speak("Which song would you like to hear?")

           
            song=takecommand()
            play_music(song)
        elif 'the time 'in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"mam,the time is{strTime}")
