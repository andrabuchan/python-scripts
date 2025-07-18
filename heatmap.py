#!/usr/bin/python3
#creates a heatmap with an input TSV. First column is used as index
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', "--input", help="input TSV")
parser.add_argument('-o', "--output", help="output .png")
parser.add_argument('-t', "--title", help="title of your heatmap")
parser.add_argument('-x', "--xlabel", help="the label for the x axis")
parser.add_argument('-y', "--ylabel", help="the label for the y axis")

args = parser.parse_args()
#color = sns.color_palette("light:r", as_cmap=True)
df = pd.read_csv(args.input, sep='\t', index_col=0)
print(df)
plt.figure(figsize=(8, 8))
sns.heatmap(df.T, linewidths=1, cmap="viridis", annot=True, fmt=".1f", annot_kws={"size": 8}, cbar=True)
plt.title(args.title)


#Functions at the top
plt.xticks(rotation=45, ha='right')
plt.xlabel(args.xlabel)

#ID names at the bottom
plt.yticks(rotation=0)
plt.ylabel(args.ylabel)
plt.subplots_adjust(left=0.35, right=0.65, top=0.75, bottom=0.25)
print("Heatmap saved to " + args.output)
plt.savefig(args.output)
