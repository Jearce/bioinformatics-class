## Dependencies

- trimmomatic
- fastqc
- spades=3.11.1
- megahit

If you have `conda` you can set up a conda environment for the script:
```
conda create -n run-assemblers-env -c conda-forge -c bioconda spades=3.11.1 megahit fastqc trimmomatic
conda activate run-assemblers-env

```
