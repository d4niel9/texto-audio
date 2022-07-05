from gtts import gTTS
import pathlib
import shutil
from playsound import playsound

path = pathlib.Path().absolute()
texto = input('text to convert -> ')
name_file = input('name file -> ') + '.mp3'

def archivo(path, texto, name_file):
    audio = gTTS(texto, lang='es', tld='es')
    audio.save(name_file)
    path = str(path) + '/outputfile/'
    shutil.move(archivo, path)
    path += name_file
    playsound(path)
    print('playing audio ' + path)

archivo(path=path, texto=texto, name_file=name_file)
