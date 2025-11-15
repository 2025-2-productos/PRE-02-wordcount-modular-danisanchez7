import os


def write_word_counts(counter, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_path = os.path.join(output_folder, "wordcount.tsv")
    with open(output_path, "w", encoding="utf-8") as f:
        for key, value in counter.items():
            f.write(f"{key}\t{value}\n")
