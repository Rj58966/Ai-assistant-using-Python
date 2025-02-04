import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit as do
import wikipedia as wiki
import datetime as dt
import pyjokes
import sys

listener=sr.Recognizer()
engine=tts.init()
v_cnvrt=engine.getProperty('voices')
engine.setProperty('voice',v_cnvrt[1].id)
engine.setProperty('rate',230)
engine.say('hii there i am friday')
engine.say('how can i help you')
engine.runAndWait()


def talk_back(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('>>>Listening....')
            voice=listener.listen(source)
            command=listener.recognize_google(voice, language='en-in')
            command=command.lower()
            if 'friday' in command:
                command=command.replace('friday','')
                print(command)
    except:
        pass
    return command

def whatmsg():
    do.check_window()
    talk_back('give information')
    talk_back('enter the country code')
    code=input('enter the country code:')
    talk_back('enter the mobile number')
    mno=input('enter the mobile no.:')
    talk_back('type your message')
    msg=input('type your message:')
    talk_back('enter the time at you want to send message')
    hr=input('enter the hour:')
    mnt=input('enter the minutes:')
    do.sendwhatmsg(code+mno,msg,int(hr),int(mnt))
    print('message successfully send!')
    sys.exit()

def run():
    command=take_command()
    if 'play' in command:
        command=command.replace('play','')
        talk_back('playing'+command)
        do.playonyt(command)
    elif 'search' in command:
        command=command.replace('search','')
        do.search(command)
        talk_back('searching')
    elif 'send' in command:
        whatmsg()
    elif 'shutdown' in command:
        talk_back('confirmation!, you want to shutdown your system?')
        take_command()
        if 'yes' in command:
            print('shutting down your system')
            talk_back('shutting down your system')
            do.shutdown()
        else:
            print('operation aborted')
            talk_back('operation aborted')
            pass
    elif 'who is' in command:
        do.search(command)
        info=wiki.summary(command,1)
        talk_back(info)
    elif 'time' in command:
        time=dt.datetime.now().strftime('%I:%M %p')
        print('',time)
        talk_back('the time is'+time)
    elif 'joke' in command:
        joke=pyjokes.get_joke()
        print('',joke)
        talk_back(joke)
    elif 'exit' in command:
        sys.exit()
        
        
while True:
    run()
