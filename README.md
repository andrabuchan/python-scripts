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
        
            seqdict.update({header:seq})

