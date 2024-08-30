import pyttsx3 #perpustakaan Python untuk sintesis suara yang bekerja secara offline
import speech_recognition as sr  # perpustakaan Python untuk pengenalan suara
import os

def synthesize_speech(text):
    # Initialize pyttsx3
    engine = pyttsx3.init()

    engine.setProperty('voice', 'com.apple.ttsbundle.Male-Indonesian') 

    # Play the converted file using pyttsx3
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Silakan bicara...")
        audio = recognizer.listen(source)

        try:
            # Using google to recognize audio
            text = recognizer.recognize_google(audio, language='id-ID')
            print(f"Anda mengatakan: {text}")
            return text
        except sr.UnknownValueError:
            print("Maaf, saya tidak mengerti apa yang Anda katakan.")
            return ""
        except sr.RequestError:
            print("Tidak dapat meminta hasil dari layanan pengenalan suara.")
            return ""


def main():
    print("Program Sintesis Suara Bahasa Indonesia")
    while True:
        print("Apakah anda ingin memasukkan teks atau suara? (ketik 'teks' atau 'suara', atau 'keluar' untuk berhenti)")
        method = input("Masukkan metode: ").lower()

        if method == 'keluar':
            print("Program dihentikan.")
            break
        if method == 'teks':
            text = input("Masukkan teks (atau ketik 'keluar' untuk berhenti):")
            if text.lower() == 'keluar':
                print("Program dihentikan.")
                break
        elif method == 'suara':
            text = recognize_speech()
            if text.lower() == 'keluar':
                print("Program dihentikan.")
                break
        else:
            print("Metode tidak dikenal. Silakan masukkan 'teks' atau 'suara'.")
            continue


        # Synthesize speech
        synthesize_speech(text)

if __name__ == "__main__":
    main()