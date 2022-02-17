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
   **If ever you will change the location of the `facts` directory, you always 
   need to repeat this step**<sup>[1](#f1)</sup>.

3. Setup is done. *facts* will run everytime you use a Python interpreter.

## Acknowledgements

Contents of `/src/facts_pool.txt` forked from [assaf's dailyhi/facts.txt](https://github.com/assaf/dailyhi/blob/master/facts.txt). Thanks.

## License
*facts* is released under the [MIT License](https://opensource.org/licenses/MIT).


---
<sub><sup>
<b id="f1">1</b> 
      If you do not repeat step 3, the interpreter will not see the updated
      filepath of `main.py` and will raise a FileNotFoundError. 
</sup></sub>
