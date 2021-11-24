from enum import Enum, auto
from time import perf_counter
from sys import exit


if __name__ == "__main__":
	exit()


class TokenError(Exception):
	def __init__(self, char: chr, ptr: int):
		self.char = char
		self.ptr = ptr

	def __str__(self) -> str:
		return f"\nAn invalid token was found at position: {self.ptr}" \
			   f"\nInvalid Token: \"{self.char}\"" \
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
		self.action_idx: int = 0
		self.buff_idx: int = 0
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

	def _interp_token(self, token: Token) -> None:
		match token:
			case Token.T_incroment:
				self.buff[self.buff_idx] += 1
			case Token.T_decroment:
				self.buff[self.buff_idx] -= 1
			case Token.T_incro_ptr:
				self.buff_idx += 1
				if self.buff_idx > self.buff_size:
					raise IndexError
			case Token.T_decro_ptr:
				self.buff_idx -= 1
				if self.buff_idx < 0:
					raise IndexError
			case Token.T_dump_cptr:
				self.out += chr(self.buff[self.buff_idx])
			case Token.T_getu_inpt:
				self._get_user_input()
			case Token.T_strt_loop:
				strt: int = self.action_idx
				end: int = self.action[strt:].index(Token.T_stop_loop)
				self._loop(strt, end)
				self.action_idx = strt + end

	def write_buff(self) -> None:
		"""
		Loops over the Tokens and generates the buffer.\n
		@param self: object\n
		@return: None
		"""
		while (self.action_idx < len(self.action)):
			token: Tokne = self.action[self.action_idx]
			self._interp_token(token)
			self.action_idx += 1
		return

	def _get_user_input(self) -> ():
		u_input: str = input("$ ")
		assert len(u_input) == 1, "Can only accept one char at a time."
		self.buff[self.buff_idx] = ord(u_input) 
		return

	def _loop(self, start_idx: int, stop_idx: int) -> ():
		while (self.buff[self.buff_idx]):
			for i in range(1, stop_idx+1, 1):
				local_action_idx: int = self.action_idx + i
				self._interp_token(self.action[local_action_idx])
		return

	@classmethod
	def from_string(cls, inpt: str, buff_size: int = 3000) -> ():
		h: list[chr] = [ c for c in inpt ]
		r: object = cls(inpt, buff_size)
		return r
