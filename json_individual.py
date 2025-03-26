#!/usr/bin/python3
#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-1", "--input_one", required=True)
parser.add_argument("-o", "--output_dir")
args = parser.parse_args()

infile1 = args.input_one
outdir = args.output_dir

seqdict1={}
key=""
val=""

#makes dictionary 1 of headers and seqs
with open(infile1, 'r') as faa1:
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


def makejson_1v1(filename, key, seq1):
	outfile = f"{outdir}/{filename}.json"
	with open(outfile, 'w') as output:
		output.write("{\n")
		output.write(f"  \"name\": \"{key}\",\n")
		output.write("  \"sequences\": [\n")
		output.write("    {\n")
		output.write("      \"protein\": {\n")
		output.write(f"	\"id\": [\"A\"],\n")
		output.write(f"	\"sequence\": \"{seq1}\"\n")
		output.write("      }\n")
		output.write("    }\n")
		output.write("  ],\n")
		output.write("  \"modelSeeds\": [1],\n")
		output.write("  \"dialect\": \"alphafold3\",\n")
		output.write("  \"version\": 1\n")
		output.write("}\n")


for i in range(0, len(seqdict1)) :
	i_key = list(seqdict1.keys())[i]
	i_val = list(seqdict1.values())[i]
	name = "contig_" + str(i+1)
	makejson_1v1(name, name, i_val)
