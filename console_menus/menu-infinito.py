def password_validator(password:int) -> bool: return True if password == 2026 else False
    
def main():
    while True:
        try:
           password = int(input("Enter your password:\n--> "))
        except ValueError: print("Invalid value")
        else:
            if password_validator(password):print("Welcome back") ; break
            else: print("Password incorrect")            
            
if __name__=='__main__': main()