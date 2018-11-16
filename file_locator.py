import os  # chdir
import glob  # pathnames


def file_locator(): # funtion
    os.chdir(input("Enter Directory: ")) # Goes to directory you choose, use "/" instead of "\"
    file_type = input("Filename / Type: ")  # use *. to find all files with same type e.g *.zip
    for file in glob.glob(file_type):
        print(file)


file_locator()
