import spacy
import json
from tqdm import tqdm
from spacy import displacy
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

result = []
nlp = spacy.load("en_core_web_sm")
for line in data:
	# print(line)
	doc = nlp(line)
	for token in doc.ents:
		# print(token.text, token.lemma_, token.pos_)
		result.append((token.text, token.label_))
		print((token.text, token.label_))

		# displacy.serve(doc, style="dep")
	print('***************************************************************************************************************************************')

# for token in result:
# 	if((token[0] == 'shall') or (token[0] == 'may') or (token[0] == 'would')):
# 		result.remove(token) 
# for token in result:
# 	if token[2] == 'VERB':
# 		print(token[0])
# # Write data to file 
# file_name = output_file_path + 'output'
# with open(file_name,'w') as handle:
#     json.dump(output, handle)

# for k in output.keys():
# 	print(k)
# 	print(output[k])