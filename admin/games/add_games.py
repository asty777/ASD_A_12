from database.utils import read_file, write_file
def add_game():
    print("===== TAMBAH GAME =====")

    nama_game = input("Nama game: ")
    genre = input("Genre: ")

    data = read_file("games.txt")

    new_id = len(data) + 1

    line = f"{new_id}|{nama_game}|{genre}|0|0|0|0|0\n"

    data.append(line)

    write_file("games.txt", data)

    print("Game berhasil ditambahkan!")