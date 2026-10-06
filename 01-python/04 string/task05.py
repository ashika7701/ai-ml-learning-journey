"""Task 4 — Palindrome ⭐

Check whether a word is a palindrome.

Example:

Enter word: madam
Palindrome

Another:

Enter word: python
Not a palindrome

Hint: Use slicing.

word[::-1]"""
print("to check whether a word is a palidrome")
text=input("enter word")
text=text.lower()
text=text.strip()
text1=text[::-1]
if text == text1:
  print("Palindrome")
else:
  print('not palindrome')
