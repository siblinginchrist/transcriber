from music21 import ConverterMusicXML, environment
import os

# b = corpus.parse('bach/bwv66.6')
# b.show() 

os.chdir('C:/Users/User/Desktop/transcriber')
environment.set('musicxmlPath', 'c:/Program Files/MuseScore 4/bin/MuseScore4.exe')
midi_file = ConverterMusicXML.parse('C:/Users/User/Desktop/transcriber/outputs/MBRFIN.mid')
musicxml_file = midi_file.write('musicxml', 'output_file.xml')
midi_file.show()