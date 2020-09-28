# Auto Annotate With Prokka

## About
This bash script is designed to annotate prokayotic genomes using `prokka`. Just give the script a directory with genomes
in it and prokka will be used to annotate them. Genomes must be in fasta format.

## Installation

The only requirement is prokka. Which you can download with `conda`. 

Create `conda` environment and download prokka:

```
conda create -n prokka_env -c bioconda prokka
```

Activate `conda` environment:

```
conda activate prokka_env
```

Clone this repository and change directories into this project's directory:

```
git clone https://github.com/Jearce/bioinformatics-class.git
cd bioinformatics-class/auto_annotate
```

## Usage

Make script execuatable:

```
chmod +x annotate_genomes.sh
```
Run script:

```
./annotate_genomes.sh <directory>
```
The directory should have fasta files, ending with .fasta or .fna, in it. The prokka results for each annotated genome will be written to `annotation_results` directory.

A second arguement is optional to specify the name of the output directory:

```
./annotate_genomes.sh <directory> [output dir]
```

