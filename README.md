# subs-audio-splicer
A python lib aimed at providing an easy way to create audio segments that match a given dialogue in a subtitles file. 

### Parser ###
The `Parser` class takes a subtitles file (currently supports `.ass` and `.srt` formats) as single argument and provides a `get_dialogues([str filename])` method to extract all dialogues from the subs file. 
``` python
from subs_audio_splicer import Parser

parser = Parser('subtitles.ass')
for dialogue in parser.get_dialogues() # Returns a list of Dialogue objects
  print dialogue.text  #'素晴らしいですね！'
  print dialogue.start # 5500 
  print dialogue.end   # 6700
```
### Splicer ###
The `Splicer`class takes an audio file (currently only mp3 is supported) as single argument and provides a `get_audio_for([Dialogue dialogue], [str output_file])` method that cuts a segment of the audio file according to the `start` and `end` properties of the `Dialogue` object passed to it. It then saves the audio segment as a new file with the name passed in the second `[str output_file]` argument. 
Note: The method automatically appends the corresponding file extension upon creating the file. The given `[str output_file]` should be in the form of `my_file` and not `my_file.mp3`

``` python
from subs_audio_splicer import Splicer, Parser

parser, splicer = Parser('subs.ass'), Splicer('audio.mp3')

# In this example we're only going to get the audio
# for dialogues #3 and #4
dialogues = parser.get_dialogues()[3:5]

for dialogue in dialogues:
	# Let's use the dialogue's text separated by '_'
	# as filename for the audio segment
	filename = '_'.join(dialogue.text.split(' '))
	splicer.get_audio_for(dialogue, filename)

```
