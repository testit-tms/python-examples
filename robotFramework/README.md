# Robot Framework example
Example of tests with Robot Framework and adapter for Test IT

## Setup

1. Install [python version 3.6+](https://www.python.org/downloads/)
2. Clone this repository `git clone https://github.com/testit-tms/python-examples.git && cd robotFramework`
3. Install dependencies `pip install -r requirements.txt`
4. Run tests via `robot tests`
5. Configure the tests to run in **connection_config.ini** file. [How to configure?](https://github.com/testit-tms/adapters-python/tree/main/testit-adapter-robotframework#configuration)
6. Run `robot -v testit tests` to upload the results to TMS

## Project structure

* **tests/** – test files
    * **steps.py** – simple steps with [Robot Framework keywords](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-keywords) and [step method testit-adapter-robotframework](https://github.com/testit-tms/adapters-python/tree/main/testit-adapter-robotframework#tags)
    * **test_annotations.robot** – simple test examples with [annotations testit-adapter-robotframework](https://github.com/testit-tms/adapters-python/tree/main/testit-adapter-robotframework#tags)
    * **test_methods.robot** – simple test examples with [methods testit-adapter-robotframework](https://github.com/testit-tms/adapters-python/tree/main/testit-adapter-robotframework#tags)
    * **test_steps.robot** – simple test examples with steps from **steps.py**
* **connection_config.ini** - configuration file where specified base options for tests
* **requirements.txt** - list of items to be installed
