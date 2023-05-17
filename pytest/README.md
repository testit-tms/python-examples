# Pytest example
Example of tests with Pytest framework and adapter for Test IT

## Setup

1. Install [python version 3.6+](https://www.python.org/downloads/)
2. Clone this repository `git clone https://github.com/testit-tms/python-examples.git && cd pytest`
3. Install dependencies `pip install -r requirements.txt`
4. Run tests via `pytest`
5. Configure the tests to run in **connection_config.ini** file. [How to configure?](https://github.com/testit-tms/adapters-python/tree/main/testit-adapter-pytest#configuration)
6. Run `pytest --testit` to upload the results to TMS

## Project structure

* **tests/** – test files
    * **test_annotations.py** – simple test examples with [annotations testit-adapter-pytest](https://github.com/testit-tms/adapters-python/tree/main/testit-adapter-pytest#decorators)
    * **test_dependency.py** – simple test examples with [pytest dependency](https://pytest-dependency.readthedocs.io/en/stable/usage.html#using-pytest-dependency)
    * **test_methods.py** – simple test examples with [methods testit-adapter-pytest](https://github.com/testit-tms/adapters-python/tree/main/testit-adapter-pytest#decorators)
    * **test_steps.py** – simple test examples with [steps testit-adapter-pytest](https://github.com/testit-tms/adapters-python/tree/main/testit-adapter-pytest#decorators)
* **connection_config.ini** - configuration file where specified base options for tests
* **requirements.txt** - list of items to be installed
