import speech_recognition as sr

def spech_to_text():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 1.0  # allow a second pause
            audio = r.listen(source, timeout=5, phrase_time_limit=7)
        query = r.recognize_google(audio)
        print("You said: ", query)
        return query
    except sr.WaitTimeoutError:
        return "Listening timed out"
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "API unavailable"
    except Exception as e:
        return f"Error: {e}"
