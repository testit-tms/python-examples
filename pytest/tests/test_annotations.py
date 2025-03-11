import pytest
import testit


def test_without_annotations_success():
    assert True


def test_without_annotations_failed():
    assert False


@testit.externalId("external_id_decorator_success")
def test_with_external_id_decorator_success():
    assert True


@testit.externalId("external_id_decorator_failed")
def test_with_external_id_decorator_failed():
    assert False


@testit.displayName("display_name_decorator_success DisplayName")
def test_with_display_name_decorator_success():
    assert True


@testit.displayName("display_name_decorator_failed DisplayName")
def test_with_display_name_decorator_failed():
    assert False


@testit.title("title_decorator_success Title")
def test_with_title_decorator_success():
    assert True


@testit.title("title_decorator_failed Title")
def test_with_title_decorator_failed():
    assert False


@testit.description("description_decorator_success")
def test_with_description_decorator_success():
    assert True


@testit.description("description_decorator_failed")
def test_with_description_decorator_failed():
    assert False


@testit.labels("Label1", "Label2")
def test_with_labels_decorator_success():
    assert True


@testit.labels("Label1", "Label2")
def test_with_labels_decorator_failed():
    assert False


@testit.links(links=[
    {'url': 'https://test01.example', 'type': testit.LinkType.ISSUE, 'title': 'Example01', 'description': 'Example01 description'},
    {'url': 'https://test02.example', 'type': testit.LinkType.ISSUE, 'title': 'Example02', 'description': 'Example02 description'}
])
def test_with_links_decorator_success():
    assert True


@testit.links(links=[
    {'url': 'https://test01.example', 'type': testit.LinkType.ISSUE, 'title': 'Example01', 'description': 'Example01 description'},
    {'url': 'https://test02.example', 'type': testit.LinkType.ISSUE, 'title': 'Example02', 'description': 'Example02 description'}
])
def test_with_links_decorator_failed():
    assert False


@testit.workItemIds("427", 428)
def test_with_work_item_ids_decorator_success():
    assert True


@testit.workItemIds("123", 321)
def test_with_work_item_ids_decorator_failed():
    assert False


@testit.externalId("with_all_decorators_success")
@testit.displayName("with_all_decorators_success DisplayName")
@testit.title("with_all_decorators_success Title")
@testit.description("with_all_decorators_success")
@testit.labels("Label1", "Label2")
@testit.workItemIds("427", 428)
@testit.links(links=[
    {'url': 'https://test01.example', 'type': testit.LinkType.ISSUE, 'title': 'Example01', 'description': 'Example01 description'},
    {'url': 'https://test02.example', 'type': testit.LinkType.ISSUE, 'title': 'Example02', 'description': 'Example02 description'}
])
def test_with_all_decorators_success():
    assert True


@testit.externalId("with_all_decorators_failed")
@testit.displayName("with_all_decorators_failed DisplayName")
@testit.title("with_all_decorators_failed Title")
@testit.description("with_all_decorators_failed")
@testit.labels("Label1", "Label2")
@testit.workItemIds("123", 321)
@testit.links(links=[
    {'url': 'https://test01.example', 'type': testit.LinkType.ISSUE, 'title': 'Example01', 'description': 'Example01 description'},
    {'url': 'https://test02.example', 'type': testit.LinkType.ISSUE, 'title': 'Example02', 'description': 'Example02 description'}
])
def test_with_all_decorators_failed():
    assert False


@testit.externalId("with_parameters_success_{number}_{text}")
@testit.displayName("with_parameters_success DisplayName {number} {text}")
@testit.title("with_parameters_success Title {number} {text}")
@pytest.mark.parametrize('number, text', [
    (1, "string1"),
    (2, "string2"),
    (3, "string3"),
    pytest.param(4, "string4", marks=pytest.mark.skip(reason="bug test"))
])
def test_with_parameters_success(number: int, text: str):
    assert True


@testit.externalId("with_parameters_failed_{number}_{text}")
@testit.displayName("with_parameters_failed DisplayName {number} {text}")
@testit.title("with_parameters_failed Title {number} {text}")
@pytest.mark.parametrize('number, text', [
    (1, "string1"),
    (2, "string2"),
    (3, "string3"),
    pytest.param(4, "string4", marks=pytest.mark.skip(reason="bug test"))
])
def test_with_parameters_failed(number: int, text: str):
    assert False
