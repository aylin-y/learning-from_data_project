import lyricsgenius
import pandas as pd
import time
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Get the API key from environment variables
GENIUS_TOKEN = os.getenv("GENIUS_API_KEY")

# Check if the token is loaded correctly
if not GENIUS_TOKEN:
    raise ValueError("GENIUS_API_KEY not found. Please check your .env file.")

csv_file = "lyrics_dataset_raw.csv"


genius = lyricsgenius.Genius(GENIUS_TOKEN)
genius.timeout = 30
genius.retries = 5  # If there is an error, try 5 more times again
genius.sleep_time = 2
genius.remove_section_headers = True
genius.skip_non_songs = True


genres = {
    "Rock": ["Queen", "Pink Floyd", "The Beatles", "Led Zeppelin", "Nirvana", "AC/DC", "The Doors"],
    "Hip-Hop": ["Eminem", "Kendrick Lamar", "Jay-Z", "Drake", "Kanye West", "Tupac", "Snoop Dogg"],
    "Pop": ["Taylor Swift", "Ariana Grande", "Billie Eilish", "Justin Bieber", "Ed Sheeran", "Dua Lipa", "Rihanna"],
    "Metal": ["Metallica", "Iron Maiden", "Black Sabbath", "Slayer", "Megadeth", "Pantera", "System of a Down"]
}


def save_to_csv(data):
    df = pd.DataFrame(data)
    # If file exist, append on it (mode='a'), or create new file
    header = not os.path.exists(csv_file)
    df.to_csv(csv_file, mode='a', index=False, header=header, encoding='utf-8-sig')


dataset = []
print("Data scraping process is starting...")

for genre, artists in genres.items():
    print(f"\n--- Category: {genre} ---")
    for artist_name in artists:
        retry_count = 0
        while retry_count < 3:
            try:
                print(f" Searching: {artist_name}...")
                artist = genius.search_artist(artist_name, max_songs=40, sort="popularity")

                if artist:
                    temp_data = []
                    for song in artist.songs:
                        temp_data.append({
                            "artist": artist_name,
                            "genre": genre,
                            "title": song.title,
                            "text": song.lyrics
                        })

                    save_to_csv(temp_data)  # Save to file after each artist
                    print(f" {artist_name} is done. Added to file.")
                break

            except Exception as e:
                retry_count += 1
                print(f"️ Error for {artist_name} (Trying count {retry_count}): {e}")
                time.sleep(10)

print(f"\n Process is done! Data was saved to '{csv_file}'.")