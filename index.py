import speech_recognition as sr
import webbrowser

def open_instagram():
    url = "https://www.instagram.com/"
    webbrowser.open(url)

def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say 'open Instagram' to open Instagram.")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            if "open Instagram" in command:
                open_instagram()
                print("Instagram opened successfully!")
            else:
                print("Command not recognized.")

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    main()
