import pytest
import testit


class TestClass1:
    def setup_method(self):
        with testit.step('Open Chrome browser'):
            pass

    def teardown_method(self):
        with testit.step('Close Chrome browser'):
            pass

    @testit.workItemID(3791)
    @testit.displayName('Authorization tests with test_suite [{test_suite}]')
    @testit.externalID('authorization_test_{test_suite}')
    @testit.title('Authorization')
    @testit.description('E2E_autotest')
    @testit.labels('{labels}')
    @testit.link(type='{link_type}', url='{url}', title='{link_title}')
    @testit.link(type=testit.LinkType.REQUIREMENT, url='https://best-tms.testit.software/projects')
    @testit.link(type=testit.LinkType.BLOCKED_BY, url='https://testit.software/')
    @testit.link(type=testit.LinkType.REPOSITORY, url='https://git.testit.software/users/sign_in')
    @pytest.mark.parametrize('test_suite, labels, url, link_type, link_title', [
        ('suite 3', ['E2E', 'Auth'], 'https://dumps.example.com/module/JCP-15593', testit.LinkType.DEFECT, 'JCP-15593'),
        ('suite 5', (), 'https://github.com/testit-tms/autotest-integration-python', testit.LinkType.RELATED,
         'Integration python')
    ])
    @pytest.mark.tag
    def test_authorization(self, test_suite, labels, url, link_type, link_title):
        testit.addLink(url="http://best-tms.testit.software/", title="Тестируемый продукт")
        with testit.step('Log in the system', 'system authentication'):
            pass
        with testit.step('Create a project', 'the project was created'):
            with testit.step('Enter the project', 'the contents of the project are displayed'):
                assert True
            with testit.step('Create a section', 'section was created'):
                assert True
            with testit.step('Create a tests case', 'tests case was created'):
                assert True


class TestClass2:
    def setup_method(self):
        with testit.step('Open Chrome browser'):
            pass

    def teardown_method(self):
        with testit.step('Close Chrome browser'):
            pass

    @testit.workItemID(3788)
    @testit.displayName('Load files tests')
    @testit.externalID('load_files_test')
    @testit.title('Attachments')
    @testit.description('E2E_autotest')
    @testit.labels('E2E', 'File')
    # @pytest.mark.tag
    @pytest.mark.mag
    def test_load_files(self):
        testit.addLink(url="http://best-tms.testit.software/", title="Тестируемый продукт")
        authorization('admin', 'Qwerty123')
        with testit.step('Attachments'):
            testit.addAttachments("123", True)
            testit.addAttachments('tests/pictures/picture.jpg')
            load_attachment('tests/pictures/picture.jpg')
            load_attachment('tests/docs/document.docx')
            load_attachment('tests/docs/logs.log')
            load_attachment('tests/docs/text_file.txt')
            load_attachment('tests/docs/document.doc')


@testit.step('Log in the system', 'system authentication')
def authorization(username, password):
    assert set_login(username)
    assert set_password(password)


@testit.step
def set_login(username):
    return 'admin' == username


@testit.step
def set_password(password):
    return 'Qwerty123' == password


@testit.step
def load_attachment(file):
    testit.addAttachments(file)
