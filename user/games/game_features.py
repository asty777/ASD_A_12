from database.utils import read_file, write_file

FILE_GAMES = "games.txt"
FILE_RATINGS = "ratings.txt"


def load_games():
    games = []
    data = read_file(FILE_GAMES)

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

    write_file(FILE_GAMES, data)



# def load_ratings():
#     ratings = []
#     data = read_file(FILE_RATINGS)

#     for line in data:
#         if not line.strip():
#             continue

#         id, user_id, game_id, rating = line.strip().split("|")

#         ratings.append({
#             "id": int(id),
#             "user_id": int(user_id),
#             "game_id": int(game_id),
#             "rating": int(rating)
#         })

#     return ratings

def load_ratings():
    ratings = []
    data = read_file(FILE_RATINGS)

    for line in data:
        if not line.strip():
            continue

        id, user_id, game_id, rating, comment = line.strip().split("|")

        ratings.append({
            "id": int(id),
            "user_id": int(user_id),
            "game_id": int(game_id),
            "rating": int(rating),
            "comment": comment
        })

    return ratings


def save_ratings(ratings):
    data = []

    for r in ratings:
        line = f"{r['id']}|{r['user_id']}|{r['game_id']}|{r['rating']}|{r['comment']}\n"
        data.append(line)

    write_file(FILE_RATINGS, data)



def lihat_game():
    games = load_games()

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

    input("\nTekan Enter untuk kembali...")



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

    ratings = load_ratings()

    print("\n===== REVIEW USER =====")

    ada_review = False

    for r in ratings:
        if r["game_id"] == g["id"] and r["comment"] != "-":
            ada_review = True
            print(f"⭐ {r['rating']} | {r['comment']}")

    if not ada_review:
        print("Belum ada review.")

    input("\nTekan Enter untuk kembali...")

def leaderboard():
    games = load_games()

    if not games:
        print("Belum ada data game.")
        return

    print("\n=== LEADERBOARD ===")
    print("1. Top Rating")
    # print("2. Most Played")
    # print("3. Most Downloaded")

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

    print("\n===== Leaderboard top rating =====")
    for i, g in enumerate(sorted_games[:5], 1):
        icon = medals[i-1] if i <= 3 else f"{i}."
        print(f"{icon} {g['nama_game']} - ⭐ {g['rating']}")



def search_game():
    games = load_games()

    keyword = input("Keyword: ").lower()
    hasil = [g for g in games if keyword in g["nama_game"].lower()]

    if not hasil:
        print("Game tidak ditemukan.")
        return

    print("\n=== HASIL PENCARIAN ===")
    for g in hasil:
        print(f"{g['nama_game']} - ⭐ {g['rating']}")



def rating_game(user):
    games = load_games()
    ratings = load_ratings()

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
    
    comment = input("Komentar: ").strip()
    if not comment:
        comment = "-"

    if nilai < 1 or nilai > 5:
        print("Rating harus 1-5!")
        return


    for r in ratings:
        if r["user_id"] == user["id"] and r["game_id"] == game["id"]:
            print("❌ Anda sudah pernah merating game ini!")
            return

    ratings.append({
    "id": len(ratings) + 1,
    "user_id": user["id"],
    "game_id": game["id"],
    "rating": nilai,
    "comment": comment
    })


    game["total_rating"] += nilai
    game["jumlah_rating"] += 1
    game["rating"] = round(game["total_rating"] / game["jumlah_rating"], 2)

    save_ratings(ratings)
    save_games(games)

    print("✅ Rating berhasil!")