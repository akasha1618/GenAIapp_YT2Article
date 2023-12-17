from openai import OpenAI
import whisper
import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.agents import AgentType
from langchain.agents import load_tools, initialize_agent
from langchain.agents import tool
import tiktoken
from pytube import YouTube
from moviepy.editor import *
from flask import Flask, redirect, url_for, request, render_template, send_file
import requests

#OpenAI initialization
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI()

#load the prompt from file
with open("prompt_article", "r") as file:
    prompt_article = file.read()


app = Flask(__name__)


#Downoad the article with Pytube, get the title, audio from the video and use Whisper from OpenAI to get the transcript from the audio
def download_and_transcribe(url):

    yt = YouTube(url)

    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    sanitized_title = yt.title.replace(" ", "_")

    audio_stream.download('.', filename=sanitized_title + '.webm')
    file_name = f'{sanitized_title}.webm'
    with open(file_name, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
    return transcript  

#generate the article with Langchain 
def generate_article_from_transcript(transcript):
    prompt =prompt_article
    llm = ChatOpenAI(temperature=0.0, model='gpt-4-1106-preview')
    prompt_template = ChatPromptTemplate.from_template(prompt)
    chain = LLMChain(llm=llm, prompt=prompt_template)
    return chain.run(transcript)

#route for the initial index page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


#route for the generation result page
@app.route('/generate-article', methods=['POST'])
def generate_article():
    youtube_link = request.form['youtube_link']
    transcription = download_and_transcribe(youtube_link)
    generated_article = generate_article_from_transcript(transcription)
    #save article to file
    filename = "article.txt"
    with open(filename, 'w') as file:
        file.write(generated_article)

    return render_template('result.html', article=generated_article)

#route for downloading the generated article
@app.route('/download-article', methods=['GET'])
def download_article():
    return send_file("article.txt", as_attachment = True)
   
if __name__ == '__main__':
    app.run(debug=True)





