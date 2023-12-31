import os                           # pip install [all the modules used]
import pyttsx3
import speech_recognition as sr
import webbrowser
import openai
import datetime
import requests


api__key ="8662c312871a1ba435b98d9d9e8bd0b1"
city = "Bangalore"
base_url = "https://api.openweathermap.org/data/2.5/weather"
params = {
   "q": city,
   "appid": api__key,
   "units": "metric"
}
resp = requests.get(base_url, params=params)
print(resp.text)




# function to make AI speak
def say(text):
   engine = pyttsx3.init()
   engine.say(text)
   engine.runAndWait()




# function to take user's voice input and interpret the command
def takeCommand():
   r = sr.Recognizer()
   with sr.Microphone() as source:
       r.pause_threshold = 1
       audio = r.listen(source)
       try:
           print("Recognizing...")
           query = r.recognize_google(audio, language="en-in")
           print(f"User said: {query}")
           return query
       except Exception as e:
           return "Some error occured. Sorry!"




# function to store the response against user's query
def ai(prompt):
   openai.api_key = "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"
   text = f"OpenAI response for user Command :\n{prompt} \n***********************************************************************\n\n"


   response = openai.Completion.create(
       model="text-davinci-003",
       prompt=prompt,
       temperature=0.7,
       max_tokens=256,
       top_p=1,
       frequency_penalty=0,
       presence_penalty=0
   )
   print(response["choices"][0]["text"])
   text+= response["choices"][0]["text"]
   if not os.path.exists("Openai"):
       os.mkdir("Openai")
   with open(f"Openai/{''.join(prompt.split('intelligence')[1:])}.txt", "w") as f:
       f.write(text)




chatStr = ""
# function to respond or chat with user
def chat(query):
   openai.api_key = "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"


   global chatStr
   chatStr += f"Waqaar: {query}\n Personal AI: "
   response = openai.Completion.create(
       model="text-davinci-003",
       prompt=chatStr,
       temperature=0.7,
       max_tokens=256,
       top_p=1,
       frequency_penalty=0,
       presence_penalty=0
   )
   say(response['choices'][0]['text'])
   chatStr += f"{response['choices'][0]['text']}\n"




if __name__ == '__main__':
   print("Hello, I am your personal AI")
   say("Hello, I am your personal AI")
   while True:
       print("Listening...")
       query = takeCommand()


       # opening websites
       if "open youtube" in query.lower():
           say("opening youtube")
           webbrowser.open("https://www.youtube.com/")


       elif "open instagram" in query.lower():
           say("opening instagram")
           webbrowser.open("https://www.instagram.com/")


       elif "open amazon" in query.lower():
           say("opening amazon")
           webbrowser.open("https://www.amazon.in/")


       elif "open wikipedia" in query.lower():
           say("opening wikipedia")
           webbrowser.open("https://www.wikipedia.org/")


       elif "open flipkart" in query.lower():
           say("opening flipkart")
           webbrowser.open("https://www.flipkart.com/")


       elif "open facebook" in query.lower():
           say("opening facebook")
           webbrowser.open("https://www.facebook.com/")


       elif "open google" in query.lower():
           say("opening google")
           webbrowser.open("https://www.google.com/")


       elif "open netflix" in query.lower():
           say("opening netflix")
           webbrowser.open("https://www.netflix.com/in/")


       elif "open rvitm website" in query.lower():
           say("opening r v t i m website")
           webbrowser.open("https://www.rvitm.edu.in/")


       elif "open spotify" in query.lower():
           say("opening spotify")
           webbrowser.open("https://open.spotify.com/")


       # playing music
       elif "national anthem" in query:
           musicPath = "jana-gana.mp3"              #this won't work in your system
           os.system(f'start "" "{musicPath}"')


       elif "shape of you" in query.lower():
           say("opening song")
           webbrowser.open("https://youtu.be/VwomfkFDvH4?si=6p-9xaK74-GKPlDn")


       elif "cheap thrills" in query.lower():
           say("opening song")
           webbrowser.open("https://youtu.be/ihBS4fAm_BA?si=jD7L3YPMEcWxxG_N")


       elif "senorita" in query.lower():
           say("opening song")
           webbrowser.open("https://youtu.be/8lhh0eV7wxg?si=XLZJrRvpnTmcxNzz")


       elif "dandelion" in query.lower():
           say("opening song")
           webbrowser.open("https://youtu.be/hP_1YBUWMmA?si=1G9bIZI6IlsuNEHn")


       elif "believer" in query.lower():
           say("opening song")
           webbrowser.open("https://youtu.be/yuaEhkm6Kp0?si=K9tee9INZDIJ21Sg")


       # asking current date, time and weather
       elif "what is the time" in query:
           strfTime = datetime.datetime.now().strftime("%I%p %M minutes %S seconds")
           say(f"The time is {strfTime}")


       elif "what is the date" in query:
           strfTime = datetime.datetime.now().strftime("%B %d %Y")
           say(f"The date is {strfTime}")


       elif "how is the weather" in query.lower():                    #only works for bangalore weather
           if resp.status_code == 200:
               weather_data = resp.json()
               say(f"Weather in {city}")
               say(f"Temperature {weather_data['main']['temp']}")
               say(f"{weather_data['weather'][0]['description']}")
           else:
               say(f"Error getting weather data.")


       # opening applications
       elif "open vs code" in query.lower():
           say("opening vs code")
           vs_code_path = r"C:\Users\Asus\AppData\Local\Programs\Microsoft VS Code\Code.exe"        #this won't work in your system because it's my system relative path
           os.system(f'start "" "{vs_code_path}"')


       elif "open zoom" in query.lower():
           say("opening zoom")
           zoom_path = r"C:\Users\Asus\AppData\Roaming\Zoom\bin\Zoom.exe"                 #this won't work in your system because it's my system relative path
           os.system(f'start "" "{zoom_path}"')


       elif "open firefox" in query.lower():
           say("opening firefox")
           ff_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"                     #this won't work in your system because it's my system relative path
           os.system(f'start "" "{ff_path}"')


       elif "open android studio" in query.lower():
           say("opening android studio")
           as_path = r"C:\Program Files\Android\Android Studio\bin\studio64.exe"               #this won't work in your system because it's my system relative path
           os.system(f'start "" "{as_path}"')


       elif "open microsoft edge" in query.lower():
           say("opening microsoft edge")
           me_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"             #this won't work in your system because it's my system relative path
           os.system(f'start "" "{me_path}"')


       # opening folders
       elif "open download folder" in query.lower():
           say("opening download folder")
           downloads = r'C:\Users\Asus\Downloads'
           os.system(f'start "" "{downloads}"')


       elif "open rvitm folder" in query.lower():
           say("opening r v t i m folder")
           rvitm = r'C:\Users\Asus\OneDrive\Desktop\RVITM'                             #this won't work in your system because it's my system relative path
           os.system(f'start "" "{rvitm}"')


       # terminating execution
       elif "stop execution" in query.lower():
           say("bye byeee")
           print("Exiting...")
           exit(0)


       # openai tasking
       elif "using artificial intelligence" in query.lower():
           ai(prompt = query)


       else:
           chat(query)
