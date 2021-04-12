## Create a phylogenetic tree with biopython

### Dependencies 
- matplotlib
- Biopython
- muscle

### Setup
```
conda create -n quick-tree-env -c bioconda -c conda-forge biopython muscle matplotlib
conda activate quick-tree-env
git clone https://github.com/Jearce/bioinformatics-class.git
cd bioinformatics-class/quick_tree
python quick_tree.py --input seqs.fasta --output out
```

### Help 
```
usage: quicktree.py [-h] --input INPUT --output OUTPUT [-phylipf PHYLIPF]
                    [-model MODEL] [-method METHOD]

Quick and easy tree reconstruction

optional arguments:
  -h, --help        show this help message and exit
  --input INPUT     Input fasta file
  --output OUTPUT   Output directory
  -phylipf PHYLIPF  Phylip format relaxed or sequential. Default is sequential
  -model MODEL      Choose model, identity for dna or blosum62 for protein.
                    Default is blosum62
  -method METHOD    Choose tree reconstruction method nj or upgma.Default is
                    nj
 ```
