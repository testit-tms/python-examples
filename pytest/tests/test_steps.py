import testit


def setup_method():
    with testit.step('Open Chrome browser'):
        pass


@testit.step
def step01():
    pass


@testit.step
def step02(number: int):
    pass


def test_with_steps_without_annotations_success():
    step01()
    step02(2)

    assert True


def test_with_steps_without_annotations_failed():
    step01()
    step02(2)

    assert False


@testit.step("Step03 Title")
def step03():
    pass


@testit.step("Step04 {number} Title")
def step04(number: int):
    pass


def test_with_steps_with_title_annotation_success():
    step03()
    step04(3)

    assert True


def test_with_steps_with_title_annotation_failed():
    step03()
    step04(3)

    assert False


@testit.step("Step05 Title")
def step05():
    pass


@testit.step("Step06 {number} Title")
def step06(number: int):
    pass


def test_with_steps_with_all_annotations_success():
    step05()
    step06(3)

    assert True


def test_with_steps_with_all_annotations_failed():
    step05()
    step06(3)

    assert False


def teardown_method():
    with testit.step('Close Chrome browser'):
        pass
