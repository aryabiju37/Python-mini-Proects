def single_letter_count(word,l):
	wrd = word.lower()
    if l in wrd:
        return wrd.count(l)
    else:
        return 0

print(single_letter_count("Hello World","h"))