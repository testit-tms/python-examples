import pytest


@pytest.mark.dependency()
@pytest.mark.xfail(reason="deliberate fail")
def test_a_failed():
    assert False


@pytest.mark.dependency()
def test_b_success():
    pass


@pytest.mark.dependency(depends=["test_a"])
def test_c_success():
    pass


@pytest.mark.dependency(depends=["test_b"])
def test_d_success():
    pass


@pytest.mark.dependency(depends=["test_b", "test_c"])
def test_e_success():
    pass
