def lengthOfLastWord(self,s:str)-> int:
    words = s.strip().split()
    if not words:
        return 0
    return len(words[-1])
print(lengthOfLastWord(0,"Hello World"))  # Output: 5