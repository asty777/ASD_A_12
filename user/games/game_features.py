from database.data_manager import load_data, save_data

FILE_GAMES = "database/games.txt"
FILE_RATINGS = "database/ratings.txt"


# =========================
# LOAD & SAVE TXT
# =========================
def load_games_txt():
    games = []
    try:
        with open(FILE_GAMES, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue  # skip baris kosong

                parts = [p.strip() for p in line.strip().split(",")]

                if len(parts) != 8:
                    print("Format salah:", parts)  # DEBUG
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
                    print("Data error:", parts)

    except FileNotFoundError:
        print("File games.txt tidak ditemukan!")

    return games

def save_games_txt(games):
    with open(FILE_GAMES, "w") as f:
        for g in games:
            line = f"{g['id']},{g['nama_game']},{g['genre']},{g['rating']},{g['total_rating']},{g['jumlah_rating']},{g['played']},{g['downloads']}\n"
            f.write(line)


# =========================
# LIHAT GAME
# =========================
def lihat_game():
    games = load_games_txt()

    if not games:
        print("Belum ada data game.")
        return

    while True:
        print("\n===== DAFTAR GAME =====")
        for i, g in enumerate(games, 1):
            print(f"{i}. {g['nama_game']} - {g['genre']} - ⭐ {g['rating']}")

        print("\n1. Filter Genre")
        print("2. Lihat Detail")
        print("3. Kembali")

        pilih = input("Pilih: ")

        if pilih == "1":
            filter_genre(games)
        elif pilih == "2":
            detail_game(games)
        elif pilih == "3":
            break
        else:
            print("Pilihan tidak valid!")


# =========================
# FILTER GENRE
# =========================
def filter_genre(games):
    genre_list = list(set([g["genre"] for g in games]))

    print("\n===== PILIH GENRE =====")
    for i, g in enumerate(genre_list, 1):
        print(f"{i}. {g}")

    try:
        pilih = int(input("Pilih: ")) - 1
        genre = genre_list[pilih]
    except:
        print("Input salah!")
        return

    print(f"\n=== GAME GENRE {genre} ===")
    for g in games:
        if g["genre"] == genre:
            print(f"- {g['nama_game']} ⭐ {g['rating']}")


# =========================
# DETAIL GAME
# =========================
def detail_game(games):
    try:
        idx = int(input("Nomor game: ")) - 1
        g = games[idx]
    except:
        print("Input salah!")
        return

    print("\n===== DETAIL GAME =====")
    print(f"Nama: {g['nama_game']}")
    print(f"Genre: {g['genre']}")
    print(f"Rating: ⭐ {g['rating']}")
    print(f"Played: {g['played']}")
    print(f"Downloads: {g['downloads']}")
    input("\nTekan Enter untuk kembali")


# =========================
# LEADERBOARD
# =========================
def leaderboard():
    games = load_games_txt()

    if not games:
        print("Belum ada data game.")
        return

    print("\n=== LEADERBOARD ===")
    print("1. Top Rating")
    print("2. Most Played")
    print("3. Most Downloaded")

    pilih = input("Pilih: ")

    if pilih == "1":
        sorted_games = sorted(games, key=lambda x: x["rating"], reverse=True)
    elif pilih == "2":
        sorted_games = sorted(games, key=lambda x: x["played"], reverse=True)
    elif pilih == "3":
        sorted_games = sorted(games, key=lambda x: x["downloads"], reverse=True)
    else:
        print("Pilihan tidak valid!")
        return

    medals = ["🥇", "🥈", "🥉"]

    for i, g in enumerate(sorted_games[:5], 1):
        icon = medals[i-1] if i <= 3 else f"{i}."
        print(f"{icon} {g['nama_game']} - ⭐ {g['rating']}")


# =========================
# SEARCH GAME
# =========================
def search_game():
    games = load_games_txt()

    keyword = input("Keyword: ").lower()
    hasil = [g for g in games if keyword in g["nama_game"].lower()]

    if not hasil:
        print("Game tidak ditemukan.")
        return

    print("\n=== HASIL PENCARIAN ===")
    for g in hasil:
        print(f"{g['nama_game']} - ⭐ {g['rating']}")


# =========================
# RATING GAME
# =========================
def rating_game(user):
    games = load_games_txt()
    ratings = load_data(FILE_RATINGS, [])

    keyword = input("Cari game: ").lower()
    hasil = [g for g in games if keyword in g["nama_game"].lower()]

    if not hasil:
        print("Game tidak ditemukan")
        return

    print("\n=== PILIH GAME ===")
    for i, g in enumerate(hasil, 1):
        print(f"{i}. {g['nama_game']}")

    try:
        pilih = int(input("Pilih: ")) - 1
        game = hasil[pilih]
    except:
        print("Input salah!")
        return

    try:
        nilai = int(input("Rating (1-5): "))
    except:
        print("Harus angka!")
        return

    if nilai < 1 or nilai > 5:
        print("Rating harus 1-5!")
        return

    ratings.append({
        "id": len(ratings) + 1,
        "user_id": user["id"],
        "game_id": game["id"],
        "rating": nilai
    })

    game["total_rating"] += nilai
    game["jumlah_rating"] += 1
    game["rating"] = round(game["total_rating"] / game["jumlah_rating"], 2)

    save_data(FILE_RATINGS, ratings)
    save_games_txt(games)

    print("✅ Rating berhasil!")