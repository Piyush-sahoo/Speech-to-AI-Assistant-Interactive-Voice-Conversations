# Speech-to-AI Assistant: Interactive Voice Conversations

## Overview
The **Speech-to-AI Assistant** is a Streamlit-based application that enables users to interact with AI through voice. Users can record their speech, which is transcribed, processed by OpenAI's GPT models, and then responded to with synthesized speech.

## Features
- **Voice Input**: Record audio directly within the app using the audio recorder feature.
- **Speech-to-Text**: Transcribe user speech into text using OpenAI's Whisper model.
- **AI Interaction**: Generate AI responses using OpenAI's GPT models.
- **Text-to-Speech**: Convert AI-generated responses back into audio for seamless interaction.
- **Streamlit UI**: Simple and interactive web interface for real-time communication.

## Requirements
Ensure you have the following installed before running the application:

- Python 3.8 or higher
- Required Python libraries (listed in `requirements.txt`):
  - Streamlit
  - OpenAI
  - audio_recorder_streamlit

## Installation
1. Clone this repository or download the project files.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
