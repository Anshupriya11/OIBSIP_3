import speech_recognition as sr
import pyttsx3
import random

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set the voice to female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def listen_command():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Please try again.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm unable to access the Google API. Please check your internet connection.")
        return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a fake noodle? An impasta!",
        "I entered 10 puns in a contest to see which would win. No pun in ten did."
    ]
    joke = random.choice(jokes)
    speak(joke)

def ai_assistant():
    speak("Good day! How may I be of service?")
    while True:
        command = listen_command()
        if any(exit_word in command for exit_word in ["exit", "goodbye", "quit", "stop"]):
            speak("Goodbye!")
            break
        elif "hello" in command:
            speak("Hey!, how are you?")
        elif "i am fine what about you" in command:
            speak("I'm doing great, thanks for asking. How about you?")
        elif "tell me a joke" in command:
            tell_joke()
        elif "vegetarian lasagna" in command:
            speak("Ah, the classic vegetarian lasagna! A delightful choice indeed.")
            speak("Do you have any specific dietary preferences or restrictions?")
            command = listen_command()
            if "no" in command:
                speak("Excellent! Here's a scrumptious recipe for you:")
                speak("First, preheat your oven to 375 degrees Fahrenheit. While that's warming up, gather your ingredients.")
                speak("You'll need lasagna noodles, spinach, mushrooms, zucchini, bell peppers, onions, garlic, marinara sauce, ricotta cheese, mozzarella cheese, and some basil and oregano for seasoning.")
                speak("Begin by sautéing the vegetables until they're tender. Then, layer them with the noodles, marinara sauce, and cheese in a baking dish. Repeat the layers, and bake in the oven for about 30 minutes or until bubbly and golden brown.")
                speak("Enjoy your culinary adventure!")
            else:
                speak("Understood. I'll keep that in mind.")
        elif "movie" in command:
            speak("Ah, a movie night! What genre are you in the mood for?")
            command = listen_command()
            if "comedy" in command:
                speak("A comedy it is! How about 'The Intouchables'? It's a delightful French film that's sure to tickle your funny bone.")
            else:
                speak("Hmm, let me think. Ah! How about 'The Grand Budapest Hotel'? It's a quirky and visually stunning film that's bound to entertain.")
        else:
            speak("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    ai_assistant()