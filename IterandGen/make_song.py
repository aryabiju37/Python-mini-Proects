def make_song(number=99,song_word="soda"):
	while number >= 2:
		yield "{num} bottles of {sng_wrd} on the wall".format(num = number,sng_wrd=song_word) 
		number = number - 1
	print("Only 1 bottle of {sng_wrd} on the wall left".format(sng_wrd=song_word))

# sng = make_song(5,"kombucha")
song = make_song()
print(next(song))
# print(next(sng))
# print(next(sng))
# print(next(sng))
# print(next(sng))
# print(next(sng))
# print(next(sng))
