import whisper

model = whisper.load_model('base')
result = model.transcribe('ReuGF.mp3')
print(result['text'])

API_KEY = ''