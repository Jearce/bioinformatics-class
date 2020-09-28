# bioinformatics-class
Projects created in my bioinformatics class. 

 - Zeus: command line program that runs other programs to assemble and annotate a bacterial genome.
 - Multi HMMER search: Simple bash script that takes query sequences in a single fasta file and a directory with fasta files
 that each contain proteins from a given organism. With the query a multiple sequence alignment (MSA) is generated with0 muscle. Afterwards, a profile Hiddin Markov Model (HMM) is generated with hmmbuild.Using hmmsearch the HMM created from hmmbuild is used to search in the fasta files that are in the given directory for similar proteins to the query sequences.
