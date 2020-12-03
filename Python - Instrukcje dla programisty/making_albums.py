def make_album(performer, title):
    album_var = {f'{performer.title()}': f'{title.title()}'}
    return album_var


albums = {}


while True:
    print('\nWrite the artist and album name or input q to finish')
    artist = input('Artist: ')
    if artist == 'q':
        break
    else:
        name = input('Album: ')
        album = make_album(artist, name)
        albums.update(album)


print(albums)

# plyta = make_album('kazik', 'tata kazika')
# print(plyta)
# plyta2 = make_album('bayer full', 'majteczki w kropeczki')
# print(plyta2)
# plyta3 = make_album('kult', 'moj bol jest lepszy niez twoj', 111)
# print(plyta3)


# plyta.update(plyta2)
# plyta.update(plyta3)
# print('/n', plyta)
