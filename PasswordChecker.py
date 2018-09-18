def PasswordValidator():
   passwords = input("Enter your string of passwords: ").split(',')
   special_str = "$#@"
   accepted = []
   for password in passwords:
       lower = 0
       upper = 0
       digits = 0
       special = 0
       if(len(password)<6 or len(password)>12):
         return 'Password is invalid'
       for char in password:
            if char.isdigit():
                digits += 1
            elif char.islower():
                lower += 1
            elif char.isupper():
                upper += 1
            elif special_str.find(char) != -1:
                special += 1
       if lower >= 1 and upper >= 1 and digits >= 1 and special >= 1 and len(password) in range(6,13):
            accepted.append(password)
   print (",".join(accepted))

if __name__=='__main__':
    PasswordValidator()
            

