from database.utils import read_file, write_file
from admin.games.read_games import show_games_admin
def delete_game():
    data = read_file("games.txt")

    show_games_admin()
    target = input("ID game yang mau dihapus: ")

    new_data = []

    for g in data:
        id = g.split("|")[0]

        if id != target:
            new_data.append(g)

    write_file("games.txt", new_data)

    print("Game berhasil dihapus")

