import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit
import datetime
import wikipedia
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = r"C:\Users\Saaransh Shandilya\Desktop\python\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
driver.maximize_window()
listen= sr.Recognizer()
def audio(text):
    engine=pt.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty("rate",140)
    engine.say(text)
    engine.runAndWait()

def take_command():
    
    with sr.Microphone() as source:
        print('Please speak')
        audio("Please say a command")
        voice=listen.listen(source)
        command=listen.recognize_google(voice)
        command=command.lower()
        if 'jarvis' in command:
            command=command.replace('jarvis','')
            print(command)
    return command

def run():
    
    command= take_command()
    if 'play' in command:
        song=command.replace('play','')
        audio('Yes sir, playing'+song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        audio('Its '+ time)


    elif 'tell me about' in command:
        obj=command.replace('tell me about','')
        info=wikipedia.summary(obj, 1)
        audio(info)

    elif 'cook' in command:
        audio('Heres a video for the recipe')
        pywhatkit.playonyt(command)

    elif 'open chrome' in command:
        app=command.replace('open','')
        audio('opening '+app)
        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome")

    elif 'open notepad' in command:
        audio('Opening notepad')
        os.system('Notepad')

    elif 'add' in command:
        exc=command.replace('add','')
        exc=exc.replace('and','/')
        num1=int(exc.split('/')[0])
        print(num1)
        num2=int(exc.split('/')[1])
        sum=num1+num2
        print(sum)
        sum=str(sum)
        audio('The sum is'+sum)

    elif 'subtract' in command:
        exc=command.replace('subtract','')
        exc=exc.replace('from','/')
        num1=int(exc.split('/')[0])
        print(num1)
        num2=int(exc.split('/')[1])
        diff=num2-num1
        print(diff)
        diff=str(diff)
        audio('The difference is'+diff)
    
    elif 'multiply' in command:
        exc=command.replace('multiply','')
        exc=exc.replace('and','/')
        num1=int(exc.split('/')[0])
        num2=int(exc.split('/')[1])
        prod=num1*num2
        print(prod)
        prod=str(prod)
        audio('The product is'+prod)

    elif 'divide' in command:
        exc=command.replace('divide','')
        exc=exc.replace('from','/')
        num1=int(exc.split('/')[0])
        print(num1)
        num2=int(exc.split('/')[1])
        diff=num1/num2
        print(diff)
        diff=str(diff)
        audio('The quiotient is'+diff)

    elif 'message' in command:
        rec = command.replace('to','/')
        rec = rec.split('/')[1]
        audio("What's the message")
        with sr.Microphone() as source:
            voice=listen.listen(source)
            message=listen.recognize_google(voice)
            message=message.lower()
            print(message)
        driver.get("https://web.whatsapp.com/")
        sleep(30)
        driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div')
        t = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        t.send_keys(rec)
        t.send_keys(Keys.RETURN)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(message)
        t1 = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
        t1.send_keys(Keys.RETURN)


    elif 'sleep' in command:
        audio("For how long, sir?")
        with sr.Microphone() as source:
            st=listen.listen(source)
            tm=listen.recognize_google(st)
            tm=int(tm)
            print(tm)
        sleep(tm)

    elif 'shutdown' in command:
        j=0
        audio('Goodbye, sir!')    
    
    else:
        audio('Please repeat yourself u werent clear')
    
    return j

i=1 
while (i==1):
    i=run()