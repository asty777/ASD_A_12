from data_manager import load_data, save_data

FILE_GAMES = "games.json"
FILE_RATINGS = "ratings.json"

def lihat_game():
    games = load_data(FILE_GAMES, [])

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

def filter_genre(games):
    genre_list = list(set([g["genre"] for g in games]))

    print("\n===== PILIH GENRE =====")
    for i, g in enumerate(genre_list, 1):
        print(f"{i}. {g}")

    pilih = int(input("Pilih: ")) - 1
    genre = genre_list[pilih]

    print(f"\n=== GAME GENRE {genre} ===")
    for g in games:
        if g["genre"] == genre:
            print(f"- {g['nama_game']} ⭐ {g['rating']}")

def detail_game(games):
    idx = int(input("Masukkan nomor game: ")) - 1
    if 0 <= idx < len(games):
        g = games[idx]
        print("\n===== DETAIL GAME =====")
        print(f"Nama: {g['nama_game']}")
        print(f"Genre: {g['genre']}")
        print(f"Rating: ⭐ {g['rating']}")
        print(f"Played: {g['played']}")
        print(f"Downloads: {g['downloads']}")
        input("\nTekan Enter untuk kembali")

def leaderboard():
    games = load_data(FILE_GAMES, [])

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
        return

    for i, g in enumerate(sorted_games[:5], 1):
        print(f"{i}. {g['nama_game']}")

def search_game():
    games = load_data(FILE_GAMES, [])

    keyword = input("Masukkan keyword: ").lower()
    hasil = [g for g in games if keyword in g["nama_game"].lower()]

    print("\n=== HASIL PENCARIAN ===")
    for i, g in enumerate(hasil, 1):
        print(f"{i}. {g['nama_game']} ⭐ {g['rating']}")

def rating_game(user):
    games = load_data(FILE_GAMES, [])
    ratings = load_data(FILE_RATINGS, [])

    keyword = input("Cari game: ").lower()
    hasil = [g for g in games if keyword in g["nama_game"].lower()]

    if not hasil:
        print("Game tidak ditemukan")
        return

    for i, g in enumerate(hasil, 1):
        print(f"{i}. {g['nama_game']}")

    pilih = int(input("Pilih game: ")) - 1
    game = hasil[pilih]

    nilai = int(input("Masukkan rating (1-5): "))

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
    save_data(FILE_GAMES, games)

    print("Rating berhasil ditambahkan!")