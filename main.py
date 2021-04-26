import json
import os
#entries: user_name, game_id, score,id
game_2048 = []
game_2018 = []
game_sketch = []

with open('entries.json') as f:
  entries = json.load(f)

for entry in entries:
  new_entry = [entry[3], entry[0], entry[2]]
  if(entry[1]==1):
    game_2048.append(new_entry)

  if(entry[1]==2):
    game_2018.append(new_entry)

  if(entry[1]==3):
    game_sketch.append(new_entry)

game_2048.sort(key=lambda x: x[2])
game_2048.reverse()
game_2018.sort(key=lambda x: x[2])
game_2018.reverse()
game_sketch.sort(key=lambda x: x[2])
game_sketch.reverse()

if(os.path.exists("leaderboard.json")):
  os.remove("leaderboard.json")

with open('leaderboard.json', 'a') as file:
  file.write('[\n\n')

game_list = [game_2048, game_2018, game_sketch]
game_strings = ["2048", "Google Doodle 2018", "sketchful.io"]
for game_id in range(3):
  game = game_list[game_id]
  gs = game_strings[game_id]
  with open('leaderboard.json', 'a') as file:
    file.write("\"{}\"\n".format(gs))
    file.write("[\"submission_id\", \"user_name\", \"score\"]\n")
  if(len(game)==0):
    with open('leaderboard.json', 'a') as file:
      file.write('[\n\n],\n\n')
  for i in range(len(game)):
      entry = game[i]
      with open('leaderboard.json', 'a') as file:
        if(i==0):
          file.write('[\n')
        file.write(json.dumps(list(entry)))
        if(i!=len(game)-1):
          file.write(",\n")
        else:
          file.write("\n],\n\n")
      

with open('leaderboard.json', 'a') as file:
  file.write('\n]')
