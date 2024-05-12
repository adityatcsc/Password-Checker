import random

password = input("Enter the password:- ")

lower = "abcdefghijklmnopqrstuvwxyz"
upper  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol = "!#$%&*+-/;=?@^.'}{][|_()~`"
number = "0123456789"

missing_criteria = []

# here the strength of the password is checked 
def check_strength(passw):

    has_lowercase = sum(1 for char in passw if char in lower) >= 2
    has_uppercase = sum(1 for char in passw if char in upper) >= 2
    has_special_symbol = sum(1 for char in passw if char in symbol) >= 2
    has_number = sum(1 for char in passw if char in number) >= 2
    
    if len(passw) <= 8:
        missing_criteria.append("at least 8 characters")
    if not has_uppercase:
        missing_criteria.append("at least 2 uppercase letters")
    if not has_lowercase:
        missing_criteria.append("at least 2 lowercase letters")
    if not has_special_symbol:
        missing_criteria.append("at least 2 special symbols")
    if not has_number:
        missing_criteria.append("at least 2 numbers")



# ther given password is modifed here 
def pass_modify(passwd):        
    if choice.lower() == "yes" or choice.lower()=='y':
        num_characters_needed = random.randint(8, 10) - len(passwd)
        generated_password = passwd

        target_length=len(generated_password)+num_characters_needed

        # Incorporate user information into the password
        name = input("Enter your full name: ").strip()
        age = input("Enter the age: ").strip()
        dob = input("Enter the Date of Birth (DOB) (dd/mm/yyyy): ").replace("/", '').strip()
        location = input("Enter the location: ").strip()

        user_info = (name or '') + (age or '') + (dob or '') + (location or '')
        print("user info :- ",user_info)

        while len(generated_password)<=target_length:

                if 'at least 2 uppercase letters' in missing_criteria :
                    if location !='' or name !='':
                        generated_password += ''.join(random.choice((location or '')+(name or '')) for _ in range(2)).upper()
                    else:
                         generated_password += ''.join(random.choice(upper) for _ in range(2))

                if 'at least 2 lowercase letters' in missing_criteria and (location !='' or name !='') :
                    if location !='' or name !='':
                        generated_password += ''.join(random.choice((location or '')+(name or '')) for _ in range(2)).lower()
                    else:
                         generated_password += ''.join(random.choice(lower) for _ in range(2))
                    
                if 'at least 2 special symbols' in missing_criteria:
                    generated_password += ''.join(random.choice(symbol) for _ in range(2))
                    
                if 'at least 2 numbers' in missing_criteria and (age !='' or dob !=''):
                    if age !='' or dob !='':
                        generated_password += ''.join(random.choice((age or '')+(dob or '')) for _ in range(2)).lower()
                    else:
                         generated_password += ''.join(random.choice(number) for _ in range(2))  
            

        print("Generated Password:", generated_password)  


if __name__=="__main__":
    check_strength(password)

    if len(missing_criteria) == 0:
        print("Very Good Password 👌")
    else:
        print("Password is not strong enough. Missing criteria:\n " + '\n '.join(missing_criteria))
        choice = input("Do you want to fill the missing criteria randomly? (yes/no): ")    
        pass_modify(password)

