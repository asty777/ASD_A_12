from database.utils import read_file, write_file

# =========================
# LOAD & SAVE GAMES
# =========================
def load_games():
    games = []
    data = read_file("games.txt")

    for line in data:
        if not line.strip():
            continue

        parts = line.strip().split("|")

        if len(parts) != 8:
            continue

        id, nama, genre, rating, total, jumlah, played, downloads = parts

        games.append({
            "id": int(id),
            "nama_game": nama,
            "genre": genre,
            "rating": float(rating),
            "total_rating": int(total),
            "jumlah_rating": int(jumlah),
            "played": int(played),
            "downloads": int(downloads)
        })

    return games


def save_games(games):
    data = []

    for g in games:
        line = f"{g['id']}|{g['nama_game']}|{g['genre']}|{g['rating']}|{g['total_rating']}|{g['jumlah_rating']}|{g['played']}|{g['downloads']}\n"
        data.append(line)

    write_file("games.txt", data)


#menu 
def admin_menu():
    while True:
        print("\n1. Tambah Game")
        print("2. Update Game")
        print("3. Delete Game")
        print("4. Lihat Game")
        print("5. Exit")

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
        else:
            print("Pilihan tidak valid!")


#tambah game
def tambah():
    games = load_games()

    nama = input("Nama: ")
    genre = input("Genre: ")

    new_id = len(games) + 1

    games.append({
        "id": new_id,
        "nama_game": nama,
        "genre": genre,
        "rating": 0,
        "total_rating": 0,
        "jumlah_rating": 0,
        "played": 0,
        "downloads": 0
    })

    save_games(games)
    print("✅ Game berhasil ditambahkan!")


# update game
def update():
    games = load_games()

    if not games:
        print("Belum ada game.")
        return

    for i, g in enumerate(games, 1):
        print(f"{i}. {g['nama_game']}")

    try:
        idx = int(input("Pilih: ")) - 1
        games[idx]["nama_game"] = input("Nama baru: ")
    except:
        print("Input salah!")
        return

    save_games(games)
    print("✅ Game berhasil diupdate!")


# hapus game
def delete():
    games = load_games()

    if not games:
        print("Belum ada game.")
        return

    for i, g in enumerate(games, 1):
        print(f"{i}. {g['nama_game']}")

    try:
        idx = int(input("Pilih: ")) - 1
        games.pop(idx)
    except:
        print("Input salah!")
        return

    save_games(games)
    print("✅ Game berhasil dihapus!")


# tampilkan game
def lihat():
    games = load_games()

    if not games:
        print("Belum ada game.")
        return

    print("\n===== DATA GAME =====")
    for g in games:
        print(g)