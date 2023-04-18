import testit


def test_with_add_links_method_success():
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

    assert True


def test_with_add_links_method_failed():
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

    assert False


def test_with_add_attachments_method_success():
    testit.addAttachments("Content", True, "file01.txt")
    testit.addAttachments("resources/docs/document.docx")
    testit.addAttachments("resources/docs/document.doc")
    testit.addAttachments("resources/pictures/png.png")

    attachment_paths = ["resources/pictures/jpg.jpg", "resources/pictures/svgz.jpg", "resources/docs/logs.log"]
    testit.addAttachments(attachment_paths)

    assert True


def test_with_add_attachments_method_failed():
    testit.addAttachments("Content", True, "file01.txt")
    testit.addAttachments("resources/docs/document.docx")
    testit.addAttachments("resources/docs/document.doc")
    testit.addAttachments("resources/pictures/png.png")

    attachment_paths = ["resources/pictures/jpg.jpg", "resources/pictures/svgz.jpg", "resources/docs/logs.log"]
    testit.addAttachments(attachment_paths)

    assert False


def test_with_add_message_method_success():
    testit.addMessage("Message")

    assert True


def test_with_add_message_method_failed():
    testit.addMessage("Message")

    assert False


def test_with_all_methods_success():
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

    testit.addAttachments("Content", True, "file01.txt")
    testit.addAttachments("resources/docs/document.docx")
    testit.addAttachments("resources/docs/document.doc")
    testit.addAttachments("resources/pictures/png.png")

    attachment_paths = ["resources/pictures/jpg.jpg", "resources/pictures/svgz.jpg", "resources/docs/logs.log"]
    testit.addAttachments(attachment_paths)

    testit.addMessage("Message")

    assert True


def test_with_all_methods_failed():
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

    testit.addAttachments("Content", True, "file01.txt")
    testit.addAttachments("resources/docs/document.docx")
    testit.addAttachments("resources/docs/document.doc")
    testit.addAttachments("resources/pictures/png.png")

    attachment_paths = ["resources/pictures/jpg.jpg", "resources/pictures/svgz.jpg", "resources/docs/logs.log"]
    testit.addAttachments(attachment_paths)

    testit.addMessage("Message")

    assert True
