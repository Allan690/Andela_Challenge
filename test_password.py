import unittest
import re
from PasswordChecker import PasswordValidator

class PasswordTester(unittest.TestCase):
  passwords = input("Enter your string of passwords: ").split(',')
  special_str = "$#@"

  def test_password_is_null_or_empty(self):
   
     for password in PasswordTester.passwords:
       if(len(password)==0 or not password):
           self.assertEqual(False, password)
           return 'Password cannot be empty or null'

  def test_password_missing_one_number(self):
      
       for password in PasswordTester.passwords:
           if any (char.isdigit() for char in password) ==False:
               self.assertEqual(False, password)
               return 'Password must contain at least one digit'

  def test_password_has_a_lowercase_letter(self):
      for password in PasswordTester.passwords:
          if not any (char.islower() for char in password):
                  self.assertEqual(False, password)
                  return 'Password must contain at least one lowercase letter'

  def test_password_has_an_uppercase_letter(self):
      for password in PasswordTester.passwords:
          if not any (char.isupper() for char in password):
              self.assertEqual(False, password)
              return 'Password must contain at least one uppercase letter'

  def test_password_has_special_chars(self):
      regex = re.compile('[$#@]')
      for password in PasswordTester.passwords:
          if(regex.search(password)==None):
              self.assertEqual(False, password)
              return 'Password must contain special characters'            
                
  def test_password_has_length_btn_six_and_twelve(self):
      for password in PasswordTester.passwords:
          if(len(password)<6 or len(password)>12):
              self.assertEqual(False,password)
              return 'Password must have a length of between 6 and 12'

  def test_password_has_spaces(self):
       for password in PasswordTester.passwords:
           if any(char.isspace() for char in password):
               self.assertEqual(False, password)

if __name__ == '__main__':
    unittest.main()
  