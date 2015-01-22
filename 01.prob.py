import string
chars = string.ascii_lowercase
cipher = {y: x for x, y in zip(chars, chars[2:]+chars[:2])}

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

hint = ''.join(x if x not in cipher else cipher[x] for x in s)
print hint

#"i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url."

string.translate("map", string.maketrans(s, hint))
#'ocr'

#Hit url: www.pythonchallenge.com/pc/def/ocr.html
