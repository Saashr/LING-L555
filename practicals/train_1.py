import sys

word_tag_matrix = {}
tag_freq_list = {}
total_tokens = 0

def is_tag(component):
    # Define a condition to identify the tag. Modify this according to your criteria.
    # For example, if tags are always uppercase, you might use:
    # return component.isupper()
    return True  # Placeholder, replace with actual condition

# Read the file
with open('wiki.conllu', 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip() == '' or line.startswith('#'):
            continue

        components = line.split('\t')
        word = components[1]

        # Find the tag in the components
        tag = next((comp for comp in components if is_tag(comp)), None)
        if tag is None:
            continue  # Skip if no tag is found

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

# Calculating probabilities and print the model
for tag, freq in tag_freq_list.items():
    p_tag = freq / total_tokens
    print(f"{p_tag:.2f}\t{freq}\t{tag}\t_")

# word-tag probabilities
for word, tags in word_tag_matrix.items():
    for tag, freq in tags.items():
        p_word_tag = freq / sum(word_tag_matrix[word].values())
        print(f"{p_word_tag:.2f}\t{freq}\t{tag}\t{word}")

