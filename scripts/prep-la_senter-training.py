# For 'prep' script, cf. https://github.com/explosion/spaCy/discussions/6926

import spacy
from spacy.tokens import Doc
from spacy.tokens import DocBin
import random

# Prep UD sentences for senter training
datasets = ["train", "dev", "test"]

for dataset in datasets:
    with open(f"assets/la_sents-ud-{dataset}.txt", "r") as f:
        sents = [line.strip() for line in f.readlines() if not line.startswith("#")]

    nlp = spacy.blank("la")
    db = DocBin()

    i = 0
    while i < len(sents):
        para_size = random.randint(3, 15)
        sent_docs = [nlp(sent) for sent in sents[i : i + para_size]]
        doc = Doc.from_docs(sent_docs, ensure_whitespace=True)
        db.add(doc)
        i += para_size

    db.to_disk(f"corpus/ud-{dataset}.spacy")
