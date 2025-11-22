# Create folders given a list of names
# python create_folders.py --enumerate

import os
import argparse


STOP_WORD = "--THE END--"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create folders")
    parser.add_argument(
        "--enumerate", default=False, action="store_true", help="Enumerate the folders"
    )
    args = parser.parse_args()
    # print(args.enumerate)

    print("Enter a list of folder names and at the end type {}:".format(STOP_WORD))
    lista = []
    while True:
        line = input()
        if line != STOP_WORD:
            lista.append(line)
        else:
            break

    # print(lista)

    for i in range(len(lista)):
        lista[i] = lista[i].replace("\t", "").replace("\n", "")

    print("Creating the folders...")

    count = 1

    for element in lista:
        if len(element) > 1:
            if args.enumerate is True:
                folder_name = str(count) + " " + element
            else:
                folder_name = element

            # print(folder_name)

            if os.path.isdir(folder_name) is False:
                os.mkdir(folder_name)
            count = count + 1
else:
    pass