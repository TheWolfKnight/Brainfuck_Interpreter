

if __name__ == "__main__":
    exit()


class PathError(Exception):
    def __init__(self, file: str):
        self.file = file

    def __str__(self) -> str:
        return "\nAn error occured with the given file" \
              f"\nThere is no file named {self.file}"


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
