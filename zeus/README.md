## About

Zeus is a command line tool for bacterial genome assembly and subsequent annotation for a set of given proteins. 

## Requirements
Third Party Packages:

- [Biopython](https://biopython.org/)

Bioinformatic Software:

- [Prodigal](https://github.com/hyattpd/Prodigal)
- [SPAdes](http://cab.spbu.ru/software/spades/) 
- [BLAST+](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download)
- [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic)
- [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)

You can also download these packages and software with `conda` and create a new environment for zeus.
To download conda you can go [here.](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)

```
$ conda create -n zeus_env -c bioconda prodigal spades fastqc trimmomatic biopython java-jdk --yes

```

After creating new environment you can activate it:

```
$ conda activate zeus_env

```
