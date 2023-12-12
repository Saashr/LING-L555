import xml.etree.ElementTree as ET

# creating mapping scheme from msa to UD
def map_msa_to_ud(msa_tag):
    tag_mapping = {
        'v': 'VERB', 'vt': 'VERB', 'vi': 'VERB', 'vd': 'VERB',
        'n': 'NOUN', 'npr': 'NOUN', 'n>n': 'NOUN', 'n>adn': 'NOUN', '???>n': 'NOUN',
        'adn': 'ADJ', 'adn>adn': 'ADJ', 'adn:Any': 'ADJ',
        'advl': 'ADV',
        'interj': 'INTJ',
        'postn': 'ADP', 'postp': 'ADP',
        'ptc': 'PART',
        'pron': 'PRON',
        'num': 'NUM', 'ordnum': 'NUM', 'num>ordnum': 'NUM',
        'cop': 'AUX', 'cop>cop': 'AUX', 'cop:Any': 'AUX',
        'clf': 'X',
        'conn': 'CONJ', 'coordconn': 'CONJ',
        'quant': 'DET',
        'dir': 'ADV', 'dir>dir': 'ADV', 'v>dir': 'ADV',
        'subo': 'SCONJ',
        'Particle': 'PART',
        'dem': 'PRON', 'dem>dem': 'PRON',
        'v>vc': 'VERB', 'vc': 'VERB', 'vc>vc': 'VERB', 'vt>vi': 'VERB', 'v:Any': 'VERB', 'v>adn': 'VERB',
        'vt>vt': 'VERB', 'v>n': 'VERB', 'v>vt': 'VERB', 'v>v': 'VERB', 'vt>adn': 'VERB', 'vt:Any': 'VERB', 'v>vc': 'VERB'
    }
    return tag_mapping.get(msa_tag, 'UNKNOWN')  # 'UNKNOWN' if unable to get a corresponding one

def modified_main():
    
    tree = ET.parse('Lamkang.xml')
    root = tree.getroot()
#find root
    paragraph_elements = root.findall('.//paragraph')
#give paragraphs index
    for paragraph_index, paragraph in enumerate(paragraph_elements):
        word_index = 1
        word_elements = paragraph.findall('.//word')

        # Gather all word texts if they are followed by tag "item" and type "txt"
        word_texts = [word_element[0].text for word_element in word_elements
                      if word_element[0].tag == 'item' and word_element[0].get('type') == 'txt']
        sentence = ' '.join(filter(None, word_texts))  # Join texts to form a sentence

        print(f"# paragraph {paragraph_index + 1}")
        print(f"text : {sentence}")
#extract word elements, again only the one which are not blank
        for word_element in word_elements:
            if word_element[0].tag == 'item' and word_element[0].get('type') == 'txt':
                word_text = word_element[0].text
                individual_words = word_text.split() if word_text else []
                morph_texts = []
#find corresponding tags
                for morph in word_element.findall('.//morph'):
                    msa_text = next((item.text for item in morph if item.tag == 'item' and item.get('type') == 'msa'), None)
                    if msa_text:
                        ud_tag = map_msa_to_ud(msa_text)
                        morph_texts.append((msa_text, ud_tag))
#if equal in number put on next line
                if len(individual_words) == len(morph_texts):
                    for individual_word, (msa_text, ud_tag) in zip(individual_words, morph_texts):
                        print(f"{word_index}\t{individual_word}\t_\t_\t{ud_tag}\t_\t_\t_\t_\t{msa_text}")
                        word_index += 1
                else:
                    print(f"{word_index}\t{word_text}\t_\t_\t{' '.join([ud_tag for _, ud_tag in morph_texts])}\t_\t_\t_\t_\t{' '.join([msa_text for msa_text, _ in morph_texts])}")
                    word_index += 1
        print()


if __name__ == "__main__":
    modified_main()

                      
