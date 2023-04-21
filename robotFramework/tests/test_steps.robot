*** Settings ***
Documentation      Step tests
Library            testit_adapter_robotframework.TMSLibrary
Library            steps.py

*** Test Cases ***
Steps success
    Step01
    Return True

Steps failed
    Step01
    Return False
