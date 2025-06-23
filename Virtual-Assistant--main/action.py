import datetime
import speak
import webbrowser
import weather
import os

def Action(send) :   
  
    data_btn  = send.lower()

    if "what is your name" in   data_btn :
      speak.speak("my name is virtual Assistant")  
      return "my name is virtual Assistant"

    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn: 
        speak.speak("Hey RAJAT ,how are you !")  
        return "Hey RAJAT , how are you !" 

    elif "how are you" in  data_btn :
            speak.speak("I am doing great these days sir") 
            return "I am doing great these days sir"   

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("its my pleasure sir to stay with you")
           return "its my pleasure sir to stay with you"      

    elif "good morning" in data_btn:
           speak.speak("Good morning sir, i think you might need some help")
           return "Good morning sir, i think you might need some help"   

    elif "time now" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 

    elif "shutdown" in data_btn or "quit" in data_btn:
            speak.speak("ok sir")
            return "ok sir"  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")   
        speak.speak("gaana.com is now ready for you, enjoy your music")                   
        return "gaana.com is now ready for you, enjoy your music"
    
    elif "open github" in data_btn or "Github" in data_btn:
        webbrowser.open("https://github.com/")   
        speak.speak("github is now ready for you")                   
        return "github is now ready for you"
    
    
    elif "open chatgpt" in data_btn or "chatgpt" in data_btn:
        webbrowser.open("https://chatgpt.com/")   
        speak.speak("chatgpt is now ready for you")                   
        return "chatgpt is now ready for you"
    
    elif "open instagram" in data_btn or "instagram" in data_btn:
        webbrowser.open("https://www.instagram.com/")   
        speak.speak("Instagram is now ready for you")                   
        return "Instagram is now ready for you"
    

    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")  
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open") 
        return "YouTube open"    
    
    elif 'weather' in data_btn:
         ans = weather.Weather()
         if ans:
              speak.speak(ans)
         else:
          speak.speak("Sorry, I could not get the weather information.")
          return ans


    elif 'music from my laptop' in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("songs playing...")
        return "songs playing..." 

    else :
        speak.speak( "i'm able to understand!")
        return "i'm able to understand!"       

