import sys

# Initialize the IPA dictionary
IPA = {}

# Open the IPA.txv file with UTF-8 encoding
with open('IPA.txv', 'r', encoding='utf-8') as fd:
    for line in fd:
        line = line.strip('\n')
        if '\t' in line:
            (w, i) = line.split('\t')
            IPA[w] = i

#read input
for line in sys.stdin:
    line = line.strip('\n')

    if '\t' not in line:
        print(line)
    else:
        row = line.split('\t')
        if len(row) > 1:  # Check if the row has at least two elements
            arabic_text = row[1]

            # transcribe each char
            transcription = ''
            for char in arabic_text:
                transcription += IPA.get(char, char)  

            # put the transcription in the appropriate column
            if len(row) > 9:  # Check if the row has at least 10 elements
                row[9] = 'IPA=' + transcription
            else:
                # Append if less than 10 elements, assuming the 10th column is for IPA
                while len(row) < 10:
                    row.append('_')
                row.append('IPA=' + transcription)

            print('\t'.join(row))

