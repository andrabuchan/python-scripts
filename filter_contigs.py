
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
