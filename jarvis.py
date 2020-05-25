import wolframalpha
import PySimpleGUI as sg
import wikipedia
import pyttsx3

client = wolframalpha.Client('4UW6LT-6757UHW5GY')
engine = pyttsx3.init()

sg.theme('DarkBlue')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Hello, I am JARVIS')],
          [sg.Text('Please enter what you would like to find out:'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('JARVIS Supercomputer', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):  # if user closes window or clicks cancel
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking("Wolfram Result: " + wolfram_res, "Wikipedia Result: " + wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()

window.close()
