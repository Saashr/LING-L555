import sys

word_tag_matrix = {}
tag_freq_list = {}
total_tokens = 0

# Read the file
with open('wiki.conllu', 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip() == '' or line.startswith('#'):
            continue

        components = line.split('\t')
        if len(components) >= 5:
            word = components[1]
            # Check both the 4th and 5th column for the UD POS tag
            tag = components[3] if components[3] != '_' else components[4]

            total_tokens += 1

            # Update word-tag matrix
            if word not in word_tag_matrix:
                word_tag_matrix[word] = {}
            if tag not in word_tag_matrix[word]:
                word_tag_matrix[word][tag] = 0
            word_tag_matrix[word][tag] += 1

            # Update tag frequency list
            if tag not in tag_freq_list:
                tag_freq_list[tag] = 0
            tag_freq_list[tag] += 1

# Print header
print("P\tcount\ttag\tform")

# Calculating probabilities and printing the model
for tag, freq in tag_freq_list.items():
    p_tag = freq / total_tokens
    print(f"{p_tag:.2f}\t{freq}\t{tag}\t_")

# Word-tag probabilities
for word, tags in word_tag_matrix.items():
    for tag, freq in tags.items():
        p_word_tag = freq / sum(word_tag_matrix[word].values())
        print(f"{p_word_tag:.2f}\t{freq}\t{tag}\t{word}")

