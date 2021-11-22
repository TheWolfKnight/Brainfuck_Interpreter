from sys import exit


class Compiler(object):
	def __init__(self, inpt: list[str]=None):
		self.inpt = self._get_nums(inpt)

	def _get_nums(self, inpt: str) -> list[chr]:
		r: list[int] = []
		for i in range(len(inpt)):
			r.append(ord(inpt[i]))
		return r

	def compile_brainfuck(self) -> str:
		r: str = ""
		for i in self.inpt:
			r += "+"*i
			r += ".>"
		return r
