import wolframalpha
import PySimpleGUI as sg
import wikipedia
import pyttsx3
import speech_recognition as sr

client = wolframalpha.Client('4UW6LT-6757UHW5GY')
engine = pyttsx3.init()
r = sr.Recognizer()

sg.theme('DarkBlue')  # Add a touch of color

# All the stuff inside your window.
layout = [[sg.Text('Hello, I am JARVIS, please ask me a question')],
          [sg.Button('Type a question'), sg.Button('Ask a question'), sg.Button('Cancel')]]


# Create the Window
window = sg.Window('JARVIS Supercomputer', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event in (None, 'Cancel'):  # if user closes window or clicks cancel
        break
    if event == 'Ask a question':
        with sr.Microphone() as source:
            print("Please talk")
            audio = r.listen(source)
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
    # Write code for gui to allow popup window to ask a question by being typed
    # if event == 'Type a question':
    #     try:
    #         wiki_res = wikipedia.summary(values[0], sentences=2)
    #         wolfram_res = next(client.query(values[0]).results).text
    #         engine.say(wolfram_res)
    #         sg.PopupNonBlocking("Wolfram Result: " + wolfram_res, "Wikipedia Result: " + wiki_res)
    #     except wikipedia.exceptions.DisambiguationError:
    #         wolfram_res = next(client.query(values[0]).results).text
    #         engine.say(wolfram_res)
    #         sg.PopupNonBlocking(wolfram_res)
    #     except wikipedia.exceptions.PageError:
    #         wolfram_res = next(client.query(values[0]).results).text
    #         engine.say(wolfram_res)
    #         sg.PopupNonBlocking(wolfram_res)
    #     except:
    #         wiki_res = wikipedia.summary(values[0], sentences=2)
    #         engine.say(wiki_res)
    #         sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()

window.close()