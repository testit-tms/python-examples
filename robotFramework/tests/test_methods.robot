*** Settings ***
Documentation      Method tests
Library            testit_adapter_robotframework.TMSLibrary
Library            steps.py

*** Variables ***
&{SIMPLE_LINK01}             url=https://test01.example   title=Example01     type=Issue   description=Example01 description
&{SIMPLE_LINK02}             url=https://test02.example   title=Example02     type=Issue   description=Example02 description

@{LINKS}               ${SIMPLE_LINK01}   ${SIMPLE_LINK02}

*** Test Cases ***
Add links success
    Add Links    @{LINKS}
    Return True

Add links failed
    Add Links    @{LINKS}
    Return False

Add attachments success
    Add Attachment    Content    file01.txt
    Add Attachments    ../resources/attachments/file02.txt
    Add Attachments    ../resources/attachments/file03.txt    ../resources/attachments/file04.txt
    Return True

Add attachments failed
    Add Attachment    Content    file01.txt
    Add Attachments    ../resources/attachments/file02.txt
    Add Attachments    ../resources/attachments/file03.txt    ../resources/attachments/file04.txt
    Return False

Add message success
    Add Message    Message
    Return True

Add message failed
    Add Message    Message
    Return False

Add all methods success
    Add Links    @{LINKS}
    Add Attachment    Content    file01.txt
    Add Attachments    ../resources/attachments/file02.txt
    Add Attachments    ../resources/attachments/file03.txt    ../resources/attachments/file04.txt
    Add Message    Message
    Return True

Add all methods failed
    Add Links    @{LINKS}
    Add Attachment    Content    file01.txt
    Add Attachments    ../resources/attachments/file02.txt
    Add Attachments    ../resources/attachments/file03.txt    ../resources/attachments/file04.txt
    Add Message    Message
    Return False
