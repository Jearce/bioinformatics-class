#!/bin/bash

export query=$1
export data_dir=$2

#build HMM
muscle -in ${query} -out ${query}.aln
hmmbuild ${query}.hmm ${query}.aln


export results_dir="multi_hmmer_results"

#check if results folder already exists
if [ -d ${results_dir} ]
then 
  echo "${results_dir} already exists"
  exit
else 
  mkdir ${results_dir}
fi

#search in given protein sets
for file in ${data_dir}/*.fasta
do
  hmmsearch ${query}.hmm ${file} > ${results_dir}/${file}_results.txt 
done

