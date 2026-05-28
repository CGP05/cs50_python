from cs50_artwork import get_artworks
from cs50_artists import get_artists

def main():
    artist = input("Artwork: ")
    artists = artists.get_artworks(query=artworks, limit=3)
    for artwork in artworks:
        print(f"* {artist}")

main()
