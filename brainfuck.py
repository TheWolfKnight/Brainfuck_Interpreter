from file_hndl import FileHandler
from intrp import Intrp
from sys import exit, argv


class InvalidFlag(Exception):
	def __init__(self, switch: chr=None, length: int=None,
				 unset_flag: str=None, invalid_respons: str=None):
		self.switch = switch
		self.length = length
		self.unset_flag = unset_flag
		self.invalid_respons = invalid_respons
		self.respons: str = self._generate_report()

	def _generate_report(self) -> str:
		r: str = ""
		match self.switch:
			case 'l':
				r = "\nA flag was not set properly" \
				   f"\nThe length of the arguments were {self.length} expected and even length"
			case 'u':
				r = "\nOne of the flags was not set" \
				   f"\n{self.unset_flag} was not set properly"
			case 'i':
				r = "\nA flags value was not as expected" \
				    f"\n{self.invalid_respons} was not the correct value"
			case _:
				raise SyntaxError
		return r

	def __str__(self) -> str:
		return self.respons


def test_env():
	obj: FileHandler = FileHandler("./tmp.txt")
	out: list[chr] = obj.read_file()
	interp: Intrp = Intrp(out)
	print(interp.action)
	return


def main():
	test_env()
	return


if __name__ == "__main__":
	if (len(argv)-1 % 2):
		raise InvalidFlag(switch='l', length=len(argv)-1)
	argm: dict = { argv[i]: argv[i+1] for i in range(1, len(argv[1:]), 2) }
	print(argm)
	# main()
	exit()