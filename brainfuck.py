from intrp import Intrp
from sys import exit


def test_env():
	lst: list[chr] = [ '-', '+', '+', '+' ]
	obj: Intrp = Intrp(lst)
	print(obj.action)
	return


def main():
	test_env()
	return


if __name__ == "__main__":
	main()
	exit()