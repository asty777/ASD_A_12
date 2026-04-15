from database.utils import read_file, write_file
from admin.games.read_games import show_games_admin
def update_game():
    data = read_file("games.txt")

    show_games_admin()
    target = input("ID game yang mau diupdate: ")

    new_data = []

    for g in data:
        id, nama, genre, rating, tr, jr, played, dl = g.strip().split("|")

        if id == target:
            print("Kosongkan jika tidak diubah")

            nama_baru = input(f"Nama ({nama}): ") or nama
            genre_baru = input(f"Genre ({genre}): ") or genre

            line = f"{id}|{nama_baru}|{genre_baru}|{rating}|{tr}|{jr}|{played}|{dl}\n"
            new_data.append(line)
        else:
            new_data.append(g)

    write_file("games.txt", new_data)

    print("Game berhasil diupdate")