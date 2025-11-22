#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', "--input", help="Input annotation (gff) file from MetaCerberus")
parser.add_argument('-o', "--output", help="Output annotation (gff) file containing filtered reads")
args = parser.parse_args()


gff = open(args.input, 'r')
linelist = gff.readlines()
header = linelist[0]
print(f"Parsing {len(linelist)} sequences...")

#filters headers out of list
def preprocess(linelist):
        num_removed_lines = 0
        for line in linelist:
                #removes headers
                if line.startswith('#'):
                        header = line
                        linelist.remove(line)
                        continue
        data = line.split('\t')

        if len(data) < 2:
                linelist.remove(line)
                num_removed_lines += 1
        print(f"PREPROCESSING: removed {num_removed_lines} lines")
        return linelist


#filters out hypothetical genes
def remove_hypothetical(linelist):
        linelist = [ line for line in linelist if "Hypothetical" not in line ]
        print(f"FILTERING: removed hypothetical genes. Left with {len(linelist)} genes")
        return linelist


#removes semicolons from gene names, as that is the delimiter for attributes
def format_names(linelist):
        num_semicolons = 0
        for line in linelist:
                data = line.split('\t')
                attr = data[-1].split(';')
                if len(attr) > 8:
                        genename = attr[1] + ";" + attr[2]
                        new_genename = attr[1] + attr[2]
                        index = linelist.index(line)
                        fixed_line = line.replace(genename, new_genename)
                        linelist[index] = fixed_line
                        num_semicolons += 1
        print(f"FORMATTING: removed semicolons from {num_semicolons} gene names")
        return linelist


linelist = preprocess(linelist)
linelist = remove_hypothetical(linelist)
linelist = format_names(linelist)

with open(args.output, 'w') as outfile:
        outfile.write(header)
        for line in linelist:
                outfile.write(line)
        outfile.close()
print(f"featureCounts friendly annotation written to {args.output}")
