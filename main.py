"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ASCENDING = True


def sort_list(items, ascending=True, remove_duplicates=False):
    if not isinstance(items, list):
        raise RuntimeError(f"Cannot sort {type(items)}")

    if remove_duplicates:
        items = remove_duplicates_from_list(items)

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    ascending = DEFAULT_ASCENDING
    if len(sys.argv) in (3, 4):
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        if len(sys.argv) == 4:
            order = sys.argv[3].lower()
            if order not in ("asc", "desc"):
                print("The third argument must be 'asc' or 'desc'")
                sys.exit(1)
            ascending = order == "asc"
    else:
        print("The file must be provided as the first argument")
        print("The second argument indicates whether duplicates should be removed (yes|no)")
        print("The optional third argument indicates the sort order (asc|desc)")
        sys.exit(1)

    print(f"Words will be read from file {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word = line.strip()
                if word:
                    word_list.append(word)
    else:
        print(f"File {filename} does not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    print(sort_list(word_list, ascending=ascending, remove_duplicates=remove_duplicates))
