from pytest import mark

from src.quiz.quiz import get_letter


@mark.parametrize('test_word', ['', 'a', 'abcdef', '1234'])
class TestGetLetter:

    def test_no_mask(self, test_word):
        result = get_letter(test_word, '')
        expected = '*'*len(test_word)
        assert result == expected

    def test_full_mask(self, test_word):
        result = get_letter(test_word, '*'*len(test_word))
        expected = len(test_word) - 1 if len(test_word) > 0 else 0
        assert result.count('*') == expected

