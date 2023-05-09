#!/usr/bin/env sh

fasta_file="input.fasta"
new_desc_file="new_desc.txt"
output_file="output.fasta"

# Load the new descriptions into an array
declare -A new_desc
while read line; do
  accession=$(echo $line | cut -f1)
  desc=$(echo $line | cut -f2)
  new_desc[$accession]=$desc
done < $new_desc_file

# Replace the description lines in the FASTA file
while read line; do
  if [[ $line =~ ^\> ]]; then
    accession=$(echo $line | cut -d' ' -f1 | sed 's/>//')
    if [[ ${new_desc[$accession]} ]]; then
      echo "$line ${new_desc[$accession]}" >> $output_file
    else
      echo $line >> $output_file
    fi
  else
    echo $line >> $output_file
  fi
done < $fasta_file
