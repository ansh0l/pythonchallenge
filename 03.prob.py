with open("03.prob.hint", "r") as f:
    text = f.read()

text = ''.join(text.split("\n"))

is_big = lambda ch: ord("A") <= ord(ch) <= ord("Z")
is_small = lambda ch: ord("a") <= ord(ch) <= ord("z")
pattern = (is_small, ) + (is_big, ) * 3 + (is_small, ) + (is_big, ) * 3 + (is_small, )

matches = lambda pat, st: all(x(y) for x, y in zip(pat, st))
result = []
for i in range(len(text)):
    st = text[i:i+9]
    if len(st) == 9 and matches(pattern, st):
        print st[1:8]
        result.append(st[4])
print result
print ''.join(result)

#Hit url: http://www.pythonchallenge.com/pc/def/linkedlist.html
#Next, hit url: http://www.pythonchallenge.com/pc/def/linkedlist.php
