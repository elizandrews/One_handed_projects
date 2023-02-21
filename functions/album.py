# Write a function make_album() building a dictionary describing a music album
# Should take artist name, album title & return dictionary with info
# Use function to make 3 dictionaries of 3 albums & print each return value

# Use None to add an optional parameter for adding number of songs in album
# If call line includes a value for number of songs, add to dictionary
# Make at least 1 new function call that includes number of songs

def make_album(artist, title, num_of_songs=None):
    """Return a dictionary of information about an album"""
    album = {'musician' : artist, 'album_title' : title}
    if num_of_songs:
        album['song_num'] = num_of_songs
    return album

record = make_album('nirvana', 'nevermind', 13)
print(record)

record = make_album('beatles', 'white album', 30)
print(record)

record = make_album(title='a night at the opera', artist='queen')
print(record)
