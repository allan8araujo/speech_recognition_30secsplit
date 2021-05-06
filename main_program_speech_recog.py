import speech_recognition as sr

text = ''
audio_file = sr.AudioFile('{FILENAME.WAV}')
with audio_file as source:
    audio_file_duration = audio_file.DURATION

'''numbers of division of a audio'''

if audio_file_duration >= 30:
    audio_file_division = audio_file_duration / 30
    n_parts = int(f'{audio_file_division:.0f}') + 1
else:
    n_parts = 1
print(n_parts)
'''----------'''


def function_audio_import():
    global text
    global audio_file_duration


    audio_wav = sr.Recognizer()

    with audio_file as source_kek:
        audio_wav.dynamic_energy_threshold = True
        audio_wav.adjust_for_ambient_noise(source_kek)
        audio_record_1 = audio_wav.record(source_kek)
        for n in range(0, n_parts):
            audio_record = audio_record_1.get_segment(n * 30000, (n + 1) * 30000)
            try:
                phrase = audio_wav.recognize_google(audio_record, language='pt-br')
                text =text + str(phrase) + '\n'
            except sr.UnknownValueError:
                f'deu erro na frase número {n_parts}'
                print('erro e fodase')
    print(text)


function_audio_import()
