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
	def __init__(self, file: str):
		if (isfile(file)):
			self.file = file
		else:
			raise PathError(file)

	def read_file(self) -> list[chr]:
		black_list: list[chr] = [ ' ', '\t', '\n' ]
		r: list[chr] = []
		with open(self.file, 'r') as r_file:
			for line in r_file.readline():
				r += [ c for c in line if c not in black_list ]
		return r
