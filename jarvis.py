import wolframalpha
import PySimpleGUI as sg
import wikipedia
import pyttsx3
import speech_recognition as sr

client = wolframalpha.Client('4UW6LT-6757UHW5GY')
engine = pyttsx3.init()
r = sr.Recognizer()

sg.theme('DarkBlue')  # Add a touch of color
with sr.Microphone() as source:
    # All the stuff inside your window.
    layout = [[sg.Text('Hello, I am JARVIS, please ask me a question')],
              [sg.Button('Ok'), sg.Button('Cancel')]]
    print("Please talk")
    audio = r.listen(source)

# Create the Window
window = sg.Window('JARVIS Supercomputer', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):  # if user closes window or clicks cancel
        break
    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        try:
            wiki_res = wikipedia.summary(r.recognize_google(audio), sentences=2)
            wolfram_res = next(client.query(r.recognize_google(audio)).results).text
            engine.say(wolfram_res)
            sg.PopupNonBlocking("Wolfram Result: " + wolfram_res, "Wikipedia Result: " + wiki_res)
        except wikipedia.exceptions.DisambiguationError:
            wolfram_res = next(client.query(r.recognize_google(audio)).results).text
            engine.say(wolfram_res)
            sg.PopupNonBlocking(wolfram_res)
        except wikipedia.exceptions.PageError:
            wolfram_res = next(client.query(r.recognize_google(audio)).results).text
            engine.say(wolfram_res)
            sg.PopupNonBlocking(wolfram_res)
        except:
            wiki_res = wikipedia.summary(r.recognize_google(audio), sentences=2)
            engine.say(wiki_res)
            sg.PopupNonBlocking(wiki_res)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request respyults from Google Speech Recognition service; {0}".format(e))

    engine.runAndWait()

window.close()