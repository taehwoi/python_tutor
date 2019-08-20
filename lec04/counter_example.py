# load the "collections" module
import collections

words = ['red', 'blue', 'red', 'green', 'blue', 'blue']
# use the Counter class in "collections" module
cnt = collections.Counter(words)

print(cnt['green'])
print(cnt['chicken'])
print(cnt.most_common(2))
