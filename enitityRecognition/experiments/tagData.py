import os
import json
import spacy

from tqdm import tqdm

file_path = './'
output_file_path = './'
files = ['./insider_rule_dump.json']

nlp = spacy.load('./../models/sebi_ib')


for file in tqdm(files):
    with open(file_path+file) as handle:
        data = json.load(handle)
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
    file_name = output_file_path + file[:-7] + 'json'
    with open(file_name,'w') as handle:
        json.dump(output, handle)


        
