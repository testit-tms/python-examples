from robot.api.deco import keyword
import testit


@keyword("Return true")
def return_true():
    assert True


@keyword("Return false")
def return_false():
    assert False


@keyword("Get parameters ${number} ${value}")
def get_parameters(number: int, value: str):
    pass


@keyword("Step01")
def step01():
    pass


@keyword("Add links method")
def add_links():
    testit.addLinks(
        url="https://test01.example",
        title="Example01",
        description="Example01 description",
        type=testit.LinkType.ISSUE)
    testit.addLinks(
        url="https://test02.example",
        title="Example02",
        description="Example02 description",
        type=testit.LinkType.ISSUE)


@keyword("Add attachments method")
def add_attachments():
    with testit.step('Attachments'):
        testit.addAttachments("Content", True, "file01.txt")
        testit.addAttachments("..resources/attachments/file02.txt")

        attachment_paths = ["../resources/attachments/file03.txt", "../resources/attachments/file04.txt"]
        testit.addAttachments(attachment_paths)


@keyword("Add message method")
def add_message():
    testit.addMessage("Message")


@keyword("Add all methods")
def add_all_methods():
    testit.addLinks(
        url="https://test01.example",
        title="Example01",
        description="Example01 description",
        type=testit.LinkType.ISSUE)
    testit.addLinks(
        url="https://test02.example",
        title="Example02",
        description="Example02 description",
        type=testit.LinkType.ISSUE)

    with testit.step('Attachments'):
        testit.addAttachments("Content", True, "file01.txt")
        testit.addAttachments("../resources/attachments/file02.txt")

        attachment_paths = ["../resources/attachments/file03.txt", "../resources/attachments/file04.txt"]
        testit.addAttachments(attachment_paths)

    testit.addMessage("Message")
