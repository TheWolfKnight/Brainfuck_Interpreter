from enum import Enum, auto
from tokens import *
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


class UnclosedLoopError(Exception):
    def __init__(self, pos: int):
        self.pos = pos

    def __str__(self) -> str:
        return f"\nA loop was initialze but never closed." \
               f"\nInvalid loop pos: {self.pos}"


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
        self.depth: int = 0
        self.action: list[BaseToken] = self._gen_tokens(inpt)
        self.action_idx: int = 0
        self.buff_idx: int = 0
        self.out: str = ""


    def _gen_tokens(self, inpt: list[chr]) -> list[BaseToken]:
        """
        Takes the objects inpt and create a list of Tokens from it\n
        @param self: 	object\n
        @param inpt: 	list[chr]\n
        @return: 		list[Token]
        """
        r: list[BaseToken] = []
        for idx, val in enumerate(inpt):
            match val:
                case '+':
                    r.append(T_incroment())
                case '-':
                    r.append(T_decroment())
                case '.':
                    r.append(T_dump_cptr())
                case ',':
                    r.append(T_getu_inpt())
                case '<':
                    r.append(T_decro_ptr())
                case '>':
                    r.append(T_incro_ptr())
                case '[':
                    r.append(T_strt_loop(self.depth))
                    self.depth += 1
                case ']':
                    self.depth -= 1
                    r.append(T_stop_loop(self.depth))
                case _:
                    raise TokenError(val, idx)
        return r

    def _interp_token(self, token: BaseToken) -> None:
        tp = type(token)
        if tp == T_incroment:
            self.buff[self.buff_idx] += 1
        elif tp == T_decroment:
            self.buff[self.buff_idx] -= 1
        elif tp == T_incro_ptr:
            self.buff_idx += 1
            if self.buff_idx > self.buff_size:
                raise IndexError
        elif tp == T_decro_ptr:
            self.buff_idx -= 1
            if self.buff_idx < 0:
                raise IndexError
        elif tp == T_strt_loop:
            start: int = self.action_idx
            end: int = None
            for idx, t in enumerate(self.action[self.action_idx:]):
                if type(t) == T_stop_loop \
                   and token.depth == t.depth:
                    end = self.action_idx + idx
                    break
            if end == None:
                raise UnclosedLoopError(start)
            print(f"{self.action_idx=}, {end=}")
            self._loop(self.action_idx, t.depth)
            self.action_idx = end
        elif tp == T_dump_cptr:
            print("buff dump hit", self.buff[self.buff_idx])
            self.out += chr(self.buff[self.buff_idx])
        elif tp == T_getu_inpt:
            self._get_user_input()
        return

    def write_buff(self) -> None:
        """
        Loops over the Tokens and generates the buffer.\n
        @param self: 	object\n
        @return: 		None
        """
        while self.action_idx < len(self.action):
            print(f"[{self.action_idx=}, {self.action[self.action_idx]=}" \
                  f" {self.buff_idx=}, {self.buff[self.buff_idx]=}]")
            token: BaseToken = self.action[self.action_idx]
            self._interp_token(token)
            self.action_idx += 1
        return

    def _get_user_input(self) -> None:
        u_input: str = input("$ ")
        assert len(u_input) == 1, "Can only accept one char at a time."
        self.buff[self.buff_idx] = ord(u_input) 
        return

    def _loop(self, start_idx: int, end_depth: int) -> None:

        self.action_idx += 1

        while True:
            self._interp_token(self.action[self.action_idx])
            print(f"[{self.action_idx=}, {self.action[self.action_idx]=}" \
                  f" {self.buff_idx=}, {self.buff[self.buff_idx]=}")
            if type(self.action[self.action_idx]) == T_stop_loop \
               and self.action[self.action_idx].depth == end_depth:
                if not self.buff[self.buff_idx]:
                    break
                self.action_idx = start_idx
            else:
                self.action_idx += 1

        # while self.buff[self.buff_idx]:
        #     for i in range(1, stop_idx+1, 1):
        #         locale_action_idx: int = self.action_idx + i
        #         print(f"[{locale_action_idx=}, {self.action[locale_action_idx]=}" \
        #               f" {self.buff_idx=}, {self.buff[self.buff_idx]=}")
        #         self._interp_token(self.action[locale_action_idx])
        return
