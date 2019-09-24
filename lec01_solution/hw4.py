"""ANAGRAMS"""
a = input().replace(' ', '')
b = input().replace(' ', '')

print(sorted(a.upper())==sorted(b.upper()))
