# from unittest import TestCase

def handle_user_input():
  passwords = input("Enter your string of passwords: ").split(',')
  return passwords

def validate_password(passwords):
  special_str = "$#@"
  accepted = []
  for password in passwords:
    lower, upper, digits, special = 0, 0, 0, 0
    for char in password:
            if char.isdigit():
                digits += 1
            elif char.islower():
                lower += 1
            elif char.isupper():
                upper += 1
            elif special_str.find(char) != -1:
                special += 1
    if lower and upper and digits and special and len(password) in range(6,13):
      accepted.append(password)

  return accepted

def main():
  passwords= handle_user_input()
  accepted = validate_password(passwords)
  print (",".join(accepted))


# class PasswordTester(unittest.TestCase):
#   def test_valid_passwords(self):
    #self.assertEqual(validate_password(["I@n123", "T@st"]), "I@n123, T@st"")
    # pass

  
if __name__=='__main__':
    # unittest.main()
    main()
