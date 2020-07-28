import speech_recognition as sr
import wikipedia as wiki
import pyttsx3
import requests
from pprint import pprint

r = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def weather(city):
    def weather_data(query):
	    res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')
	    return res.json()
    def print_weather(result,city):
        print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
        print("Wind speed: {} m/s".format(result['wind']['speed']))
        print("Description: {}".format(result['weather'][0]['description']))
        print("Weather: {}".format(result['weather'][0]['main']))

        speak("{}'s temperature: {}°C ".format(city,result['main']['temp']))
        speak("Wind speed: {} m/s".format(result['wind']['speed']))
        speak("Description: {}".format(result['weather'][0]['description']))
        speak("Weather: {}".format(result['weather'][0]['main']))
    def main():
        try:
            query='q='+city
            w_data=weather_data(query)
            print_weather(w_data, city)
            print()
            
        except:
            print('City name not found...')
    if __name__=='__main__':
        main()

def speak(text):
    engine.say(text)
    engine.runAndWait()    

def eleko_wiki(text):
    for i in search:
	    if i in text:
		    k=text.split(i)
		    str1 = ""
		    for i in k:
			    str1+=i
    print(wiki.summary(str1,sentences=3))
    return speak(wiki.summary(str1,sentences=3))

def eleko_greets(text):
    for i in greetings:
	    if i in text:
		    speak('Your Most Welcome!!')
def eleko_temp(text):    
    with sr.Microphone() as source:
        print("City Name: ")
        speak('say the city name')
        audio = r.listen(source)
        try: 
            city = r.recognize_google(audio)            
            print('you said {}'.format(city))
            weather(city)       
        except:
            speak('Speak Again')
            print('Speak Again')
    
    
    

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
            greetings = ['thank you','thanks','bye']
            temp = ['temperature','weather','forecast']

            if any(x in text for x in search):
                eleko_wiki(str(text))

            elif any(x in text for x in greetings):
                eleko_greets(str(text))
                t=0
            elif any(x in text for x in temp):                
                eleko_temp(str(text))

                
                
                    
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





