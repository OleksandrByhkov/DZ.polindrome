def is_palindrome(text):
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome('A man, a plan, a canal: Panama'))
print(is_palindrome('race a car'))
print(is_palindrome('OP'))
print(is_palindrome('a.'))