import json
import os
import nltk
import spacy
from operator import itemgetter
import itertools
import random
import Levenshtein
import difflib
import pickle
def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
def depickle(file):
    file = open(file, 'rb')
    data = pickle.load(file)
    file.close()
    return data
def load_json_file(file):
    with open(file) as f:
        data = json.load(f)
    return data

def similarity_between_rules(r, verbose =True):
    s1 = r[0]
    s2 = r[1]
#     s1 = tag_words(rule1)
#     s2 = tag_words(rule2)
    s = difflib.SequenceMatcher(None, s1, s2)
    verbose_list = []
    if verbose:
        for tag, i1, i2, j1, j2 in s.get_opcodes():
            verbose_list.append((tag, s1[i1:i2], s2[j1:j2]))
    return (verbose_list,s.ratio())

def get_score_only(s1,s2,verbose=False):
    s = difflib.SequenceMatcher(None, s1, s2)
    verbose_list = []
    if verbose:
        for tag, i1, i2, j1, j2 in s.get_opcodes():
            verbose_list.append((tag, s1[i1:i2], s2[j1:j2]))
    return s.ratio()


def rSubset(arr, r): 
    return list(itertools.combinations(arr, r))

def tag_words(s):
    nlp = spacy.load("en_core_web_sm")
    output_dir = 'my_mixed_random/'
    nlp2 = spacy.load(output_dir)
    ent_list = []
    doc2 = nlp2(s)
    for ent in doc2.ents:
        ent_list.append({'label':ent.label_, 'start':ent.start, 'end':ent.end})
    doc = nlp(s)
    for token in doc:
        ent_list.append({'label':token.pos_, 'start':token.idx, 'end': token.idx+len(token.text)})
    ent_list = sorted(ent_list,
                          key=lambda k: (k['start']))
    sign_list = []
    for tag in ent_list:
        sign_list.append(tag['label'])
    return sign_list


import random
import networkx as nx
#pass a dictionary consisting of rules and tag signs as values.
def clustering_sentences(sentence_dict, threshold):
    clusters = []
    remaining_rules = list(sentence_dict.keys())
    while(len(remaining_rules)!=0):
        seed_rule = random.choice(remaining_rules)
        #initial values.
        cluster = [seed_rule]
#         print(seed_rule+"8888888888")
#         remaining_rules = list(sentence_dict.keys())
        remaining_rules.remove(seed_rule)
        #make a cluster grow its optimal size.
        #keep doing until size of cluster remains unchanged.
        old_size = 1
        new_size = 100
        while (new_size>old_size):
            old_size = len(cluster)
#             print(local_similarity)
            local_similarity = {}
            for k in remaining_rules:
                for r in cluster:
                    if (k,r) not in local_similarity.keys():
                        local_similarity[(k,r)] = get_score_only(sentence_dict[k],sentence_dict[r])
            add_to_cluster = {k[0]:v for (k,v) in local_similarity.items() if v >= threshold}
            remaining = {k[0]:v for (k,v) in local_similarity.items() if v < threshold}
            cluster.extend(add_to_cluster.keys())
            cluster = list(set(cluster))
            remaining_rules = remaining.keys()
            remaining_rules = list(set(remaining_rules))
            new_size = len(cluster)
            new_clusters = []
            #updating clusters midway for efficient transactions.
            for clu in clusters:
                if clu!= cluster:
                    if set(clu).intersection(set(cluster)):
                        cluster.extend(clu)
#                         new_clusters.append(cluster)
                    else:
                        new_clusters.append(clu)
            clusters = new_clusters
                        
#             print(new_size)
        print(cluster)
        clusters.append(cluster)
    #merging clusters if they consist of the same elements.
    print(clusters)
    L = clusters
    G = nx.Graph()    
    G.add_nodes_from(sum(L, []))
    q = [[(s[i],s[i+1]) for i in range(len(s)-1)] for s in L]
    for i in q:
        G.add_edges_from(i)
    clusters = [list(i) for i in nx.connected_components(G)]
    return clusters
    

# r1 = '43.In order to remove any difficulties in respect of the application or interpretation of these regulations, the Board may issue clarifications or guidelines in the form of circulars.'
# r2 = '27.In order to remove any difficulties in the interpretation or application of the provisions of these regulations, the Board may issue clarifications or guidelines from time to time.'
# print(r1)
# print(r2)
# similarity_between_rules((r1,r2))[1]

rule_tag_dict = depickle('all_rules_all_annotations.pkl')
sentence_dict = {}
for rule in rule_tag_dict:
    if len(rule)>30 and ('Page' not in rule) and ('Amendment' not in rule) and ('.....' not in rule) and('…………' not in rule):
        sentence_dict[rule] = [k['label'] for k in rule_tag_dict[rule]]
        print(rule)
print(len(sentence_dict))
# print(sentence_dict.keys())

cluster060= clustering_sentences(sentence_dict, 0.60)
save_object(cluster060, 'cluster060')


