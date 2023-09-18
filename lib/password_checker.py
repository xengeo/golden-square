# File: lib/file_checker.py

class PasswordChecker():
    """Class for checking password validity"""
    
    def check(self, password):
        if len(password) >=8:
            return True
        else:
            raise Exception("Invalid password, must be 8+ characters.")
        
        