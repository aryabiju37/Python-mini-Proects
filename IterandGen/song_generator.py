# def make_song(verses = 99, song_word = "Soda"):
    

    
#     for i in range(verses,-1,-1):
                
#         if i > 1:
#             yield "{} bottles of {} on the wall".format(i,song_word)
#         elif i == 1:
#             yield "Only {} bottle of {} left!".format(i,song_word)
#         else:
#             yield "No more {}".format(song_word)

def make_song(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)

sng = make_song(3,"Kombucha")
print(next(sng))
print(next(sng))
print(next(sng))
print(next(sng))
print(next(sng))
# print(next(sng))
# print(next(sng))