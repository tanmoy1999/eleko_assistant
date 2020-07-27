import speech_recognition as sr
import wikipedia as wiki
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()    

def eleko_wiki(text):
    k = text.split('search for')
    str1 = ""
    for ele in k:
         str1+=ele            
            
    print(wiki.summary(str1,sentences=3))
    speak(wiki.summary(str1,sentences=3))

speak('hiii, I am eleko. How may i help you')
t=1
while (t!=0):
    
    with sr.Microphone() as source:
        print("say anything")
        audio = r.listen(source)
        try: 
            text = r.recognize_google(audio)            
            print('you said {}'.format(text))
            search = ['search for','tell me','tell me about','define','meaning of']
            for i in search:
                if i in text:
                    k = text.split(i)
                    str1 = ""
                    for i in k:
                        str1+=i
                
                    speak('you said {}'.format(text))
                    eleko_wiki(str1)
                    break
                elif 'thank you' in text:
                    speak('Good Bye. Have a great day ahead')
                    break
                    
            '''elif 'weather' in text.split():
                speak('Place where you stay?')
            elif 'multiply' in text.split():
                p = text.split('multiply')
                mul = 0
                for ele in p:
                    mul = k[ele]*mul
                    speak(mul)'''

        except:
            print('Try again!!')
            speak('I cant hear you')


'''a = str(input())
search = ['search for','tell me','define']
for p in search:
    k = a.split(p)
    str1 = ""
    for i in k:
        str1+=i

print(str1)'''

'''a = str(input())
search = ['search for','tell me','define']
for i in search:
    if i in a:
        k = a.split(i)
        str1 = ""
        for i in k:
            str1+=i

print(str1)'''


'''if search in a.split():
    print('1')
else:
    print('0')'''





