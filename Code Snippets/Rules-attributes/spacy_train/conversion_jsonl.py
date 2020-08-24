import json

f = open('2nd.json', 'r')
l = json.load(f)
# print(type(json.load(l)))
print(type(l))
JSON_file = l
with open('output2.jsonl', 'w') as outfile:
    for entry in JSON_file:
        json.dump(entry, outfile)
        outfile.write('\n')