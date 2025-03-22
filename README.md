# 🤖 AI Assistant with Voice

An interactive web-based AI assistant application that combines Google's Gemini AI for text generation and Sarvam AI for speech-to-text and text-to-speech capabilities in multiple Indian languages.

[![AI Assistant with Voice Interface](https://raw.githubusercontent.com/AdityaAjithKumar/Genesis_Personalised_AI/main/Screenshot%202025-03-22%20100238.png)](https://genesis-personalised-ai.vercel.app/)

## 🎬 Demo Video

Check out the demo video to see the application in action:

[![Demo Video](https://raw.githubusercontent.com/AdityaAjithKumar/Genesis_Personalised_AI/main/Screenshot%202025-03-22%20100238.png)](https://www.dropbox.com/scl/fi/k6q1l8vxiicwwyisx2eih/Screen-Recording-2025-03-22-092147.mp4?rlkey=01y1b5uaaruexole1vh7gez8o&st=1qqg680a&dl=0)

[Download Demo Video](https://www.dropbox.com/scl/fi/k6q1l8vxiicwwyisx2eih/Screen-Recording-2025-03-22-092147.mp4?rlkey=01y1b5uaaruexole1vh7gez8o&st=1qqg680a&dl=1)

## ✨ Features

- 💬 **Text-based chat** with Gemini AI's powerful language model
- 🎙️ **Voice input** through Sarvam AI's advanced speech recognition
- 🔊 **Voice output** through Sarvam AI's natural-sounding text-to-speech
- 🌏 **Multilingual support** for 11 Indian languages
- 📊 **Real-time audio visualization** with dynamic waveform display
- 💾 **Local storage** for securely saving your API keys and preferences
- 🎨 **Responsive design** that works beautifully on desktop and mobile devices
- 🌙 **Dark mode support** that automatically follows your system preferences

## 🌐 Live Demo

Try it now: [Genesis Personalised AI](https://genesis-personalised-ai.vercel.app/)

[![Deploy with Vercel](https://vercel.com/button)](https://genesis-personalised-ai.vercel.app/)

## 🗣️ Supported Languages

- 🇮🇳 English (en-IN)
- 🇮🇳 Hindi (hi-IN)
- 🇮🇳 Bengali (bn-IN)
- 🇮🇳 Gujarati (gu-IN)
- 🇮🇳 Kannada (kn-IN)
- 🇮🇳 Malayalam (ml-IN)
- 🇮🇳 Marathi (mr-IN)
- 🇮🇳 Odia (or-IN)
- 🇮🇳 Punjabi (pa-IN)
- 🇮🇳 Tamil (ta-IN)
- 🇮🇳 Telugu (te-IN)

## 🚀 Getting Started

### Prerequisites

To use this application, you'll need:

1. 🔑 A **Gemini AI API key** from [Google AI Studio](https://makersuite.google.com/)
2. 🔑 A **Sarvam AI API key** from [Sarvam AI](https://sarvam.ai/)

### Installation

1. 📥 Clone this repository or download the source code
   ```bash
   git clone https://github.com/AdityaAjithKumar/Genesis_Personalised_AI.git
   ```
2. 📂 Open the `index.html` file in your web browser
3. ⚙️ Enter your API keys in the settings panel
4. 🌍 Select your preferred language
5. 💾 Click "Save Settings"

### Usage

#### Text Chat
1. ⌨️ Type your message in the input box
2. 📤 Press Enter or click the send button to send your message
3. 🤖 The AI will respond with text and audio

#### Voice Chat
1. 🎙️ Click the microphone button to start recording
2. 🗣️ Speak your message
3. 🛑 Click the microphone button again to stop recording
4. 📝 Your speech will be transcribed and sent to the AI
5. 🔊 The AI will respond with text and audio

## 🔒 Privacy and Security

- 🔐 All API keys are stored locally in your browser's localStorage
- 🎤 Audio processing occurs on Sarvam AI's servers
- 💬 Text processing occurs on Google's Gemini AI servers

## 🛠️ Technical Details

This application is built with:

- 📄 HTML5 for structure
- 🎨 CSS3 for styling with modern design principles
- ⚡ JavaScript (ES6+) for interactive functionality
- 🔊 Web Audio API for audio visualization
- 🎙️ MediaRecorder API for audio recording
- 🌐 Fetch API for communication with Gemini and Sarvam AI

## 🧩 API Usage

### Gemini AI
The application uses the Gemini 2.0 Flash model for text generation. It maintains a conversation history to provide context-aware responses.

### Sarvam AI
The application uses:
- 🎤 **Saarika v2** model for speech-to-text conversion
- 🔊 **Bulbul v1** model for text-to-speech conversion

## 🎨 Customization

You can customize the application by modifying:
- 🎭 CSS variables in the `:root` selector to change colors
- 📝 Font styles and sizes
- 📏 Layout dimensions

## ❓ Troubleshooting

Common issues:
- 🎙️ **Microphone not working**: Ensure you've granted microphone permissions in your browser
- 🔑 **API errors**: Verify your API keys are correct and have sufficient quota
- 🔇 **No speech detected**: Speak clearly and ensure your microphone is working properly

## 📜 License

This project is released under the MIT License. See the LICENSE file for details.

## 👏 Acknowledgments

- 🙏 Google Gemini AI for text generation capabilities
- 🙏 Sarvam AI for speech-to-text and text-to-speech capabilities
- 🙏 Material Icons for the user interface icons
- 🙏 Vercel for hosting the live demo
