from exercises.exercise_1_uppercase_letters.extract_uppercase_letters import extract_uppercase_letters


def test_no_uppercase_letters():
    sentence = 'ala ma kota'
    expected = ''

    result = extract_uppercase_letters(sentence=sentence)

    assert expected == result


def test_empty_string():
    sentence = ''
    expected = ''

    result = extract_uppercase_letters(sentence=sentence)

    assert expected == result


def test_sentence_with_uppercase_letters():
    sentence = 'Ala Ma Kota a Kota ma Ale'
    expected = 'AMKKA'

    result = extract_uppercase_letters(sentence=sentence)

    assert result == expected
