
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

file = open("emancipation_proclamation.txt", "r")

content = file.read()

lowercase = content.lower()
print(lowercase)

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    
        # content = content.split()

    # def clean_text(text):
    #     all_letters = "abcdefghijklmnopqrstuvwxyz"
    #     keep_text = ""
    #     for char in text:
    #         if char in all_letters:
    #             keep_text += char
    #     return keep_text

    # clean_words = []

    # for word in content:
    #     clean_words.append(clean_words(word))

    # def remove_stop_words(array):
    #     for word in array:
    #         if word in STOP_WORDS:
    #             array.remove(word)
    #             return array

        


# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)
