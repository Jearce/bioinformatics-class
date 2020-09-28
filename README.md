# bioinformatics-class
Projects created in my bioinformatics class. 

 - **zeus**: Command line program, written in python, that runs other programs to assemble and annotate a bacterial genome.
 - **multihmmer_script**: 
 Simple bash script that takes query sequences in a single fasta file and a directory with fasta files
 that each contain proteins from a given organism. With the query a MSA is generated with `muscle`. 
 Afterwards, a HMM isgenerated with `hmmbuild`.Using `hmmsearch` the HMM created from hmmbuild is used to search in the
 fasta files that are in the given directory for similar proteins to the query sequences.
 - **auto_annotate**: Bash script to annotate prokayotic genomes using `prokka`. Just give the script a directory with
 genomes in it and prokka will be used to annotate them.
