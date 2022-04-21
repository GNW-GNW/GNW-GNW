import pyttsx3

#changing voice to a girl

friend = pyttsx3.init()
voices = friend.getProperty('voices')
friend.setProperty('voice', voices[1].id)
friend.say("Hello motherfucker" + "I love you and fuck you. Goodbye!")
friend.runAndWait()
friend.stop()