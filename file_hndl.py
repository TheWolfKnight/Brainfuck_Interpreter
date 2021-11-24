from os.path import isfile
from sys import exit


if __name__ == "__main__":
	exit()


class PathError(Exception):
	def __init__(self, file: str):
		self.file = file

	def __str__(self) -> str:
		return "\nAn error occured with the given file" \
			  f"\nThere is no file named {self.file}"


class FileHandler(object):
	"""
	An object to handle the reading of files, and subsequent pasing of data to the Intrp object\n
	@param self: object\n
	@param file: str
	"""
	def read_file(self, file_name: str) -> list[chr]:
		if not isfile(file_name):
			raise PathError(file_name)
		black_list: list[chr] = [ ' ', '\t', '\n' ]
		r: list[chr] = []
		with open(file_name, 'r') as r_file:
			for line in r_file.readlines():
					r += [ c for c in line if c not in black_list  ]
		return r

	def write_file(self, file_name: str, inpt: str) -> ():
		if isfile(file_name):
			print("This file already exist.\nDo you want to overwrite it?\n")
			uInput = input("[y/N]: ")
			if uInput.lower() == 'n' or not uInput:
				raise PathError(file_name)
		with open(file_name, 'w') as w_file:
			w_file.write(inpt)
		return