# subs-audio-splicer
A python lib aimed at providing an easy way to create audio segments that match a given dialogue in a subtitles file. 

### Parser ###
The `Parser` class takes a subtitles file (currently supports `.ass` and `.srt` formats) as single argument and provides a `get_dialogues()` method to extract all dialogues from the subs file. 
``` python
from subs_audio_splicer import Parser

parser = Parser('subtitles.ass')
for dialogue in parser.get_dialogues() # Returns a list of Dialogue objects
  print dialogue.text  #'素晴らしいですね！'
  print dialogue.start # 5500 
  print dialogue.end   # 6700
```

To be continued.
