import speech_recognition as speech_recog

def speech():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        print("Nasłuchiwanie szumu tła...")
        recog.adjust_for_ambient_noise(audio_file)
        print("Nagrywanie dźwięku...")
        audio = recog.listen(audio_file)
        print("Transkrypcja...")
        result = recog.recognize_google(audio, language="pl-PL")

        return result