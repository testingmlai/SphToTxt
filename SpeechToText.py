import speech_recognition as sr
import os


r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Speak:")
    while True:
        try:
            audio = r.listen(source, phrase_time_limit=10)
            text = r.recognize_google(audio)
            print("You said: {}".format(text))
            if text.lower() == "bye" or text.lower() == "exit":
                print("Exiting script.")
                break
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
            with open(os.path.join(downloads_path, "recognized_text.txt"), "a") as f:
                f.write(text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")
pass
