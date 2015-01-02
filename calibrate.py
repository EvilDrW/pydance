import dance
from constants import *

latencyMeasurement = 0

# This judge is used to adapt the offset from the config file to the latency 
# of the system that we're playing on (TV, sound system, etc.)

def run(screen):
  # here's the signature for dance.play from dance.py
  # def play(screen, playlist, configs, songconf, playmode):

  # playlist is a list of (song_filename, song_diff)
  filename = os.path.join(sound_path, "calibration/calibrate.dance")
  mode = "SINGLE"
  diff = "BASIC"
  
  # store some configurations that we need to temporarily subvert...
  temp = { 'judge': game_config['judge'],
           'secret': game_config['secret'],
           'grading': mainconfig['grading'] }
  
  # use CalibrationJudge, make hidden arrows invisible, and don't show the grading screen
  game_config.update({ 'judge': 2, 'secret': 1 })
  mainconfig['grading'] = False
  
  mainconfig['masteroffset'] = 0
  
  dance.play(screen, [(filename, [diff])], [player_config], game_config, mode)
  
  print "New master offset: " + str(mainconfig['masteroffset'])
  
  # restore original settings
  mainconfig['grading'] = temp['grading']
  for x in [ 'secret', 'judge' ]:
    game_config[x] = temp[x]
  