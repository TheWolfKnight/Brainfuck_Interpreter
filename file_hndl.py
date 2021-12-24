from error import PathError
from os.path import isfile
from sys import stdout

if __name__ == "__main__":
    exit()


class FileHandler(object):
    """
    An object to handle the reading of files, and subsequent pasing of data to the Intrp object\n
    """
    @staticmethod
    def read_file(file_name: str) -> list[chr]:
        if not isfile(file_name):
            raise PathError(file_name)
        black_list: list[chr] = [ ' ', '\t', '\n' ]
        r: list[chr] = []
        with open(file_name, 'r') as r_file:
            for line in r_file.readlines():
                    r += [ c for c in line if c not in black_list  ]
        return r

    @staticmethod
    def write_file(file_name: str, inpt: str) -> None:
        if isfile(file_name):
            stdout.write("This file already exist.\nDo you want to overwrite it?\n")
            stdout.flush()
            uInput = input("[y/N]: ")
            if uInput.lower() == 'n' or not uInput:
                raise PathError(file_name)
        with open(file_name, 'w') as w_file:
            w_file.write(inpt)
        return
