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

target_csv = "lyrics_dataset_raw.csv"


genius = lyricsgenius.Genius(GENIUS_TOKEN, timeout=30, retries=3, sleep_time=1)
genius.remove_section_headers = True
genius.skip_non_songs = True


new_singers = {
    "Rock": ["The Smiths", "Arctic Monkeys"],
    "Hip-Hop": ["Post Malone"],
    "Pop": ["Harry Styles"],
    "Metal": ["Korn"]
}

print("Data scraping process is starting...")

for genre, artists in new_singers.items():
    print(f"\n--- Category: {genre} ---")
    for artist_name in artists:
        try:
            print(f" Searching: {artist_name}...")
            artist = genius.search_artist(artist_name, max_songs=45, sort="popularity")

            if artist:
                temp_data = []
                for song in artist.songs:
                    temp_data.append({
                        "artist": artist_name,
                        "genre": genre,
                        "title": song.title,
                        "text": song.lyrics
                    })


                df_new = pd.DataFrame(temp_data)
                df_new.to_csv(target_csv, mode='a', index=False, header=not os.path.exists(target_csv),
                              encoding='utf-8-sig')
                print(f" {artist_name} is done.")

            time.sleep(2)

        except Exception as e:
            print(f"️ {artist_name} is skipped (Error): {e}")

print(f"\n Process is done! Data was saved to '{target_csv}'.")