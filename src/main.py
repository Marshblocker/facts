from random import choice
from math import floor, ceil
from os.path import basename
from os import environ


FACTS_TXT_FILE_NAME = 'facts_pool.txt'


def main() -> None:
	filepath: str = environ['PYTHONSTARTUP'].partition(basename(__file__))[0] + \
			   FACTS_TXT_FILE_NAME  # get absolute path of FACTS_TXT_FILE_NAME.

	with open(filepath, mode= 'r') as f:
		fact: str = choice(f.readlines()).rstrip('\n')

	len_ = len(fact)

	print("")
	print('╔' + '═' * (floor(len_ / 2) - 7) + ' RANDOM FACT! '
		      + '═' * (ceil(len_ / 2) - 7) + '╗'
	)
	print('║' + fact + '║')
	print('╚' + '═' * len_ + '╝')
	print(" ")


if __name__ == '__main__':
	main()