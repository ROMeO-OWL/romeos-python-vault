# use py 3.10 or later
def get_typed_input(data_type, prompt='', error_msg="invalid input"):
    for _ in range(3):
        try:
            val = input(prompt)
            if data_type == str:
                if val.strip(): return val
                print("the text cannot be empty") ; continue
            return data_type(val)
        except ValueError: print(error_msg)
    return None

def main():
    s_id = 1_000 ; songs = {} ; opt = 0
    while opt != 8:
        opt = get_typed_input(int, "n1)add a song\n2)show all song titles\n3)search song (by title or artist)\n4)filter songs by artist\n5)play a song by Id\n6)delete a song by ID\n7)view library stats\n8)exit\n--> ")
        if opt is None: print("invalid data or no more attempts") ; return
        match opt:
            case 1:
                artist = get_typed_input(str, "Enter artist:\n--> ")
                artist = artist.title() if artist else "unknown"
                title = get_typed_input(str, "Enter title:\n--> ")
                title = title.title() if title else "untitled"
                genre = get_typed_input(str, "Enter genre:\n--> ")
                genre = genre.title() if genre else "general"
                duration = get_typed_input(int, "Enter duration (seconds):\n--> ")
                val_dur = duration if (duration and duration > 0) else 0
                size = get_typed_input(float, "Enter size (KB):\n--> ")
                val_size = size if (size and size > 0) else 0.0
                songs[s_id] = [artist, title, genre, val_dur, val_size]
                print(f"Song added successfully with id: {s_id}")
                s_id += 1
            case 2:
                if songs:
                    for id_num, song in songs.items(): print(f"Id: {id_num} title: {song[1]} artist: {song[0]} genre: {song[2]}")
                else: print("no songs registered")
            case 3:
                query = get_typed_input(str, "Enter search query:\n--> ")
                if not query: continue
                query = query.lower()
                results = [f"Id: {id_num} artist: {song[0]} title: {song[1]} genre: {song[2]} duration: {song[3]}s size: {song[4]}KB" 
                           for id_num, song in songs.items() if query in song[0].lower() or query in song[1].lower()]
                if results:
                    for res in results: print(res)
                else: print("no songs found")
            case 4:
                query_artist = get_typed_input(str, "Enter artist name:\n--> ")
                if not query_artist: continue
                filtered = [f"Id: {id_num} title: {song[1]} genre: {song[2]}" for id_num, song in songs.items() if query_artist.lower() in song[0].lower()]
                if filtered:
                    for song in filtered: print(song)
                else: print("no songs found for this artist")
            case 5:
                play_id = get_typed_input(int, "Enter song ID to play:\n--> ")
                if play_id in songs: print(f"Playing '{songs[play_id][1]}' by {songs[play_id][0]}")
                else: print("song id not found")
            case 6:
                del_id = get_typed_input(int, "Enter song ID to delete:\n--> ")
                if del_id in songs:
                    removed = songs.pop(del_id)
                    print(f"Song '{removed[1]}' deleted successfully")
                else: print("song ID not found")
            case 7:
                if songs:
                    total_dur =sum(s[3] for s in songs.values());  total_size = sum(s[4] for s in songs.values()) / 1024
                    print(f"Total songs: {len(songs)}\nTotal duration: {total_dur //60}m {total_dur % 60}s\nTotal size: {total_size:.2f} mb")
                else: print("library is empty")
            case 8: print("exiting") ; break
            case _: print("invalid option")

if __name__ == '__main__': main()