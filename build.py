from os import system, path
from src import main


def setup() -> None: # Sets the PYTHONSTARTUP to the absolute path of /src/main.py.
	main_path: str = path.realpath(main.__file__)
	
	fail: int = system(f'setx PYTHONSTARTUP "{main_path}" /M >nul 2>&1')

	if fail:
		print(f'Failed to set PYTHONSTARTUP to {main_path}')
	else:
		print(f'Successfully set PYTHONSTARTUP to {main_path}')


if __name__ == '__main__':
	setup()