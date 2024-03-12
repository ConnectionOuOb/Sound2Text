import wenet

model = wenet.load_model('chinese')
result = model.transcribe('data/input_120_part-002.wav')

print(result)
