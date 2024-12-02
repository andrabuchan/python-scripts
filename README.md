# splitseqs.py - splits multiple sequences in one file to their own individual files

    #Read the input file    

    inputfile='path to input file full of sequences'
    with open(inputfile, 'r') as file:
        sequences = file.read().split('>')

    #Remove empty elements

    sequences = [seq for seq in sequences if seq.strip()]

    #Split into individual sequences and write to separate files

    for seq in sequences:
        seq_lines = seq.strip().split('\n')
        seq_name = seq_lines[0].strip().replace(' ', '_')
        seq_data = '\n'.join(seq_lines[1:])

     #Write to a separate file
  
      with open(f'{seq_name}.phil.fasta', 'w') as output_file: 
        output_file.write(f'>{seq_name}\n{seq_data}\n')


# Python fasta parser - parses fasta input file and puts sequences into a dictionary

    with open("input.fa", "r") as infile:
        linelst=[] #used to hold each line in input file
        seq = ""
        seqdict={} #used to assign sequences to corresponding headers

    #adds each line in input file into a list
        for line in infile.readlines():
            linelst.append(line)

        for entry in linelst:
            count=0

            if entry.startswith(">"):
                header = entry
                
            else:
                seq = seq + entry
            #strips the sequence string of new line characters, adds header and corresponding sequence to dictionary, and then clears seq variable
            seq = seq.strip("\n")        
            seqdict.update({header:seq})
            seq=""

# Filter contigs under n nucleotides long

#!/usr/bin/python3

import argparse
import os

#argparse stuff
parser = argparse.ArgumentParser()
required = parser.add_argument_group("Required")
optional = parser.add_argument_group("Optional")

required.add_argument('-f', '--file', help='Input file (.fna)', required=True)
required.add_argument('-m', '--minimum', help='Minimum contig length (bp)', required=True)
required.add_argument('-o', '--output', help='Name of file for filtered contigs', required=True)

optional.add_argument('--filter-out', help='Specify and include -o to save filtered output', required=False)

args = parser.parse_args()

input_file_str = str(args.file)
output_file_str = str(args.output)
min_bp = int(args.minimum)

#collects headers and seqs into dictionary, keeping newline chars
def get_header(infile, min):
        print("Collecting contigs containing at least " + str(min) + " bp")
        contig_dict={}
        header=""
        seq=""
        with open(infile, "r") as infile:
                for line in infile.readlines():
                        if line.startswith(">"):
                                if len(seq.rstrip()) > min:
                                        contig_dict.update({header:seq})
                                seq=""
                                header = line
                        else:
                                seq += line
                contig_dict.update({header:seq})
        print(str(len(contig_dict.keys())) + " contigs found...")
        return contig_dict

info_dict = get_header(input_file_str, min_bp)

def write_output(dict, outfile):
        print("Creating filtered output...")
        with open(outfile, 'w') as out:
                for key, value in dict.items():
                        out.write(key)
                        out.write(value)
        print("Filtered sequence has been written to " + outfile)

write_output(info_dict, output_file_str)
