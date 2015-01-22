with open("03.prob.hint", "r") as f:
    text = f.read()

text = ''.join(text.split("\n"))

is_big = lambda ch: ord("A") <= ord(ch) <= ord("Z")
is_small = lambda ch: ord("a") <= ord(ch) <= ord("z")
pattern = (is_small, ) + (is_big, ) * 3 + (is_small, ) + (is_big, ) * 3 + (is_small, )

matches = lambda pat, st: all(x(y) for x, y in zip(pat, st))
for i in range(len(text)):
    st = text[i:i+9]
    if matches(pattern, st):
        print st[1:8]
