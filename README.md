<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: la_senter

Code required to train spaCy-compatible sentence segmenter for Latin.


## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `assets` | Download assets |
| `preprocess` | Convert the data to spaCy's format |
| `load-vectors` | load floret vectors |
| `train` | Train senter |
| `evaluate` | Evaluate on the test data and save the metrics |
| `package` | Package the trained model so it can be installed |
| `document` | Document senter |
| `clean` | Remove intermediate files |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `assets` &rarr; `preprocess` &rarr; `load-vectors` &rarr; `train` &rarr; `evaluate` &rarr; `package` &rarr; `document` &rarr; `clean` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets/treebanks/UD_Latin-Perseus` | Git |  |
| `assets/treebanks/UD_Latin-PROIEL` | Git |  |
| `assets/treebanks/UD_Latin-ITTB` | Git |  |
| `assets/treebanks/UD_Latin-LLCT` | Git |  |
| `assets/treebanks/UD_Latin-UDante` | Git |  |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->

## Install

- To install the current version...
    - `pip install https://huggingface.co/diyclassics/la_senter/resolve/main/la_senter-0.3.0/dist/la_senter-0.3.0.tar.gz`

## Current version

| Feature | Description |
| --- | --- |
| **Name** | `la_senter` |
| **Version** | `0.3.0` |
| **spaCy** | `>=3.4.2,<3.6.0` |
| **Default Pipeline** | `senter` |
| **Components** | `senter` |
| **Vectors** | -1 keys, 50000 unique vectors (300 dimensions) |
| **Sources** | UD_Latin-Perseus<br />UD_Latin-PROIEL<br />UD_Latin-ITTB<br />UD_Latin-LLCT<br />UD_Latin-UDante |
| **License** | `MIT` |
| **Author** | [Patrick J. Burns](https://diyclassics.github.io/) |

### Accuracy

| Type | Score |
| --- | --- |
| `SENTS_F` | 99.55 |
| `SENTS_P` | 99.45 |
| `SENTS_R` | 99.65 |
| `SENTER_LOSS` | 4029.93 |
