"""Start with your program from Exercise 8-7.
Write a while loop that allows users to enter an album's artist and title.
Once you have that information, call make_album() with the
user's input and print the dictionary that's created.
Be sure to include a quit value in the while loop."""


def make_album(artist_name, album_title):
    album = {"artist_name": artist_name, "album_title": album_title}
    return album


while True:
    print("\nPlease, tell me your favorite album or press 'q' to quit.")

    ar_name = input("Artist's name: ")
    if ar_name == "q":
        break

    al_title = input("Album's title: ")
    if al_title == "q":
        break

    dic_album = make_album(ar_name, al_title)
    print(f"Album: {dic_album}")
