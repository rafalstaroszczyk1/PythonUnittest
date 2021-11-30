import pytest


class Persons:
    def __init__(self, name_list):
        self.name_list = name_list

    def sort_first_letter(self):
        fl_name_list = sorted(self.name_list)
        return list(fl_name_list)

    def sort_last_letter(self):
        ll_name_list = sorted(self.name_list, key=lambda x: x[::-1])
        return list(ll_name_list)

    def sort_length_letter(self):
        len_l_name_list = sorted(self.name_list, key=lambda x: len(x), reverse=True)
        return list(len_l_name_list)


class TestName:

    @pytest.fixture()
    def names(self):
        return ['Alina', 'Ewa', 'Paulina', 'Maciej']

    def test_first_letter(self, names):
        persons = Persons(names)
        assert persons.sort_first_letter() == ['Alina', 'Ewa', 'Maciej', 'Paulina']

    def test_last_letter(self, names):
        persons = Persons(names)
        assert persons.sort_last_letter() == ['Alina', 'Paulina', 'Ewa', 'Maciej']

    def test_length_letter(self, names):
        persons = Persons(names)
        assert persons.sort_last_letter() == ['Alina', 'Paulina', 'Ewa', 'Maciej']

