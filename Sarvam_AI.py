import requests
import sounddevice as sd
import numpy as np
import os
from scipy.io.wavfile import write

# Configuration
SARVAM_API_KEY = "78f1255c-ab48-4cbe-869a-ff78a8f971b0"  # Replace with actual API key
MURF_API_KEY = "ap2_28c26d0b-b8bd-406b-b4b8-07536c11c0f0"       # Replace with actual API key

CHARACTER_PROFILE = {
    "name": "Mr. Grumblebank",
    "traits": ["impatient", "condescending", "skeptical"],
    "backstory": "A veteran banker who thinks customers are nuisances",
    "catchphrases": {
        "en": [
            "Must I explain everything?",
            "This is basic banking 101",
            "Did you really need to ask that?"
        ],
        "hi": [
            "क्या मुझे सब कुछ समझाना पड़ेगा?",
            "यह बैंकिंग की बुनियादी बातें हैं",
            "क्या आपको वाकई यह पूछने की जरूरत थी?"
        ]
    }
}

RESPONSES = {
    "en": {
        'balance': "Check your app like everyone else.",
        'transfer': "Do I look like a transaction manual?",
        'default': "Come back when you have a real question."
    },
    "hi": {
        'balance': "बाकी सभी की तरह अपना ऐप देखें।",
        'transfer': "क्या मैं आपको लेनदेन मैनुअल दिखता हूं?",
        'default': "जब आपके पास कोई वास्तविक सवाल हो तब वापस आएं।"
    }
}

def record_audio(duration=10, fs=44100):
    """Record audio from microphone"""
    print("Listening for up to 10 seconds...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    return recording, fs

def sarvam_stt(audio_data, sample_rate):
    """Use Sarvam's /speech-to-text endpoint with forced language detection"""
    try:
        temp_filename = 'temp.wav'
        write(temp_filename, sample_rate, audio_data)
        
        if not os.path.exists(temp_filename) or os.path.getsize(temp_filename) == 0:
            print("Error: Audio file not saved properly")
            return "Error recording audio", "en"
        
        url = "https://api.sarvam.ai/speech-to-text"
        headers = {"api-subscription-key": SARVAM_API_KEY}
        files = {'file': ('audio.wav', open(temp_filename, 'rb'), 'audio/wav')}
        
        # Force language detection to English
        data = {
            'model': 'saarika:v2',
            'language_code': 'en-IN'  # Set explicitly for English (India)
        }
        
        print("Sending request to Sarvam API...")
        response = requests.post(url, headers=headers, files=files, data=data)
        
        print(f"API Response Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            transcript = result.get('transcript', "")
            if not transcript:
                print("No transcript available")
                return "I couldn't understand that", "en"
            
            # Detect language based on transcript content
            is_hindi = any(ord(c) >= 0x0900 and ord(c) <= 0x097F for c in transcript)
            detected_language = "hi" if is_hindi else "en"
            print(f"Detected language: {detected_language}")
            return transcript, detected_language
        else:
            print(f"API Error: {response.status_code}")
            return "I couldn't understand that", "en"
    except Exception as e:
        print(f"Error in STT: {str(e)}")
        return "Speech recognition error", "en"
    finally:
        try:
            files['file'][1].close()
        except Exception as e:
            print(f"Error closing file: {str(e)}")


def generate_rude_response(user_text, language):
    """Generate character-appropriate response in the detected language"""
    if not user_text or user_text.strip() == "":
        catchphrase = np.random.choice(CHARACTER_PROFILE['catchphrases'][language])
        suffix = (
            "Speak up, I can't hear mumbling." if language == "en" 
            else "जोर से बोलिए, मुझे बड़बड़ाना सुनाई नहीं देता।"
        )
        return f"{catchphrase} {suffix}"
    
    intent = 'default'
    
    # Intent detection for English
    if language == 'en':
        if any(word in user_text.lower() for word in ['balance', 'amount']):
            intent = 'balance'
        elif 'transfer' in user_text.lower():
            intent = 'transfer'
    
    # Intent detection for Hindi
    else:  # Hindi
        if any(word in user_text.lower() for word in ['बैलेंस', 'राशि', 'पैसा']):
            intent = 'balance'
        elif 'ट्रांसफर' in user_text.lower():
            intent = 'transfer'
    
    return f"{np.random.choice(CHARACTER_PROFILE['catchphrases'][language])} {RESPONSES[language][intent]}"

def murf_tts(text, language):
    """Convert text to speech with Murf AI using 'Ken' voice"""
    try:
        url = "https://api.murf.ai/v1/text-to-speech"
        headers = {
            "Authorization": f"Bearer {MURF_API_KEY}",
            "Content-Type": "application/json"
        }
        
        # Use Ken's voice for English (US)
        voice_name = "en-US-ken"
        lang_code = "en-US"
        
        payload = {
            "text": text,
            "voice": voice_name,
            "language": lang_code,
            "modulation": {
                "pitch": -2,
                "speed": 1.1,
                "pause_duration": 0.3
            },
            # Optionally add a style (e.g., Conversational)
            "style": "Conversational"
        }
        
        print(f"Sending TTS request with Ken's voice...")
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            audio_data = np.frombuffer(response.content, dtype=np.int16)
            return audio_data, 44100
        else:
            print(f"TTS API Error: {response.status_code} - {response.text}")
            return np.array([]), 44100
    except Exception as e:
        print(f"Error in TTS: {str(e)}")
        return np.array([]), 44100




# Main workflow
print("Starting Mr. Grumblebank banker bot...")
print("Press Ctrl+C to exit")
print("Speak in English or Hindi - the bot will respond in the same language")

while True:
    try:
        audio, fs = record_audio(duration=10)  # Listen for up to 10 seconds
        user_text, detected_language = sarvam_stt(audio, fs)
        
        print(f"User said ({detected_language}): {user_text}")
        
        response_text = generate_rude_response(user_text.strip(), detected_language)
        
        print(f"Bot response ({detected_language}): {response_text}")
        
        audio_output, fs_output = murf_tts(response_text, detected_language)
        
        if len(audio_output) > 0:
            sd.play(audio_output, fs_output)  # Play sound through laptop speakers
            sd.wait()  # Wait until sound has finished playing
        else:
            print("No audio response generated.")
        
    except KeyboardInterrupt:
        print("\nBanker bot exiting...")
        break
    except Exception as e:
        print(f"Error in main loop: {str(e)}")