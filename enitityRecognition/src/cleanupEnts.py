import os
import spacy 
import json
from tqdm import tqdm

nlp = spacy.load('en')
file_path = './../outputs/nerOutputs/'

files = os.listdir(file_path)

for file_name in tqdm(files):
  file = json.load(open(file_path+file_name))
  for i in (file):
    doc = nlp(file[i]['text'])
    parsedData = []
    for j in doc:
      parsedData.append([j.text,j.pos_])
    file[i]['parsed_data'] = parsedData
    file[i]['nounChunks'] = {np.text
    for nc in doc.noun_chunks
    for np in [
      nc,
      doc[
        nc.root.left_edge.i
        :nc.root.right_edge.i+1]]}
    file[i]['nounChunks'] = [i.strip() for i in file[i]['nounChunks']]

  for i in (file):
    cleanedUpEnts = []
    for ent in file[i]['ents']:
      if ent in file[i]['nounChunks']:
        cleanedUpEnts.append(ent)
    for ent in file[i]['ents']:
      if ent not in cleanedUpEnts:
        bigB = ent
        marked = False
        for maybeEnt in file[i]['nounChunks']:
          if ent in maybeEnt:
            if bigB in maybeEnt:
              if len(maybeEnt.split()) - len(ent.split()) < 5:
                if len(maybeEnt.split()) > len(bigB.split()):
                  bigB = maybeEnt
                  marked = True
        if marked:
          cleanedUpEnts.append(bigB)
    file[i]['cleanedUpEnts'] = cleanedUpEnts
  with open('./../outputs/cleaned/' + file_name, 'w') as handle:
    json.dump(file,handle)

  



