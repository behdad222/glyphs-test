glyphs = ['ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی', 'ء', 'آ', 'ة', 'ك', 'ي', 'ˇ', 'أ', 'ۊ', 'ؤ', 'ئ', 'ى', 'ټ', 'څ', 'ځ' ,'ډ' ,'ړ' ,'ږ' ,'ښ' ,'ګ' ,'ڼ' ,'ې' ,'ۍ' ,'ڕ' ,'ڵ' ,'ﭪ' ,'ێ' ,'ۍ‎' ,'ڤ']
text = ""

i = 0
while i < len(glyphs):
	text = text + "\n\n" + glyphs[i]

	j = 0
	while j < len(glyphs):
		text = text + "\n\n" + glyphs[j] + glyphs[i] + "\n"
		temp = ""
		temp = temp + glyphs[j] + glyphs[i]

		k = 0
		while k < len(glyphs):
			text = text + temp + glyphs[k] + " - "
			k = k + 1

		j = j + 1

	i = i + 1


print (text)