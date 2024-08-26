import os
from music21 import converter, environment

us = environment.UserSettings()
us['musescoreDirectPNGPath'] = 'C:/Program Files/MuseScore 4/bin/MuseScore4.exe'

def mp3_to_midi(file_path):
    # добавить magenta
    score = converter.parse(file_path)
    midi_path = file_path.rsplit('.', 1)[0] + '.mid'
    score.write('midi', fp=midi_path)
    return midi_path

def midi_to_pdf(midi_file):
    score = converter.parse(midi_file)
    pdf_path = midi_file.rsplit('.', 1)[0] + '.pdf'
    score.write('musicxml.pdf', fp=pdf_path)
    return pdf_path

def midi_to_musicxml(midi_file):
    score = converter.parse(midi_file)
    xml_path = midi_file.rsplit('.', 1)[0] + '.xml'
    score.write('musicxml', fp=xml_path)
    return xml_path

def process_file(file_path, output_format):
    midi_path = mp3_to_midi(file_path)
    if output_format == 'midi':
        return midi_path
    elif output_format == 'pdf':
        return midi_to_pdf(midi_path)
    elif output_format == 'musicxml':
        return midi_to_musicxml(midi_path)