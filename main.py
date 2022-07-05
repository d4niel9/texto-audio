from gtts import gTTS
import shutil
import pathlib
from playsound import playsound

path = pathlib.Path().absolute()
name_file = input('name file') + '.mp3'
texto = 'Soy el texto convertido en audio'

def archivo(path, name_file, texto):
    audio = gTTSS(texto, lang='es', tld='es')
    audio.save(name_file)
    path = str(path) + '/outputfile/'
    shutil.move(archivo, path)
    path += name_file
    playsound(path)
    print('reproduciendo audio ' + path)

archivo(path=path, name_file=name_file, texto=texto)
