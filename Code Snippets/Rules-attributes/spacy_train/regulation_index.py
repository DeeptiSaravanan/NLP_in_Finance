with open('insider_rule_dump.json') as f:
    data = json.load(f)
import re
#The following functions are used to index the documents is order and combine them chapter wise.
p = re.compile(r'^(\(\d\)|\(\d\d\))')
new_data = []
int_list = []
for k in range(len(data)):
    int_list.append(data[k])
    if k+1<len(data):
        if not p.findall(data[k+1]):
            pass
        else:
            new_data.append(''.join(map(str, int_list)))
            int_list = []

for line in new_data:
    p = re.compile(r'^(\(\d\)|\(\d\d\))')

reg_data = []
chap_list = []
for k in range(len(new_data)):
    chap_list.append(new_data[k])
    if k+1<len(new_data):
        if p.findall(new_data[k+1])[0][1]=='1':
            reg_data.append(chap_list)
            chap_list = []
reg_dict = {}
#reg_dict is a dictionary of rules with keys as chapter numbers and values as list of ordered rules(strings).
count = 0
for k in reg_data:
    rules_dict = {}
    for i in k:
        rules_dict[p.findall(i)[0][1]] = i 
    count +=1
    reg_dict[count] = rules_dict

# print(reg_dict)