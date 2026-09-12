class Song:
    def __init__(self, song_id, song_title, artist, duration):
        self.song_id = song_id
        self.song_title = song_title
        self.artist = artist
        self.duration = duration

    def display(self):
        print(f"Song ID: {self.song_id}")
        print(f"Song Title: {self.song_title}")
        print(f"Artist: {self.artist}")
        print(f"Duration: {self.duration}")


class Node:
    def __init__(self, song):
        self.song = song
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.count

    def insert_first(self, song):
        new_node = Node(song)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def insert_last(self, song):
        new_node = Node(song)

        if self.head is None:
            self.head = new_node
            self.count += 1
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
        self.count += 1

    def insert_at(self, song, position):
        if position < 1 or position > self.count + 1:
            return False

        if position == 1:
            self.insert_first(song)
            return True

        new_node = Node(song)
        current = self.head

        for _ in range(position - 2):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.count += 1

        return True

    def search(self, song_id):
        current = self.head

        while current is not None:
            if current.song.song_id.lower() == song_id.lower():
                return current.song

            current = current.next

        return None

    def delete(self, song_id):
        if self.head is None:
            return False

        if self.head.song.song_id.lower() == song_id.lower():
            self.head = self.head.next
            self.count -= 1
            return True

        current = self.head

        while current.next is not None:
            if current.next.song.song_id.lower() == song_id.lower():
                current.next = current.next.next
                self.count -= 1
                return True

            current = current.next

        return False

    def display(self):
        if self.head is None:
            print("Playlist is empty.")
            return

        print("\n========== PLAYLIST ==========")

        current = self.head
        song_number = 1

        while current is not None:
            print(f"\nSong {song_number}")
            current.song.display()

            current = current.next
            song_number += 1

        print(f"\nTotal number of songs: {self.count}")


def read_non_empty_string(message):
    while True:
        value = input(message).strip()

        if value != "":
            return value

        print("Input cannot be empty.")


def read_integer(message):
    while True:
        try:
            return int(input(message).strip())
        except ValueError:
            print("Please enter a valid number.")


def display_menu():
    print("================================")
    print("      MUSIC PLAYLIST MANAGER")
    print("================================")
    print("1. Add Song at Beginning")
    print("2. Add Song at End")
    print("3. Insert Song at Position")
    print("4. Display Playlist")
    print("5. Search Song")
    print("6. Remove Song")
    print("7. Display Playlist Size")
    print("8. Exit")


def create_song(playlist):
    song_id = read_non_empty_string("Enter Song ID: ")

    if playlist.search(song_id) is not None:
        print("Song ID already exists.")
        return None

    song_title = read_non_empty_string("Enter Song Title: ")
    artist = read_non_empty_string("Enter Artist: ")
    duration = read_non_empty_string("Enter Duration: ")

    return Song(song_id, song_title, artist, duration)


def add_song_at_beginning(playlist):
    print("\n========== ADD SONG AT BEGINNING ==========")

    song = create_song(playlist)

    if song is not None:
        playlist.insert_first(song)
        print("Song added at the beginning successfully.")


def add_song_at_end(playlist):
    print("\n========== ADD SONG AT END ==========")

    song = create_song(playlist)

    if song is not None:
        playlist.insert_last(song)
        print("Song added at the end successfully.")


def insert_song_at_position(playlist):
    print("\n========== INSERT SONG AT POSITION ==========")
    print(f"Enter a position from 1 to {playlist.size() + 1}.")
    print("Position 1 means the beginning of the playlist.")

    position = read_integer("Enter position: ")

    if position < 1 or position > playlist.size() + 1:
        print("Invalid position.")
        return

    song = create_song(playlist)

    if song is not None:
        playlist.insert_at(song, position)
        print("Song inserted successfully.")


def search_song(playlist):
    print("\n========== SEARCH SONG ==========")

    song_id = read_non_empty_string("Enter Song ID to search: ")
    song = playlist.search(song_id)

    if song is None:
        print("Song not found.")
    else:
        print("\nSong found:")
        song.display()


def remove_song(playlist):
    print("\n========== REMOVE SONG ==========")

    song_id = read_non_empty_string("Enter Song ID to remove: ")

    if playlist.delete(song_id):
        print("Song removed successfully.")
    else:
        print("Song not found.")


def display_playlist_size(playlist):
    print("\n========== PLAYLIST SIZE ==========")
    print(f"Total number of songs: {playlist.size()}")


def main():
    playlist = SinglyLinkedList()

    while True:
        display_menu()
        choice = read_integer("Enter your choice: ")

        if choice == 1:
            add_song_at_beginning(playlist)

        elif choice == 2:
            add_song_at_end(playlist)

        elif choice == 3:
            insert_song_at_position(playlist)

        elif choice == 4:
            playlist.display()

        elif choice == 5:
            search_song(playlist)

        elif choice == 6:
            remove_song(playlist)

        elif choice == 7:
            display_playlist_size(playlist)

        elif choice == 8:
            print("Exiting Music Playlist Manager...")
            break

        else:
            print("Invalid choice. Please select from 1 to 8.")

        print()


if __name__ == "__main__":
    main()