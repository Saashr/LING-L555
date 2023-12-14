import sys

tag_counts = {}
word_to_tag = {}

#  read the model file (my moodel file has only two columns , I processed my training output file further to create a tsv mapping file)
with open('model.tsv', 'r') as fd:
    for line in fd.readlines():
        row = line.strip().split('\t')
        if len(row) != 2:  
            continue
        form, tag = row  

        word_to_tag[form] = tag

        if tag not in tag_counts:
            tag_counts[tag] = 0
        tag_counts[tag] += 1

# Find the most frequent tag
most_frequent_tag = max(tag_counts, key=tag_counts.get)

# Process the standard input
for line in sys.stdin.readlines():
    line = line.strip('\n')
    if '\t' not in line:
        print(line)
        continue

    row = line.split('\t')
    if len(row) < 2:  # make sure there are enough columns
        print(line)
        continue

    form = row[1]
    tag = word_to_tag.get(form, most_frequent_tag)
    row[3] = tag  #put the tag in the 4th column
    print('\t'.join(row))

