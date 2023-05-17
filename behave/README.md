# Behave example
Example of tests with Behave framework and adapter for Test IT

## Setup

1. Install [python version 3.6+](https://www.python.org/downloads/)
2. Clone this repository `git clone https://github.com/testit-tms/python-examples.git && cd behave`
3. Install dependencies `pip install -r requirements.txt`
4. Run tests via `behave`
5. Configure the tests to run in **connection_config.ini** file. [How to configure?](https://github.com/testit-tms/adapters-python/tree/main/testit-adapter-behave#configuration)
6. Run `behave -f testit_adapter_behave.formatter:AdapterFormatter` to upload the results to TMS

## Project structure

* **features/** – test files
    * **steps/** – step files
        * **steps.py** – simple [Behave steps](https://behave.readthedocs.io/en/latest/tutorial.html)
    * **annotation-tests.feature** – simple test examples with [annotations testit-adapter-behave](https://github.com/testit-tms/adapters-python/tree/main/testit-adapter-behave#tags)
    * **method-tests.feature** – simple test examples with [methods testit-adapter-behave](https://github.com/testit-tms/adapters-python/tree/main/testit-adapter-behave#tags)
    * **step-tests.feature** – simple test examples with steps from **steps.py**
* **connection_config.ini** - configuration file where specified base options for tests
* **requirements.txt** - list of items to be installed
