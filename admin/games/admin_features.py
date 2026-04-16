from database.data_manager import load_data, save_data

FILE_GAMES = "database/games.json"

def admin_menu():
    while True:
        print("\n1. Tambah\n2. Update\n3. Delete\n4. Lihat\n5. Kembali")
        pilih = input("Pilih: ")

        if pilih == "1":
            tambah()
        elif pilih == "2":
            update()
        elif pilih == "3":
            delete()
        elif pilih == "4":
            lihat()
        elif pilih == "5":
            break


def tambah():
    games = load_data(FILE_GAMES, [])
    nama = input("Nama: ")
    genre = input("Genre: ")

    games.append({
        "id": len(games) + 1,
        "nama_game": nama,
        "genre": genre,
        "rating": 0,
        "total_rating": 0,
        "jumlah_rating": 0,
        "played": 0,
        "downloads": 0
    })

    save_data(FILE_GAMES, games)


def update():
    games = load_data(FILE_GAMES, [])

    for i, g in enumerate(games, 1):
        print(f"{i}. {g['nama_game']}")

    idx = int(input("Pilih: ")) - 1
    games[idx]["nama_game"] = input("Nama baru: ")
    save_data(FILE_GAMES, games)


def delete():
    games = load_data(FILE_GAMES, [])

    for i, g in enumerate(games, 1):
        print(f"{i}. {g['nama_game']}")

    idx = int(input("Pilih: ")) - 1
    games.pop(idx)
    save_data(FILE_GAMES, games)


def lihat():
    games = load_data(FILE_GAMES, [])
    print(games)