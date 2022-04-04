# facts
### Learn a random fact whenever you open a Python interpreter.

![Sample Image 1](./misc/sample1.png "Sample Image 1")
![Sample Image 2](./misc/sample2.png "Sample Image 2")

## Notes
* *facts* is currently available to Windows OS only.
* Building *facts* overwrites the content of the `PYTHONSTARTUP` system environment
  variable to the filepath of `main.py`. Check if `PYTHONSTARTUP` is assigned to
  a necessary Python script before building *facts*.

## Setup
1. Clone this repo within your local directory via 
   `git clone https://github.com/Marshblocker/facts`.

2. (**Important**) Run the command-line (`cmd`/`Powershell`) as an Administrator, `cd` to 
   `your/local/directory/facts/`, run `python build.py`, then exit the command-line.
   **Note:** Whenever the path of the `facts` directory changes, you always 
   need to repeat step 2.

3. Setup is done. *facts* will run everytime you use a Python interpreter.

## Acknowledgements

Contents of `/src/facts_pool.txt` forked from [assaf's dailyhi/facts.txt](https://github.com/assaf/dailyhi/blob/master/facts.txt).

## License
*facts* is released under the [MIT License](https://opensource.org/licenses/MIT).
