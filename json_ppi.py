#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-1", "--input_one", required=True)
parser.add_argument("-2", "--input_two", required=False)
parser.add_argument("-o", "--output_dir")
args = parser.parse_args()

infile1 = args.input_one
infile2 = args.input_two
outdir = args.output_dir

seqdict1={}
seqdict2={}
key=""
val=""
#makes dictionary 1 of headers and seqs
with open(infile1, 'r') as faa1, open(infile2, 'r') as faa2:
	for line in faa1:
		if line.startswith(">") and len(val) == 0:
			key = line[1:].strip()
		elif not line.startswith(">") and len(key) != 0:	
			val += line.strip()
		elif (line.startswith(">") or False) and len(val) > 0:
			val = val.strip("*")
			seqdict1.update({key:val})
			key = line[1:].strip()
			val=""
#makes dictionary 2 if input 2 present
	if args.input_two is not None:
		val=""
		key=""
		for line in faa2:
			if line.startswith(">") and len(val) == 0:
				key = line[1:].strip()
			elif not line.startswith(">") and len(key) != 0:
				val += line.strip()
			elif (line.startswith(">") or False) and len(val) > 0:
				val = val.strip("*")
				seqdict2.update({key:val})
				key = line[1:].strip()
				val=""


def makejson_1v1(filename, key, seq1, seq2 ):
	outfile = f"{outdir}/{filename}.json"
	with open(outfile, 'w') as output:
		output.write("{\n")
		output.write(f"  \"name\": \"{key}\",\n")
		output.write("  \"sequences\": [\n")
		output.write("    {\n")
		output.write("      \"protein\": {\n")
		output.write(f"        \"id\": [\"A\"],\n")
		output.write(f"        \"sequence\": \"{seq1}\"\n")
		output.write("      }\n")
		output.write("    },\n")
		output.write("    {\n")
		output.write("      \"protein\": {\n")
		output.write(f"        \"id\": [\"B\"],\n")
		output.write(f"        \"sequence\": \"{seq2}\"\n")
		output.write("      }\n")
		output.write("    }\n")
		output.write("  ],\n")
		output.write("  \"modelSeeds\": [1],\n")
		output.write("  \"dialect\": \"alphafold3\",\n")
		output.write("  \"version\": 1\n")
		output.write("}\n")


def makejson_1v2(filename, key, seq1, seq2 ):
        outfile = f"{outdir}/{filename}.json"
        with open(outfile, 'w') as output:
                output.write("{\n")
                output.write(f"  \"name\": \"{key}\",\n")
                output.write("  \"sequences\": [\n")
                output.write("    {\n")
                output.write("      \"protein\": {\n")
                output.write(f"        \"id\": [\"A\"],\n")
                output.write(f"        \"sequence\": \"{seq1}\"\n")
                output.write("      }\n")
                output.write("    },\n")
                output.write("    {\n")
                output.write("      \"protein\": {\n")
                output.write(f"        \"id\": [\"B\"],\n")
                output.write(f"        \"sequence\": \"{seq2}\"\n")
                output.write("      }\n")
                output.write("    }\n")
                output.write("  ],\n")
                output.write("  \"modelSeeds\": [1],\n")
                output.write("  \"dialect\": \"alphafold3\",\n")
                output.write("  \"version\": 1\n")
                output.write("}\n")


#if no input 2, do 1v1 json gen
if args.input_two is None:
	for i in range(0, len(seqdict)) :
		i_key = list(seqdict1.keys())[i]
		i_val = list(seqdict1.values())[i]

		for j in range(0, len(seqdict1)):

			j_val = list(seqdict1.values())[j]
			name = "contig_" + str(i+1) + "_" + str(j+1)
			makejson_1v1(name, name, i_val, j_val)
#if input2, do 1v2 json gen
elif args.input_two is not None:
	for i in range(0, 499):
		i_key = list(seqdict1.keys())[i]
		i_val = list(seqdict1.values())[i]
		out = "contig_" + str(i+1)
		for j in range(0, len(seqdict2)): #j = seq2
			j_val = list(seqdict2.values())[j]
			name = "contig_" + str(i+1) + "_" + str(j+1)
			makejson_1v2(name, name, i_val, j_val)
