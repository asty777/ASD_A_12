from database.utils import read_file, write_file
def show_games_admin():
    print("===== DATA GAME =====")

    data = read_file("games.txt")

    if not data:
        print("Kosong")
        return

    for g in data:
        id, nama, genre, rating, tr, jr, played, dl = g.strip().split("|")
        print(f"{id}. {nama} - {genre} - ⭐ {rating}")