def reverse_array_str(self,s):
    left=0
    right=len(s)-1

    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    

    return s
# Example usage to test the reverse_array_str function:
input_str = ["H", "e", "l", "l", "o"]
solution = reverse_array_str(None, input_str)
print("Reversed string array:", solution) 