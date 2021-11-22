from enum import Enum, auto
from sys import exit


if __name__ == "__main__":
	exit()


class TokenError(Exception):
	def __init__(self, char: chr, ptr: int):
		self.char = char
		self.ptr = ptr

	def __str__(self) -> str:
		return f"\nAn invalid token was found as position: {self.ptr}" \
			   f"\nInvalid Token: {self.char}" \
			   "\nValid Tokens: '+', '-', '[', ']', '.', ','"


class Token(Enum):
	T_incroment = auto()
	T_decroment = auto()
	T_incro_ptr = auto()
	T_decro_ptr = auto()
	T_strt_loop = auto()
	T_stop_loop = auto()
	T_getu_inpt = auto()
	T_dump_cptr = auto()


class Intrp(object):
	"""
	Object used for the interpreted version of the brainfuck language\n
	@param self: 		object\n
	@param inpt: 		list[chr]\n
	@param buff_size: 	int, Default = 3000
	"""
	def __init__(self, inpt: list[chr], buff_size: int=30000):
		self.buff: list[int] = [ 0 for _ in range(buff_size) ]
		self.buff_size = buff_size
		self.action: list[Token] = self._gen_tokens(inpt)
		self.out: str = ""

	def _gen_tokens(self, inpt: list[chr]) -> list[Token]:
		"""
		Takes the objects inpt and create a list of Tokens from it\n
		@param self: 	object\n
		@param inpt: 	list[chr]\n
		@return: 		list[Token]
		"""
		r: list[Token] = []
		for i, val in enumerate(inpt):
			match val:
				case '+':
					r.append(Token.T_incroment)
				case '-':
					r.append(Token.T_decroment)
				case '.':
					r.append(Token.T_dump_cptr)
				case ',':
					r.append(Token.T_getu_inpt)
				case '<':
					r.append(Token.T_decro_ptr)
				case '>':
					r.append(Token.T_incro_ptr)
				case '[':
					r.append(Token.T_strt_loop)
				case ']':
					r.append(Token.T_stop_loop)
				case _:
					raise TokenError(val, i)
		return r

	def write_buff(self) -> None:
		"""
		Loops over the Tokens and generates the buffer.\n
		@param self: object\n
		@return: None
		"""
		action_idx: int = 0
		buff_idx: int = 0
		while (action_idx < len(self.action)):
			token: Tokne = self.action[action_idx]
			if token == Token.T_incroment:
				self.buff[buff_idx] += 1
			elif token == Token.T_decroment:
				self.buff[buff_idx] -= 1
			elif token == Token.T_incro_ptr:
				buff_idx += 1
			elif token == Token.T_decro_ptr:
				buff_idx -= 1
			elif token == Token.T_dump_cptr:
				self.out += chr(self.buff[buff_idx])
			elif token == Token.T_getu_inpt:
				self._get_user_input()
			elif token == Token.T_strt_loop:
				strt: int = action_idx
				end: int = self.action[i:].index(Token.T_stop_loop)
				action_idx = self._loop(strt, end)
			action_idx += 1
		return


	def _get_user_input(self, inpt: int) -> None:
		u_input: str = input("$ ")

		return

	def _loop(self, start_idx: int, stop_idx: int) -> int:
		return

	@classmethod
	def from_string(cls, inpt: str, buff_size: int = 3000) -> None:
		h: list[chr] = [ c for c in inpt ]
		r: object = cls(inpt, buff_size)
		return r
