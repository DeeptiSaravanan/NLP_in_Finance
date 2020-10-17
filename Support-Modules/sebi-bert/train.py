# imports 
import logging
import os 
import spacy

from simpletransformers.language_modeling import (
    LanguageModelingModel,
    LanguageModelingArgs,
)

# logging 
logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

DATA_DIR = "./../../data/sebi-bert-data/"
SEBI_TEXT_FILES = DATA_DIR + "SEBI Text Files/"
IK_FILES = DATA_DIR + "IndianKanoon Text Files/"
SEBI_REG_MERGE = DATA_DIR + "sebi_regulations.txt"

# BERT Args 12 Layer 12 head model 
model_args = LanguageModelingArgs()
model_args.reprocess_input_data = True
model_args.overwrite_output_dir = True
model_args.num_train_epochs = 2
model_args.dataset_type = "simple"

# Some files are parsed as a single line, thus inorder to process them we will need to increase
# the size of the spacy buffer. 
nlp = spacy.load('en')
nlp.max_length = 100000000


# Sentence segementation for the documents.

print("Began sentence segmentation")

sebi_regs  = open(SEBI_REG_MERGE).read()
doc = nlp(sebi_regs)
sebi_regs = [sentence.text for sentence in doc.sents]
print("Sebi done")

sebi_files = os.listdir(SEBI_TEXT_FILES)
concat_sebi_files = []
for i in sebi_files:
  d = open(SEBI_TEXT_FILES + i).read()
  doc = nlp(d)
  dd = [sentence.text for sentence in doc.sents] 
  concat_sebi_files += dd
print("Sebi v2 done")

india_kanoon_files = os.listdir(IK_FILES)
concat_ik = []
for i in india_kanoon_files:
  d = open(IK_FILES+ i).read()
  doc = nlp(d)
  dd = [sentence.text for sentence in doc.sents] 
  dd = [sentence.text for sentence in doc.sents] 
  concat_ik += dd
print("india kanoon done")

# Merge all the training data so far
train_file = sebi_regs + concat_sebi_files + concat_ik
with open('train_file.txt','w') as handle:
  for i in train_file:
    line = " ".join(i.split())
    handle.write(line)
    handle.write("\n")
train_file = 'train_file.txt'

# Define BERT Model, currently using the cased version of bert 
model = LanguageModelingModel(
    "bert", "bert-base-cased", args=model_args
)

# Train the model
model.train_model(train_file)

# Model will be found at ./outputs/


# Evaluate the model
# result = model.eval_model(test_file)
