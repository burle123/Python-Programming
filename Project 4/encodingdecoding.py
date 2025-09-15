#Encoding And Decoding of Strings

# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode
# import random

# string = input("Enter any String : ")
# words = string.split()
# choice = input("Enter 'c' to code or 'd' to decode : ")
# choice = True if choice == 'c' else False

# if (choice):  # Encoding
#     nwords = []
#     for word in words:
#         if len(word) >= 3:
#             symbols = ['@', '#', '$', '%', '^', '&', '*']
#             # pick 3 random chars for start and end
#             start = ''.join(random.choices(symbols, k=3))
#             end = ''.join(random.choices(symbols, k=3))
            
#             # encoding rule
#             new_word = start + word[1:] + word[0] + end
#             nwords.append(new_word)
#         else:
#             nwords.append(word[::-1])
#     print("Coded String : ", ' '.join(nwords))

# else:  # Decoding
#     nwords = []
#     for word in words:
#         if len(word) >= 3:
#             # remove 3 from start and 3 from end
#             new_word = word[3:-3]
#             # move last letter to front
#             new_word = new_word[-1] + new_word[:-1]
#             nwords.append(new_word)
#         else:
#             nwords.append(word[::-1])
#     print("Decoded String : ", ' '.join(nwords))

st = input("Enter message : ")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding : ")
coding = True if (coding=="1") else False
print(coding)
if(coding):
  nwords = []
  for word in words:
    if(len(word)>=5):
      r1 = "ds@f"
      r2 = "j%kr"
      stnew = r1+ word[1:] + word[0] + r2
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print("Coded String : ", ' '.join(nwords))

else:
  nwords = []
  for word in words:
    if(len(word)>=5): 
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print("Decoded String : ", ' '.join(nwords))
