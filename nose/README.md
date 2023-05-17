# Nose example
Example of tests with Nose framework and adapter for Test IT

## Setup

1. Install [python version 3.6+](https://www.python.org/downloads/)
2. Clone this repository `git clone https://github.com/testit-tms/python-examples.git && cd nose`
3. Install dependencies `pip install -r requirements.txt`
4. Run tests via `nose2`
5. Configure the tests to run in **connection_config.ini** file. [How to configure?](https://github.com/testit-tms/adapters-python/tree/main/testit-adapter-nose#configuration)
6. Run `nose2 --testit` to upload the results to TMS

## Project structure

* **tests/** – test files
    * **test_annotations.py** – simple test examples with [annotations testit-adapter-nose](https://github.com/testit-tms/adapters-python/tree/main/testit-adapter-nose#decorators)
    * **test_methods.py** – simple test examples with [methods testit-adapter-nose](https://github.com/testit-tms/adapters-python/tree/main/testit-adapter-nose#decorators)
    * **test_steps.py** – simple test examples with [steps testit-adapter-nose](https://github.com/testit-tms/adapters-python/tree/main/testit-adapter-nose#decorators)
* **connection_config.ini** - configuration file where specified base options for tests
* **requirements.txt** - list of items to be installed
* **unittest.cfg** - configuration file for [Nose](https://docs.nose2.io/en/latest/configuration.html)
