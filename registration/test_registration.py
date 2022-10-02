import unittest
from reg import Registration


class TestRegistration(unittest.TestCase):

    def setUp(self) -> None:
        self.reg = Registration

    def test_is_include_all_register(self):
        self.assertFalse(self.reg.is_include_all_register('aA'))
        self.assertTrue(self.reg.is_include_all_register('aAA'))
        self.assertTrue(self.reg.is_include_all_register('AAA'))
        self.assertTrue(self.reg.is_include_all_register('AA1'))

    def test_is_include_only_latin(self):
        self.assertFalse(self.reg.is_include_only_latin('фвафаф'))
        self.assertTrue(self.reg.is_include_only_latin('adfkle123'))
        self.assertFalse(self.reg.is_include_only_latin('adfkleСмит1'))

    def test_check_password_dictionary(self):
        self.assertTrue(self.reg.check_password_dictionary('211181POIUu'))
        self.assertFalse(self.reg.check_password_dictionary('qwertyuiop'))

    def test_is_include_digit(self):
        self.assertTrue(self.reg.is_include_digit('adasda11'))
        self.assertFalse(self.reg.is_include_digit('adaadsa'))


if __name__ == "main":
    unittest.main()
