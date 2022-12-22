# Imports
import os
import os.path
import glob
import re

# Constants
UD_PATH = "assets/treebanks"

# Set up files
files = glob.glob(f"{UD_PATH}/**/*.conllu", recursive=True)
train = [file for file in files if "train" in file]
dev = [file for file in files if "dev" in file]
test = [file for file in files if "test" in file]

# Helper functions
def format_filename(filename):
    return os.path.basename(os.path.normpath(filename))


def format_sent(sent):
    return sent.replace("# text = ", "")


def convert_pauses(contents):
    return re.sub(r"([:;]) ", "\g<1>\n", contents)


def force_punctuation(line):
    # if not re.search(r'A-Za-z]$', line):
    if line[-1] not in ".?!:;":
        line = f"{line}."
    return line


# Main function
def extract_ud_sents(contents):
    contents = convert_pauses(contents)
    lines = contents.split("\n")
    sents = [
        force_punctuation(format_sent(line))
        for line in lines
        if line.startswith("# text = ")
    ]
    return sents


# Process filesets
filesets = [("train", train), ("dev", dev), ("test", test)]

for fileset in filesets:
    with open(f"assets/la_sents-ud-{fileset[0]}.txt", "w") as fout:
        for file in fileset[1]:
            fout.write(f"# {format_filename(file)}\n")
            with open(file, "r") as f:
                contents = f.read()
            sents = extract_ud_sents(contents)
            for sent in sents:
                fout.write(f"{sent}\n")
