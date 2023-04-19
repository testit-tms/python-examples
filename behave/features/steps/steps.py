import testit
from behave import then
from behave import when


@then("return true")
def return_true(context):
    assert True


@then("return false")
def return_false(context):
    assert False


@when(u"get parameters {number} {value}")
def get_parameters(context, number: int, value: str):
    pass


@when("step01")
def step01(context):
    pass


@when("add links")
def add_links(context):
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


@when("add attachments")
def add_attachments(context):
    with testit.step('Attachments'):
        testit.addAttachments("Content", True, "file01.txt")
        testit.addAttachments("resources/attachments/file02.txt")

        attachment_paths = ["resources/attachments/file03.txt", "resources/attachments/file04.txt"]
        testit.addAttachments(attachment_paths)


@when("add message")
def add_message(context):
    testit.addMessage("Message")


@when("add all methods")
def add_all_methods(context):
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
        testit.addAttachments("resources/attachments/file02.txt")

        attachment_paths = ["resources/attachments/file03.txt", "resources/attachments/file04.txt"]
        testit.addAttachments(attachment_paths)

    testit.addMessage("Message")
