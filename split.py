#!/usr/bin/env python
"""This program parses, splits, and writes the slices of a list to files."""

import argparse
import random
from typing import Iterator, List

def main(args):

    def read_tags(path: str) -> Iterator[List[List[str]]]:
        with open(path, "r") as source:
            lines = []
            for line in source:
                line = line.rstrip()
                if line:  # Line is contentful.
                    lines.append(line.split())
                else:  # Line is blank.
                    yield lines.copy()
                    lines.clear()
    # Just in case someone forgets to put a blank line at the end...
        if lines:
            yield lines
    
    corpus = list(read_tags(args.file_input))


    #Defining a function that turns the innermost list into a string then writes it to a file. 
    def write_tags(my_list, my_file):
        with open(my_file, 'w') as file_object:
            for i in my_list:
                for j in i:
                    my_string = " ".join(j)
                    print(my_string, file = file_object)

    #The seeding and shuffling steps 
    random.seed(args.seed)
    random.shuffle(corpus)

    #Slicing the corpus list. 
    index_80 = int(len(corpus)*0.8) 
    slice_80 = corpus[:index_80]
    del corpus[:index_80] 

    index_10 = int(len(corpus)*0.5)
    slice_10 = corpus[:index_10]
    del corpus[:index_10]

    #Calling the function.
    write_tags(slice_80, args.train) 
    write_tags(slice_10, args.dev)  
    write_tags(corpus, args.test)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file_input", help = "The input file"
        )
    parser.add_argument(
        "train", help = "The training data"
        )
    parser.add_argument(
       "dev", help = "The devolopement data"
        )
    parser.add_argument(
        "test", help = "The test data"
        )
    parser.add_argument(
        "--seed", required = True, help = "The number used to seed"
    )
    main(parser.parse_args())