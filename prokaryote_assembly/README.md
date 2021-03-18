## Dependencies

- trimmomatic
- fastqc
- spades=3.11.1
- megahit

If you have `conda` you can set up an conda environment for the script:
```
conda create -n run-assemblers-env -c conda-forge -bioconda spades=3.11.1 megahit fastqc trimmomatic
conda activate run-assemblers-env

```
