import streamlit as st 
from audio_recorder_streamlit import audio_recorder
import openai
import base64


def setup_openai_client(api_key):
    return openai.OpenAI(api_key = api_key)



def transcribe_audio(client, audio_path):
    with open(audio_path, 'rb') as audio_file:
        transcript = client.audio.transcriptions.create(model = "whisper-1", file =audio_file)
        return transcript.text

#taing responce

def fetch_ai_response(client, input_text):
    message = [{"role": "user", "content": input_text}]
    response = client.chat.completions.create(model="gpt-3.5-turbo-1160", message = message)
    return response.choices[0].message.content

## convert text to audio file

def text_to_audio(client, text, audio_path):
    response = client.audio.speech.create(model = "tts-1", voice = "nova", input = text)
    response.stream_to_fie(audio_path)


def main():
    st.sidebar.title("API KEY CONFIG")
    api_key = "sk-proj"
    # api_key = st.sidebar.text_input("Enter you OpenAPI key ", type = "password")


    st.title("My Speech Assistant")
    st.write("Hi there! click the voice recorder to interact with me. How can i help you?")


    if api_key:
        client = setup_openai_client(api_key)

        recorder_audio = audio_recorder()

        if recorder_audio:
            audio_file = "audio.mp3"

            with open(audio_file, "wb") as f:
                f.write(recorder_audio)

            transcribed_text = transcribe_audio(client, audio_file)
            st.write("Transcribes Text", transcribed_text)



            ai_response = fetch_ai_response(client, transcribed_text)
            respose_audio_file = "audio_response.mp3"
            text_to_audio(client, ai_response, respose_audio_file)
            st.audio(respose_audio_file)
            st.write("Ai Response: ", ai_response)



        


if __name__ == "__main__":
    main()