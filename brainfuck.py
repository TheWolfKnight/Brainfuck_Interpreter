from file_hndl import FileHandler
from sys import argv, stdout
from error import FlagError
from fnmatch import filter
from intrp import Intrp


def print_help() -> None:
    hlp_msg: str = """
-f|--file:		Use: -f {file name}, gets input from the given file. Should not be used with "-i"
-o|--output:		Use: -o {file name}, writes the output to the given file, can be used with "-s"
-s|--silent:		Use: -s, stops the program from writing to stdout, can be used with "-o"
-i|--in:		Use: -i {input}, takes the input from stdin and use it for the interpretaiton.\n\t\t\t\t\t Should not be used with "-f"
-h|--help:		Use: -h, will show this message again.
    """
    stdout.write(hlp_msg)
    stdout.flush()
    return


def from_file(file_path: str) -> list[chr]:
    file_handler: FileHandler = FileHandler()
    r: list[chr] = file_handler.read_file(file_path)
    return r


def write_output(file_path: str, inpt: str) -> None:
    file_handler: FileHandler = FileHandler()
    file_handler.write_file(file_path, inpt)
    stdout.write(f"Wrote file {file_path}")
    stdout.flush()
    return


def from_string(inpt: str) -> list[chr]:
    return [ c for c in inpt ]


def main(argm: dict[str, str]=None):
    inpt: list[chr] = []

    silent: bool = 0
    out_file: str = ""

    if (len(argm) < 1):
        print_help()

    accepted_argvs: list[str] = ["-f", "--file", "-s", "--silent", "-i",
                                 "--in", "-h", "--help"]

    for key in argm:
        if key.startswith('-') or key.startswith('--') \
           and key.lower() not in accepted_argvs:
            raise FlagError(key)

        match key.lower():
            case ("-f"|"--file"):
                # Handles an input file
                idx: int = argm.index('-f') if '-f' in argm else argm.index('--file')
                inpt = from_file(argm[idx+1])
            case ("-o"|"--output"):
                idx: int = argm.index('-o') if '-o' in argm else argm.index('--output')
                out_file = argm[idx+1]
            case ("-s"|"--silent"):
                silent = 1
            case ("-i"|"--in"):
                # Handles the case where the user sets the input from terminal
                idx: int = argm.index('-i') if '-i' in argm else argm.index('--in')
                inpt = argm[idx+1]
            case ("-h"|"--help"):
                # Handles the case where the user needs help
                print_help()
            case _:
                pass

    intrp: Intrp = Intrp(inpt)
    intrp.write_buff()

    if (out_file):
        write_output(out_file, intrp.out)

    if (not silent):
        stdout.write("Output:", intrp.out)
        stdout.flush()

    return


if __name__ == "__main__":
    main(argv[1:])
    exit()
