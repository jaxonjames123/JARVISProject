import wolframalpha
import PySimpleGUI as sg
import wikipedia
import pyttsx3
import speech_recognition as sr

##client = wolframalpha.Client('API Key here')
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
                if event in (None, 'Cancel'):  # if user closes window or clicks cancel
                    break
            except wikipedia.exceptions.DisambiguationError:
                wolfram_res = next(client.query(r.recognize_google(audio)).results).text
                engine.say(wolfram_res)
                sg.PopupNonBlocking(wolfram_res)
                if event in (None, 'Cancel'):  # if user closes window or clicks cancel
                    break
            except wikipedia.exceptions.PageError:
                wolfram_res = next(client.query(r.recognize_google(audio)).results).text
                engine.say(wolfram_res)
                sg.PopupNonBlocking(wolfram_res)
                if event in (None, 'Cancel'):  # if user closes window or clicks cancel
                    break
            except:
                wiki_res = wikipedia.summary(r.recognize_google(audio), sentences=2)
                engine.say(wiki_res)
                sg.PopupNonBlocking(wiki_res)
                if event in (None, 'Cancel'):  # if user closes window or clicks cancel
                    break
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # Logic allows user to type out a question
    if event == 'Type a question':
        layout = [[sg.Text('Please type your question below')],
                  [sg.InputText()],
                  [sg.Button('Ok'), sg.Button('Cancel')]]
        window2 = sg.Window('JARVIS Supercomputer', layout)
        while True:
            event, values = window2.read()
            if event in (None, 'Cancel'):  # if user closes window or clicks cancel
                break
            try:
                wiki_res = wikipedia.summary(values[0], sentences=2)
                wolfram_res = next(client.query(values[0]).results).text
                engine.say(wolfram_res)
                sg.PopupNonBlocking("Wolfram Result: " + wolfram_res, "Wikipedia Result: " + wiki_res)
                if event in (None, 'Cancel'):  # if user closes window or clicks cancel
                    break
            except wikipedia.exceptions.DisambiguationError:
                wolfram_res = next(client.query(values[0]).results).text
                engine.say(wolfram_res)
                sg.PopupNonBlocking(wolfram_res)
                if event in (None, 'Cancel'):  # if user closes window or clicks cancel
                    break
            except wikipedia.exceptions.PageError:
                wolfram_res = next(client.query(values[0]).results).text
                engine.say(wolfram_res)
                sg.PopupNonBlocking(wolfram_res)
                if event in (None, 'Cancel'):  # if user closes window or clicks cancel
                    break
            except:
                wiki_res = wikipedia.summary(values[0], sentences=2)
                engine.say(wiki_res)
                sg.PopupNonBlocking(wiki_res)
                if event in (None, 'Cancel'):  # if user closes window or clicks cancel
                    break

    engine.runAndWait()

window.close()
