import music21

# добавить обр непереводимых значений
def midi_to_musicxml(midi_file, musicxml_file):
    midi_data = music21.converter.parse(midi_file)
    midi_data.write('musicxml', fp=musicxml_file)

def musicxml_to_pdf(musicxml_file, pdf_file):
    try:
        score = music21.converter.parse(musicxml_file)  
        us = music21.environment.UserSettings()
        if not us['musescoreDirectPNGPath']:
            musescore_path = 'c:/Program Files/MuseScore 4/bin/MuseScore4.exe'
            us['musescoreDirectPNGPath'] = musescore_path
    
        score.write('musicxml.pdf', fp=pdf_file)
        
        print(f"Successfully converted {musicxml_file} to {pdf_file}")
    except Exception as e:
        print(f"Error converting MusicXML to PDF: {str(e)}")
def remove_non_convertible_parts(midi_file, output_file):
    midi_data = music21.converter.parse(midi_file)
    filtered_stream = music21.stream.Stream()

    for part in midi_data.getElementsByClass('Stream'):
        try:
            part.write('musicxml')
            filtered_stream.append(part)
            if len(filtered_stream.getElementsByClass('Stream')) >= 2:
                break
        except music21.musicxml.xmlObjects.MusicXMLExportException:
            continue

    filtered_stream.write('midi', fp=output_file)


input_midi_file = 'C:/Users/User/Desktop/transcriber/outputs/var1.mid'
output_midi_file = 'C:/Users/User/Desktop/transcriber/outputs/processed_midi.mid'
musicxml_file = 'test_mxml.musicxml'
pdf_file = 'test_pdf.pdf'



remove_non_convertible_parts(input_midi_file, output_midi_file)
midi_to_musicxml(output_midi_file, musicxml_file)
musicxml_to_pdf(musicxml_file, pdf_file)