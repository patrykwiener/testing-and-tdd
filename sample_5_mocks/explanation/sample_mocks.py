from unittest.mock import Mock, MagicMock


class Sample:
    def __init__(self):
        self.sample_str = ...
        self.sample_number = ...

    def some_method(self):
        pass


def mock1():
    sample = Sample()
    sample.sample_str
    sample.sample_number

    mock = Mock()
    mock.sample_str = 'sample_str'
    mock.ala_ma_kota = 'sample_str'
    mock.sample_number = 10

    print(mock.sample_number)
    print(mock.sample_str)

    mock.some_method()
    t = 0


def add_number(num1, num2):
    return num1 + num2


def mock2():
    mock = Mock(return_value=20)
    mock(15, 5)
    assert mock.return_value == 20
    assert mock() == 20

    mock.get_balance.return_value = 20
    mock.get_balance()

    mock.some_method = Mock(return_value='mocked_method_value')
    assert mock.some_method() == 'mocked_method_value'

    mock.some_method()
    assert mock.some_method.call_count == 2


def mock3():
    mock = Mock()
    mock.method_with_exception = Mock(side_effect=Exception('some_msg'))
    mock.method_with_exception()  # raises Exception


def magic_mock1():
    magic_mock = MagicMock()
    magic_mock.sample_str = 'sample_str'
    magic_mock.sample_number = 10
    magic_mock.some_method()

    assert magic_mock.__len__() == 0
    assert len(magic_mock) == 0


if __name__ == '__main__':
    mock1()
    mock2()
    # mock3()
    # magic_mock1()
    # b = Mock()

    mock = MagicMock()
    mock('test', 123)
    mock.assert_called()
    mock.assert_called_with('test', 123)
    mock.assert_called_once()
    mock.assert_called_once_with('test', 123)
