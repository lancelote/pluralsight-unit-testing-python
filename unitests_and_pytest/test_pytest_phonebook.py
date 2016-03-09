# coding=utf-8

""""
Phonebook tests via pytest
"""

import pytest

from unitests_and_pytest.phonebook import Phonebook


@pytest.fixture
def phonebook(tmpdir):
    """Provides and empty Phonebook"""
    phonebook = Phonebook(tmpdir)
    return phonebook


def test_add_and_lookup_entry(phonebook):
    pytest.skip('WIP')
    phonebook.add('Bob', '123')
    assert '123' == phonebook.lookup('Bob'), 'Bob not found'


def test_phonebook_gives_access_to_names_and_numbers(phonebook):
    phonebook.add('Alice', '12345')
    assert 'Alice' in phonebook.get_names()
    assert '12345' in phonebook.get_numbers()


def test_missing_entry_raises_key_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup('missing')
