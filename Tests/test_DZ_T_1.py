import pytest
from trace import Trace
from app_for_test_1 import get_name, Directory

def test_get_name_1():
    assert get_name('10006') == 'Аристарх Павлов'

@pytest.mark.xfail
def test_get_name_2():
    assert get_name('10006') == 'Ася Монина'

@pytest.mark.skipif(Trace, reason='Боевой сервер')
def test_get_name_3():
    assert get_name('10006') == 'Вася Пупкин'

@pytest.mark.parametrize(
    'arg,expected',
    (
            ("10006", "Аристарх Павлов"),
            ("11-2", "Геннадий Покемонов"),
            ("2207 876234", "Василий Гупкин"),
    )
)
def test_get_name_params(arg, expected):
    assert get_name(arg) == expected

@pytest.fixture
def create_directory():
    directory = Directory('Base')
    return directory

def test_add_content(create_directory):
    directory = create_directory
    return len(directory.add
        (
        'international passport',
        '311 020203',
        'Александр Пушкин',
        3)
    ) == 4

def test_check_item(create_directory):
    directory = create_directory
    return directory.get_directory('10006') == 2

def test_directory_name(create_directory):
    directory = create_directory
    return directory.dir_name == 'Base'

