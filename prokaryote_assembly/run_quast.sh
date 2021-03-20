#!/bin/bash

export ref_genome_dir=$1

if [ $# -ne 1 ]
then
  echo "Incorrect number of arguments"
  echo "$0 <reference genome dir>"
  exit
fi

quast -o quast_out \
  -R ${ref_genome_dir}/*.fna.gz -g ${ref_genome_dir}/*.gff.gz \
  -l "Spades_default , Spades_careful, Megahit_default, Megahit_min_count" \
  spades_default/contigs.fasta \
  spades_careful/contigs.fasta \
  megahit_default/final.contigs.fa \
  megahit_min_count_3/final.contigs.fa
