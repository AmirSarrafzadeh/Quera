import re

def extract_paper(paper_file_path: str, font_size: int) -> dict:
    with open(paper_file_path, 'r', encoding='utf-8') as file:
        text = file.read().upper()


    with open(paper_file_path, 'r', encoding='utf-8') as file:
        originalText = file.read()

    sections = ["title\n", "\nabstract\n", "\nkeywords\n", "\nintroduction\n", "\nbody\n", "\nconclusion\n", "\nreferences\n"]
    originalSections = ["title", "abstract", "keywords", "introduction", "body", "conclusion", "references"]
    stringSections = ["title", "abstract", "introduction", "body", "conclusion"]
    data = {}

    # Split the text into sections and extract the desired sections
    for i in range(len(sections)):
        start_index = text.index(sections[i].upper()) + len(sections[i]) + 1
        end_index = text.index(sections[i + 1].upper()) if i < len(sections) - 1 else len(text)
        data[originalSections[i]] = originalText[start_index:end_index]

    # Calculate number of words
    word_count = sum(len(re.split(r'\s+|\n+', content)) for content in data.values())
    data['words_count'] = int(word_count + len(sections))

    average_words_per_page = 8192
    number_of_pages = (word_count * font_size) / average_words_per_page
    data['pages_count'] = int(number_of_pages)

    for i in range(len(sections)):
        if originalSections[i] == "keywords":
            data[originalSections[i]] = data[originalSections[i]].split(",")
        if originalSections[i] == "references":
            data[originalSections[i]] = data[originalSections[i]].split("\n")

    for i in range(len(stringSections)):
        data[stringSections[i]] = data[stringSections[i]].replace("\n", "")

    if len(data['abstract'].split(" ")) > 150:
        raise Exception("The abstract section can't be more than 150 words")

    if len(data['keywords']) > 5:
        raise Exception("You can't put more than 5 keywords")

    if sorted(data['keywords']) != data['keywords']:
        raise Exception("Keywords are not sorted")

    if number_of_pages > 9:
        raise Exception("The whole paper can't be more than 9 pages")



# extract_paper('paper1_sample.txt', 16)

