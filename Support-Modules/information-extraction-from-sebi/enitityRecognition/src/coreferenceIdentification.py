import neuralcoref
import os 
import spacy 

file_path = "./../../../../data/HTML_TO_TEXT_UNCLEANED/"
files = os.listdir(file_path)

nlp = spacy.load('en') 
neuralcoref.add_to_pipe(nlp) 

def getIndexMapping(text):
  startIndex = []
  indexTrack = 0
  for i in range(len(text)):
    startIndex.append(indexTrack)
    indexTrack += (len(text[i]))
    indexTrack +=1
  return startIndex


files = os.listdir('./../outputs/cleaned/')
files = [i for i in files if i[-5:] == ".json"]
from tqdm import tqdm
import json
def getIndexMapping(text):
  startIndex = []
  indexTrack = 0
  for i in range(len(text)):
    startIndex.append(indexTrack)
    indexTrack += (len(text[i]))
    indexTrack +=1
  return startIndex

file_path = './../outputs/cleaned/'
for file in files:
  data = json.load(open(file_path + file))
  data1 = []
  for i in data:
    data1.append(data[i]['text'])
  ents1 = []
  for i in tqdm(range(len(data1)-10)):
    text = '\n'.join(data1[i:i+10])
    doc = nlp(text)
    ents1.append(doc)
  coref = [[] for i in (data1)]
  for i in (range(len(data)-10)):
    lineMapping = getIndexMapping(data1[i:i+10])
    lineWiseSplit = [[] for i in range(10)]
    for cluster in ents1[i]._.coref_clusters:
      for mention in cluster.mentions:
        sc,ec,ct,mt = (mention.start_char,mention.end_char,mention.text,cluster.main)
        line = lineMapping[0]
        lineIndex = 0
        broken = False
        for line in lineMapping:
          if line > sc:
            break
          lineIndex +=1
        if '\n' in ct:
          ct = ct.split('\n')[0]
          ec = sc + len(ct)
        lineWiseSplit[lineIndex-1].append((sc-lineMapping[lineIndex-1],ec-lineMapping[lineIndex-1],ct,str(mt).strip()))
    c = 0
    for line in lineWiseSplit:
      for cc in line:
        # print(c+i)
        if(data1[i+c][cc[0]:cc[1]]!=cc[2].strip()):
          print('A:',data1[i+c][cc[0]:cc[1]])
          print('D:', cc[2], 'M:',cc[0],cc[1],c+i, i)
          input()

        coref[c+i].append(cc)
      c+=1
    coref = [list(set(i)) for i in coref]
    for i in range(len(data)):
      data[str(i)]['coref'] = coref[i]
    with open('./../outputs/CoRef/'+file,'w') as handle:
      json.dump(data,handle)

  
      





  
      
