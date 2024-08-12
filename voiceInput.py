import speech_recognition as sr
# import noisereduce as nr
# import numpy as np

r = sr.Recognizer()

def voiceInput():
    while(True):
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Speak your answer: ")
            audio = r.listen(source)

            # audio_data = np.frombuffer(audio.get_wav_data(), dtype=np.int16)
            # reduced_noise = nr.reduce_noise(y=audio_data, sr=audio.sample_rate)
            # audio_data = sr.AudioData(reduced_noise.tobytes(), audio.sample_rate, audio.sample_width)
            
            try:
                command = r.recognize_google(audio)
                return command
            
            except sr.RequestError as e:
                print(e)

            except sr.UnknownValueError:
                print("Unknown error")