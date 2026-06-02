from database.utils import read_file, write_file


def load_games():
    games = []
    data = read_file("games.txt")

    for line in data:
        if not line.strip():
            continue

        parts = line.strip().split("|")

        if len(parts) != 8:
            continue

        try:
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
        except:
            continue

    return games

def save_games(games):
    data = []

    for g in games:
        line = f"{g['id']}|{g['nama_game']}|{g['genre']}|{g['rating']}|{g['total_rating']}|{g['jumlah_rating']}|{g['played']}|{g['downloads']}\n"
        data.append(line)

    write_file("games.txt", data)


# lihat game
def lihat():
    games = load_games()

    if not games:
        print("Belum ada game.")
        return

    print("\n===== GAME =====")
    for g in games:
        print(f"{g['id']}. {g['nama_game']} | {g['genre']} | ⭐ {g['rating']}")


# tambah game
def tambah():
    games = load_games()

    nama = input("Nama game: ").strip()
    genre = input("Genre: ").strip()

    if not nama or not genre:
        print("Input tidak boleh kosong!")
        return

    # ambil ID terbesar
    if games:
        new_id = max(g["id"] for g in games) + 1
    else:
        new_id = 1

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
    print("Game berhasil ditambahkan!")


# update game
def update():
    games = load_games()

    if not games:
        print("Belum ada game.")
        return

    for i, g in enumerate(games, 1):
        print(f"{i}. {g['nama_game']}")

    try:
        idx = int(input("Pilih nomor: ")) - 1

        if idx < 0 or idx >= len(games):
            print("Pilihan tidak valid!")
            return

        nama_baru = input("Nama baru: ").strip()

        if not nama_baru:
            print("Nama tidak boleh kosong!")
            return

        games[idx]["nama_game"] = nama_baru

        save_games(games)
        print("Game berhasil diupdate!")

    except ValueError:
        print("Input harus angka!")


# hapus game
def delete():
    games = load_games()

    if not games:
        print("Belum ada game.")
        return

    for i, g in enumerate(games, 1):
        print(f"{i}. {g['nama_game']}")

    try:
        idx = int(input("Pilih nomor: ")) - 1

        if idx < 0 or idx >= len(games):
            print("Pilihan tidak valid!")
            return

        konfirmasi = input("Yakin mau hapus? (y/n): ").lower()
        if konfirmasi != "y":
            print("Dibatalkan.")
            return

        games.pop(idx)
        save_games(games)

        print("Game berhasil dihapus!")

    except ValueError:
        print("input harus angka!")


#menu
def admin_menu():
    while True:
        print("\n===== MENU ADMIN =====")
        print("1. Tambah Game")
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
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid!")