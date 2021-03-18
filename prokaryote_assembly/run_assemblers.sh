#!/bin/bash

set -u
set -e
set -o pipefail

function create_directory_if_needed(){
  dir_name=$1
  if [ ! -d ${dir_name} ]
  then
    mkdir ${dir_name}
  fi
  echo ${dir_name}
}



if [ $# -ne 3 ]
then
  echo "Incorrect number of arguments"
  echo "${0} <forward reads> <reverse reads> <adapter fasta>" 
  exit
fi 

export raw_r1_reads=$1
export raw_r2_reads=$2
export adapters=$3
export t=10

export fastqc_dir=$(create_directory_if_needed "fastqc_report")

#get just the filename from the forward and reverse reads with no extension
#example somefolder/ERR163736_1_.fastq -> EERR163736_1_
export ffile_name=$(basename -- "${raw_r1_reads%.*}")
export rfile_name=$(basename -- "${raw_r2_reads%.*}")

#quality assessment
fastqc ${raw_r1_reads} ${raw_r2_reads} -o ${fastqc_dir} -t ${t} --extract
export fastqc_r1_file_dir=${fastqc_dir}/${ffile_name}_fastqc
export fastqc_r2_file_dir=${fastqc_dir}/${rfile_name}_fastqc
export read_length=$(grep -E "^(Sequence length)" ${fastqc_r1_file_dir}/fastqc_data.txt  | awk -F " " '{print $3}')


#trimmomatic output dir name and files
export trim_dir=$(create_directory_if_needed "trimmomatic_out")
export r1_paired=${trim_dir}/${ffile_name}_paired.fastq 
export r1_unpaired=${trim_dir}/${ffile_name}_unpaired.fastq 
export r2_paired=${trim_dir}/${rfile_name}_paired.fastq 
export r2_unpaired=${trim_dir}/${rfile_name}_unpaired.fastq 

#attempt to improve reads
trimmomatic PE \
  ${raw_r1_reads} ${raw_r2_reads} \
  ${r1_paired} ${r2_unpaired} \
  ${r2_paired} ${r2_unpaired} \
  ILLUMINACLIP:${adapters}:2:30:10 \
  CROP:${read_length} LEADING:20 \
  TRAILING:20 SLIDINGWINDOW:5:20 \
  MINLEN:${read_length} \

#create report for improved data
fastqc ${r1_paired} ${r2_paired} -o ${fastqc_dir} -t ${t} --extract


#error correction
spades.py -1 $r1_paired  -2 $r2_paired \
-o spades_corrected --only-error-correction -t ${t}

#use corrected reads for assemblies
export forward_cor="spades_corrected/corrected/$(basename "${r1_paired%.*}").00.0_0.cor.fastq"
export reverse_cor="spades_corrected/corrected/$(basename "${r2_paired%.*}").00.0_0.cor.fastq"

#decompress for megahit assembly
gzip -d ${forward_cor}.gz
gzip -d ${reverse_cor}.gz


echo "Running spades.py default....."

spades.py \
  -1 ${forward_cor}\
  -2 ${reverse_cor}\
  -o spades_default\
  -t ${t}\
  --only-assembler

echo "Spades default run finished successfully!"

echo "Running spades.py careful...."

spades.py \
  -k 21,33,55,77,99,127 \
  -1 ${forward_cor}\
  -2 ${reverse_cor}\
  -o spades_careful\
  -t ${t}\
  --careful \
  --only-assembler \

echo "Spades careful run finished successfully!"

echo "Running megahit default..."

megahit\
  -1 ${forward_cor}\
  -2 ${reverse_cor}\
  -o megahit_default

echo "Megahit default finished successfully!"

echo "Running megahit min-count=3...."

megahit \
  -1 ${forward_cor} \
  -2 ${reverse_cor} \
  -o megahit_min_count_3 \
  --min-count 3

echo "megahit min-count=3 finished successfully!"

echo "Done."
