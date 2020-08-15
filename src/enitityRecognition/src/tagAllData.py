import os
import json
import spacy

from tqdm import tqdm

# Load Data 
file_path = './../../../data/HTML_TO_TEXT_UNCLEANED/'
output_file_path = './../outputs/nerOutputs/'
files = os.listdir(file_path)

# Load Spacy NER model 
nlp = spacy.load('./../models/sebi_ib')

# Iterate thorugh the files and tag data 
for file in tqdm(files):
    with open(file_path+file) as handle:
        data = handle.read().splitlines()
    output = {}
    lineNumber = 0
    for line in data:
        doc = nlp(line)
        ents = []
        entlabels = []
        for ent in doc.ents:
            ents.append(ent.text)
            entlabels.append(ent.label_)
        output[lineNumber] ={}
        output[lineNumber]['text'] = line
        output[lineNumber]['ents'] = ents
        output[lineNumber]['ent_labels'] = entlabels
        lineNumber += 1

    # Write data to file 
    file_name = output_file_path + file[:-7] + 'json'
    with open(file_name,'w') as handle:
        json.dump(output, handle)


        
