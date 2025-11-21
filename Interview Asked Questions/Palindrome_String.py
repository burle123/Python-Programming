

def isPalindrome(self,s):
    """
    Check if the given string is a palindrome.

    A palindrome is a string that reads the same forwards and backwards.

    Parameters:
    s (str): The string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """

    # Example usage:
    new =""
    for char in s:
        if char.isalnum():  # Consider only alphanumeric characters
            new += char.lower()  # Convert to lowercase for uniformity
    return new == new[::-1]  # Check if the string is equal to its reverse



# Example usage to test the isPalindrome function:
test_strings = ["A man, a plan, a canal: Panama"]  # Expected: True   
  
for s in test_strings:
    result = isPalindrome(None, s)
    print(f'Is "{s}" a palindrome? {result}')


