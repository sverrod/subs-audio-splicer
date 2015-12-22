
from pydub import AudioSegment
from parser import Parser

class Splicer:
	def __init__(self, audio_file):
		self.audio = audio_file
		self.audio_format = self.audio.split('.')[1]

	def get_audio_for(self, dialogue, output_file):
		if self.audio_format == 'mp3':
			audio = AudioSegment.from_mp3(self.audio)
		start = dialogue.start
		end = dialogue.end
		audio_segment = audio[start:end]	
		#print start, end
		audio_segment.export(output_file+'.'+self.audio_format, format='mp3')		
