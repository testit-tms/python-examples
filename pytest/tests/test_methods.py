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
    testit.addAttachments("../resources/attachments/file02.txt")

    attachment_paths = ["../resources/attachments/file03.txt", "../resources/attachments/file04.txt"]
    testit.addAttachments(attachment_paths)

    assert True


def test_with_add_attachments_method_failed():
    testit.addAttachments("Content", True, "file01.txt")
    testit.addAttachments("../resources/attachments/file02.txt")

    attachment_paths = ["../resources/attachments/file03.txt", "../resources/attachments/file04.txt"]
    testit.addAttachments(attachment_paths)

    assert False


def test_with_add_message_method_success():
    testit.addMessage("Message")

    assert True


def test_with_add_message_method_failed():
    testit.addMessage("Message")

    assert False


def test_with_add_work_item_ids_method_success():
    testit.addWorkItemIds("427", 428)

    assert True


def test_with_add_work_item_ids_method_failed():
    testit.addWorkItemIds("123", 321)

    assert False


def test_with_add_display_name_method_success():
    testit.addDisplayName("add_display_name_method_success DisplayName")

    assert True


def test_with_add_display_name_method_failed():
    testit.addDisplayName("add_display_name_method_failed DisplayName")

    assert False


def test_with_add_namespace_method_success():
    testit.addNameSpace("add_namespace_method_success NameSpace")

    assert True


def test_with_add_namespace_method_failed():
    testit.addNameSpace("add_namespace_method_failed NameSpace")

    assert False


def test_with_add_classname_method_success():
    testit.addClassName("add_classname_method_success ClassName")

    assert True


def test_with_add_classname_method_failed():
    testit.addClassName("add_classname_method_failed ClassName")

    assert False


def test_with_add_external_id_method_success():
    testit.addExternalId("add_external_id_method_success")

    assert True


def test_with_add_external_id_method_failed():
    testit.addExternalId("add_external_id_method_failed")

    assert False


def test_with_add_title_method_success():
    testit.addTitle("add_title_method_success Title")

    assert True


def test_with_add_title_method_failed():
    testit.addTitle("add_title_method_failed Title")

    assert False


def test_with_add_description_method_success():
    testit.addDescription("add_description_method_success Description")

    assert True


def test_with_add_description_method_failed():
    testit.addDescription("add_description_method_failed Description")

    assert False


def test_with_add_label_method_success():
    testit.addLabels("Label1", "Label2")

    assert True


def test_with_add_label_method_failed():
    testit.addLabels("Label1", "Label2")

    assert False


def test_with_add_parameter_method_success():
    testit.addParameter("name_parameter_success1", "value_parameter_success1")
    testit.addParameter("name_parameter_success2", "value_parameter_success2")

    assert True


def test_with_add_parameter_method_failed():
    testit.addParameter("name_parameter_failed1", "value_parameter_failed1")
    testit.addParameter("name_parameter_failed2", "value_parameter_failed2")

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
    testit.addAttachments("../resources/attachments/file02.txt")

    attachment_paths = ["../resources/attachments/file03.txt", "../resources/attachments/file04.txt"]
    testit.addAttachments(attachment_paths)

    testit.addMessage("Message")
    testit.addWorkItemIds("427", 428)
    testit.addDisplayName("with_all_methods_success DisplayName")
    testit.addNameSpace("with_all_methods_success NameSpace")
    testit.addClassName("with_all_methods_success ClassName")
    testit.addExternalId("with_all_methods_success")
    testit.addTitle("with_all_methods_success Title")
    testit.addDescription("with_all_methods_success Description")
    testit.addLabels("Label1", "Label2")
    testit.addParameter("name_parameter_success1", "value_parameter_success1")
    testit.addParameter("name_parameter_success2", "value_parameter_success2")

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
    testit.addAttachments("../resources/attachments/file02.txt")

    attachment_paths = ["../resources/attachments/file03.txt", "../resources/attachments/file04.txt"]
    testit.addAttachments(attachment_paths)

    testit.addMessage("Message")
    testit.addWorkItemIds("123", 321)
    testit.addDisplayName("with_all_methods_failed DisplayName")
    testit.addNameSpace("with_all_methods_failed NameSpace")
    testit.addClassName("with_all_methods_failed ClassName")
    testit.addExternalId("with_all_methods_failed")
    testit.addTitle("with_all_methods_failed Title")
    testit.addDescription("with_all_methods_failed Description")
    testit.addLabels("Label1", "Label2")
    testit.addParameter("name_parameter_failed1", "value_parameter_failed1")
    testit.addParameter("name_parameter_failed2", "value_parameter_failed2")

    assert False
