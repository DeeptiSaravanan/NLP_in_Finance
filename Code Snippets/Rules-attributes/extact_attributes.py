import spacy
import json
from tqdm import tqdm

# Load Spacy NER model 
# nlp = spacy.load('models/sebi_ib')

with open('insider_rule_dump.json') as f:
	data = json.load(f)

# output = {}
# lineNumber = 0
# for line in data:
#     doc = nlp(line)
#     ents = []
#     entlabels = []
#     for ent in doc.ents:
#         ents.append(ent.text)
#         entlabels.append(ent.label_)
#     output[lineNumber] ={}
#     output[lineNumber]['text'] = line
#     output[lineNumber]['ents'] = ents
#     output[lineNumber]['ent_labels'] = entlabels
#     lineNumber += 1


nlp = spacy.load("en_core_web_sm")
for line in data:
	print(line)
	doc = nlp(line)
	for token in doc:
		print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
	print('***************************************************************************************************************************************')
# # Write data to file 
# file_name = output_file_path + 'output'
# with open(file_name,'w') as handle:
#     json.dump(output, handle)

# for k in output.keys():
# 	print(k)
# 	print(output[k])