# facts
### Enjoy a random fact whenever you open a Python Interactive Environment.

![Sample Image 1](./misc/sample1.png "Sample Image 1")
![Sample Image 2](./misc/sample2.png "Sample Image 2")

## Notes
* *facts* is currently available to Windows OS only.
* Building *facts* overwrites the content of the `PYTHONSTARTUP` system environment
  variable to the filepath of `main.py`. Check if `PYTHONSTARTUP` is assigned to
  a necessary Python script before building *facts*.

## Setup
1. Make sure you have Python installed, preferably Python 3+. Visit 
   [this link](https://www.python.org/downloads/) to download the latest version
   of Python.

2. Clone this repo within your local directory via 
   `git clone https://github.com/Marshblocker/facts`.

3. (**Important**) Run `cmd` as an Administrator and, `cd` to 
   `your/local/directory/facts/`, execute `python build.py`, then exit `cmd`.
   If ever you will change the location of the `facts` directory, you **always 
   need to repeat this step**[^1].

4. Setup is done. *facts* will run everytime you enter `python` in `cmd` or
   open the built-in Python shell. 

## Acknowledgements

Contents of `/src/facts_pool.txt` forked from [assaf's dailyhi/facts.txt](https://github.com/assaf/dailyhi/blob/master/facts.txt). Thanks.

## License
*facts* is released under the [MIT License](https://opensource.org/licenses/MIT).

[^1] If you do not repeat step 3, the interpreter will not see the updated
     filepath of `main.py` and will raise a FileNotFoundError.