from collections import Counter
code_hint = "contents of code hint in page source"
count = Counter(code_hint)
words_needed = ''.join(x for x in count if count[x] < 10)
filter(lambda x: x in words_needed, code_hint)
#"equality"

#Hit url: http://www.pythonchallenge.com/pc/def/equality.html
