import os
import spacy 
import json
from tqdm import tqdm

# Load data 
import en_core_web_sm
nlp = en_core_web_sm.load()

file_path = './../outputs/nerOutputs/'

files = os.listdir(file_path)

visited = []
def mergeEntsFromNounChunks(ent, nounChunks, startPos):
#     print(ent,nounChunks[startPos])
    visited.append([ent,startPos])
    curCount = startPos
    bigB = ent
    marked = False
    possibleAns = []
    for maybeEnt in nounChunks[startPos:]:
        if ent in maybeEnt:
            if bigB in maybeEnt:
                if len(maybeEnt.split()) - len(ent.split()) < 5:
                        if len(maybeEnt.split()) > len(bigB.split()):
                            bigB = maybeEnt
                            marked = True
            else:
#                 print("started", ent, curCount)
                if( [ent,curCount] not in visited):
                    possibleAns = mergeEntsFromNounChunks(ent,nounChunks,curCount)
        curCount +=1
        
    if marked:
        possibleAns.append(bigB)
#     print(possibleAns)
    return possibleAns
                            
  
for file_name in tqdm(files):
  file = json.load(open(file_path+file_name))
  for i in (file):
    doc = nlp(file[i]['text'])
    parsedData = []
    
    # Parse Data
    for j in doc:
      parsedData.append([j.text,j.pos_])
    file[i]['parsed_data'] = parsedData
    
    # Get noun chunks
    file[i]['nounChunks'] = {np.text
    for nc in doc.noun_chunks
    for np in [
      nc,
      doc[
        nc.root.left_edge.i
        :nc.root.right_edge.i+1]]}
    file[i]['nounChunks'] = [i.strip() for i in file[i]['nounChunks']]

  # Cleanup entities 


                            
                
    
  for i in (file):
    cleanedUpEnts = set()
    for ent in file[i]['ents']:
      if ent in file[i]['nounChunks']:
        cleanedUpEnts.add(ent)
    
    # Merge noun chunks 
    nounChunks = file[i]['nounChunks']
    visited = []
    for ent in file[i]['ents']:
      cEnts = mergeEntsFromNounChunks(ent, nounChunks, 0)
      for cEnt in cEnts:
        cleanedUpEnts.add(cEnt)
    file[i]['cleanedUpEnts'] = list(cleanedUpEnts)
  
  # Write Data 
  
  with open('./../outputs/cleaned/' + file_name, 'w') as handle:
    json.dump(file,handle)

  



