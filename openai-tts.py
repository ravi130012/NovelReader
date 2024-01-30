from pathlib import Path
from openai import OpenAI
import os

def openai_tts(data):
  client = OpenAI(api_key='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')
  OpenAI.api_key = os.getenv('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')
  client.audio()
  
  speech_file_path = Path(__file__).parent / "speech.mp3"
  response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=data,
    
  )
  
  
  response.stream_to_file(speech_file_path)

with open("beginning_after_the_end.txt","r",encoding='utf-8') as r:
  data = r.readlines()[4]

openai_tts(data)