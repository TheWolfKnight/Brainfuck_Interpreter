from file_hndl import FileHandler
from sys import exit, argv
from compiler import Compiler
from intrp import Intrp


GLOB_compile: bool = False


class FlagError(Exception):
	def __init__(self, flag: str, response: str):
		self.flag = flag
		self.response = response

	def __str__(self) -> str:
		return f""



def print_help() -> ():
	print("Help")
	return


def from_file(file_path: str) -> list[chr]:
	global GLOB_compile
	file_handler: FileHandler = FileHandler(file_path)
	r: list[chr] = file_handler.read_file(GLOB_compile)
	return r


def from_string(inpt: str) -> list[chr]:
	return [ c for c in inpt ]


def to_compiled(inpt: list[chr]) -> list[chr]:
	r: list[chr] = []


def test_env():
	inpt: list[chr] = ['+'] + ['['] + ['+'] * 71 + ['>'] + [']'] + ['<'] + ['.']
	intrp: Intrp = Intrp(inpt)
	intrp.write_buff()
	print(intrp.out)


def main(argm: dict[str, str]=None):
	test_env()
	return

	global GLOB_compile
	inpt: list[chr] = []
	for key in argm:
		match key:
			case ("-c"|"--compile"):
				# Handles the file by compiling it to brainfuck
				GLOB_compile = True
			case ("-f"|"--file"):
				# Handles an input file
				idx: int = argm.index('-f') if '-f' in argm else argm.index('--file')
				inpt = from_file(argm[idx+1])
			case ("-i"|"--in"):
				# Handles the case where the user sets the input from terminal
				idx: int = argm.index('-i') if '-i' in argm else argm.index('--in')
				inpt = argm[idx+1]
			case ("-h"|"--help"):
				# Handles the case where the user needs help
				print_help()
			case _:
				break
	if (len(argm) < 1):
		print_help()
	return


if __name__ == "__main__":
	main(argv[1:])
	exit()