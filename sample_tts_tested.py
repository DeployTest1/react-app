
from gtts import gTTS
import pyttsx3

text = "The stable diffusion model is a mathematical model that describes the b>
engin =pyttsx3.init()

engin.say(text)
tts = gTTS(text, lang='en',slow=False)
tts.save("Output2.mp3")
engin.runAndWait()
