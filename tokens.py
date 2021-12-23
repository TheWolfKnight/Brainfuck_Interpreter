from abc import ABC


if __name__ == "__main__":
    exit()


class BaseToken(ABC):
    pass


class T_incroment(BaseToken):
    pass


class T_decroment(BaseToken):
    pass


class T_incro_ptr(BaseToken):
    pass


class T_decro_ptr(BaseToken):
    pass


class T_strt_loop(BaseToken):
    def __init__(self, depth: int):
        self.depth = depth

    def __eq__(self, other) -> bool:
        return self.depth == other.depth


class T_stop_loop(BaseToken):
    def __init__(self, depth: int):
        self.depth = depth

    def __eq__(self, other) -> bool:
        return self.depth == other.depth


class T_getu_inpt(BaseToken):
    pass


class T_dump_cptr(BaseToken):
    pass
