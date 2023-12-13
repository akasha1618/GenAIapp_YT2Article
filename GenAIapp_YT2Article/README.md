 YouTube Video to SEO Article Writer\Generator

This project is a web application that generates an article based on the content of a YouTube video. The user enters the URL of a YouTube video, and the application downloads the video, transcribes the audio to text using OpenAI's Whisper API, and generates an article with specific SEO keywords using the LangChain framework.

## Features

- Download YouTube videos using pytube
- Transcribe audio to text using OpenAI's Whisper API
- Generate an article based on the video content using LangChain

## Prerequisites

- Python 
- pip

## Installation

1. Clone the repository: `git clone https://github.com/akasha1618/GenAIapp_YT2Article.git`
2. Navigate to the project directory: `cd yourrepository`
3. Install the dependencies: `pip install -r requirements.txt`

## Configuration

Create a `.env` file in the root directory of the project, and add the following line:

OPENAI_API_KEY=your_openai_api_key

Replace `your_openai_api_key` with your actual OpenAI API key.

## Usage

1. Start the server: `python app.py`
2. Open your web browser and navigate to `http://localhost:5000`
3. Enter the URL of a YouTube video and click the "Write Article" button

## Technologies Used

- Python
- Flask
- OpenAI Whisper API
- LangChain
- pytube
- OpenAI gpt-4-turbo

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

