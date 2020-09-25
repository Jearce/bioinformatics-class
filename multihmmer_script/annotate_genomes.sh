#!/bin/bash

export path_to_genomes=$1

#make directory to hold results
if [ $# -eq 2 ]
then 
  #use custom results dir
  export results_dir=$2
elif [ $# -eq 1 ]
then 
  #use default results dir name
  export results_dir="annotation_results"
else
  echo "incorrect number of arguments"
  echo "usage: annotate_genomes.sh <data directory> [outdir]"
  exit
fi

#check is results dir already exists
if [ -d $results_dir ]
then
  echo "${results_dir} already exists"
  exit
else
  mkdir $results_dir
fi

#loop through files that end in .fasta and .fna
for file in ${path_to_genomes}/*.fna ${path_to_genomes}/*.fasta
do

  if [ -f $file ]
  then 
    export name=$(basename $file)
    prokka --outdir ${results_dir}/${name}_dir $file
  else
    echo "Skipping non-file ${file}"
  fi

done



