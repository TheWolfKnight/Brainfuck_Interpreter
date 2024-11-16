from typing import Optional
from error import UnclosedLoopError, TokenError
from sys import exit


if __name__ == "__main__":
    exit()


class Intrp(object):
    """
    Object used for the interpreted version of the brainfuck language\n
    @param self:        object\n
    @param inpt:        list[chr]\n
    @param buff_size:   int, Default = 3000
    """
    def __init__(self, inpt: list[chr], buff_size: int=30000):
        if not self._validate_input(inpt):
            raise Exception("Invalid input exception")

        self.buff: list[int] = [ 0 for _ in range(buff_size) ]
        self.buff_size = buff_size
        self.depth: int = 0
        self.actions = inpt
        self.action_idx: int = 0
        self.buff_idx: int = 0
        self.out: str = ""
        self.loop_buffer = []

    def _interp_chr(self, token: chr) -> None:
        if token == '+':
            self.buff[self.buff_idx] += 1
            if self.buff[self.buff_idx] > 255:
                self.buff[self.buff_idx] = 0
        elif token == '-':
            self.buff[self.buff_idx] -= 1
            if self.buff[self.buff_idx] < 0:
                self.buff[self.buff_idx] = 255
        elif token == '>':
            self.buff_idx += 1
            if self.buff_idx > self.buff_size:
                raise IndexError
        elif token == '<':
            self.buff_idx -= 1
            if self.buff_idx < 0:
                raise IndexError
        elif token == '[':
            self.loop_buffer.append(self.action_idx)
        elif token == ']':
            if self.buff[self.buff_idx] != 0:
                self.action_idx = self.loop_buffer[-1]
            else:
                self.loop_buffer.pop()
        elif token == '.':
            self.out += chr(self.buff[self.buff_idx])
        elif token == ',':
            self._get_user_input()
        return

    def write_buff(self) -> None:
        """
        Loops over the Tokens and generates the buffer.\n
        @param self: object\n
        @return:     None
        """
        while self.action_idx < len(self.actions):
            token: chr = self.actions[self.action_idx]
            self._interp_chr(token)
            self.action_idx += 1
        return

    def _get_user_input(self) -> None:
        u_input: str = input("$ ")
        assert len(u_input) == 1, "Can only accept one char at a time."
        self.buff[self.buff_idx] = ord(u_input) 
        return

    def _validate_input(self, inpt: list[chr]) -> bool:
        depth: int = 0
        for idx, char in enumerate(inpt):
            if char == '[':
                depth += 1
            elif char == ']':
                depth -= 1

        return depth == 0
