# -*- coding: utf-8 -*-
from dialogue import Dialogue
import ass, pysrt

class Parser:
	def __init__(self, subs):
		self.subs = subs
		self.subs_format = subs.split('.')[1]

	def get_dialogues(self):

		if self.subs_format == 'ass':
			f = open(self.subs, 'r')
			subs = ass.parse(f)
			return [Dialogue(event.text, self.to_ms(event.start), self.to_ms(event.end)) for event in subs.events]
		
			
		elif self.subs_format == 'srt':
			subs = pysrt.open(self.subs)
			return [Dialogue(sub.text, self.to_ms_srt(sub.start), self.to_ms_srt(sub.end)) for sub in subs]


	def to_ms(self, time):
		return int(time.total_seconds() * 1000)

	# Pysrt is stupid and doesn't return a deltatime object so we have to convert everything manually
	def to_ms_srt(self, time):
		hours, minutes, seconds, milliseconds = time.hours, time.minutes, time.seconds, time.milliseconds
		return 36000000 * hours + 60000 * minutes + 1000 * seconds + milliseconds
	