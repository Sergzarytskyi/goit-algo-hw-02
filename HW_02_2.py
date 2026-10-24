import re
from collections import deque

def is_palindrome(text):

    cleaned_text = re.sub(r"[^\w]", "", text).replace("_", "").lower()
    char_deque = deque(cleaned_text)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            print(f"Текст: '{text}' - це не паліндром.")  
            return False  
  
    print(f"Текст: '{text}' - це паліндром.")  
     


is_palindrome("Python 345543")
is_palindrome("Козак з казок")
is_palindrome("123 456 7 654 321") 
