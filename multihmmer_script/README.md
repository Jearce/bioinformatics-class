# Multi HMMER Search



## About

This is a simple bash script that takes query sequences in a single fasta file and a directory with fasta files
that each contain proteins from a given organism. With the query a multiple sequence alignment (MSA) is generated
with `muscle`. Afterwards, a profile Hiddin Markov Model (HMM) is generated with `hmmbuild`.Using `hmmsearch` the
HMM created from `hmmbuild` is used to search in the fasta files that are in the given directory for similar 
proteins to the query sequences.


## Usage

Clone this repository and change directories into this projects directory:
```
git clone https://github.com/Jearce/bioinformatics-class.git
cd bioinformatics-class/multihmmer_script

```

First make execuatable:

```
chmod +x multi_hmmer_search.sh

```
Run the script:

```
multi_hmmer_search <query> <in directory>

```
