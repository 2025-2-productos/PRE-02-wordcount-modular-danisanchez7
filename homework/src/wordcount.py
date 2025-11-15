# obtain a list of files in the input directory
import sys

from ._internals.count_words import count_words
from ._internals.preprocess_lines import preprocess_lines
from ._internals.read_all_lines import read_all_lines
from ._internals.split_into_words import split_into_words
from ._internals.write_word_counts import write_word_counts


def main():
    """
    if len(sys.argv) != 3:
        print("Usage: python -m homework <input_folder> <output_folder>")
        sys.exit(1)
    """
    input_folder = "data/input"
    output_folder = "data/output"

    all_lines = read_all_lines(input_folder)
    all_lines = preprocess_lines(all_lines)
    words = split_into_words(all_lines)
    counter = count_words(words)
    write_word_counts(counter, output_folder)


if __name__ == "__main__":
    main()
