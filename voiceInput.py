import speech_recognition as sr

r = sr.Recognizer()

def voiceInput():
    while(True):
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                print("Speak your answer: ")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                return command

        except sr.RequestError as e:
            print(e)
        except sr.UnknownValueError:
            print("Unknown error")