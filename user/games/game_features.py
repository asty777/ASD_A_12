from database.utils import read_file, write_file
from my_clear import cls  # import cls untuk bersihkan layar

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

FILE_GAMES = "games.txt"
FILE_RATINGS = "ratings.txt"

# Fungsi helper untuk UI
def print_header(text, icon="✨"):
    """Menampilkan header section dengan icon"""
    print(f"\n{Colors.BLUE}{icon} {Colors.BOLD}{text}{Colors.RESET}")
    print(f"{Colors.CYAN}{'─'*50}{Colors.RESET}")

def print_success(text):
    """Menampilkan pesan sukses"""
    print(f"{Colors.GREEN}✅ {text}{Colors.RESET}")

def print_error(text):
    """Menampilkan pesan error"""
    print(f"{Colors.RED}❌ {text}{Colors.RESET}")

def print_warning(text):
    """Menampilkan pesan warning"""
    print(f"{Colors.YELLOW}⚠️ {text}{Colors.RESET}")

def print_info(text):
    """Menampilkan pesan info"""
    print(f"{Colors.CYAN}ℹ️ {text}{Colors.RESET}")

def print_game_card(game, show_detail=False):
    """Menampilkan game dalam format kartu"""
    medal = ""
    if game['rating'] >= 4.5:
        medal = "🏆"
    elif game['rating'] >= 4.0:
        medal = "⭐"
    elif game['rating'] >= 3.0:
        medal = "👍"
    elif game['rating'] > 0:
        medal = "📈"
    else:
        medal = "🆕"
    
    rating_star = "⭐" * int(game['rating']) if game['rating'] > 0 else "⏳"
    
    print(f"\n{Colors.CYAN}┌{'─'*48}┐{Colors.RESET}")
    print(f"{Colors.CYAN}│{Colors.RESET} {Colors.BOLD}{medal} {game['nama_game']}{Colors.RESET}{' ' * (40 - len(game['nama_game']))}{Colors.CYAN}│{Colors.RESET}")
    print(f"{Colors.CYAN}├{'─'*48}┤{Colors.RESET}")
    print(f"{Colors.CYAN}│{Colors.RESET} Genre: {game['genre']}{' ' * (38 - len(game['genre']))}{Colors.CYAN}│{Colors.RESET}")
    print(f"{Colors.CYAN}│{Colors.RESET} Rating: {rating_star} {game['rating']}{' ' * (30 - len(str(game['rating'])) - len(rating_star))}{Colors.CYAN}│{Colors.RESET}")
    
    if show_detail:
        print(f"{Colors.CYAN}│{Colors.RESET} Played: {game['played']:,} kali{' ' * (28 - len(str(game['played'])))} {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET} Downloads: {game['downloads']:,}{' ' * (26 - len(str(game['downloads'])))} {Colors.CYAN}│{Colors.RESET}")
    
    print(f"{Colors.CYAN}└{'─'*48}┘{Colors.RESET}")

def pause():
    """Jeda sampai user tekan Enter"""
    input(f"\n{Colors.CYAN}Tekan Enter untuk melanjutkan...{Colors.RESET}")

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

<<<<<<< HEAD
# =========================
# LOAD & SAVE RATINGS
# =========================
=======


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

>>>>>>> 60b0ea8ee8d5b11fecfe4ed71325d583a9d0e8a0
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

<<<<<<< HEAD
# =========================
# LIHAT GAME
# =========================
=======


>>>>>>> 60b0ea8ee8d5b11fecfe4ed71325d583a9d0e8a0
def lihat_game():
    cls()
    games = load_games()

    if not games:
        print_warning("Belum ada data game.")
        pause()
        return

    while True:
        cls()
        print_header("DAFTAR GAME")
        
        # Tampilan grid game yang rapi
        print(f"\n{Colors.BOLD}{Colors.CYAN}No  | Nama Game{' ' * 25} | Genre{' ' * 12} | Rating{Colors.RESET}")
        print(f"{Colors.YELLOW}{'─'*65}{Colors.RESET}")
        
        for i, g in enumerate(games, 1):
            rating_display = f"{'★' * int(g['rating'])} {g['rating']}" if g['rating'] > 0 else "Belum ada"
            print(f"{Colors.GREEN}{i:3}{Colors.RESET} | {g['nama_game']:<30} | {g['genre']:<15} | {rating_display}")
        
        print(f"\n{Colors.YELLOW}{'─'*65}{Colors.RESET}")
        print("\n Menu:")
        print(f"  {Colors.GREEN}1.{Colors.RESET} Filter Genre")
        print(f"  {Colors.GREEN}2.{Colors.RESET} Lihat Detail")
        print(f"  {Colors.GREEN}3.{Colors.RESET} Kembali")

        pilih = input(f"\n{Colors.BOLD}{Colors.YELLOW} Pilih: {Colors.RESET}").strip()

        if pilih == "1":
            filter_genre(games)
        elif pilih == "2":
            detail_game(games)
        elif pilih == "3":
            break
        else:
            print_error("Pilihan tidak valid!")
            pause()


def filter_genre(games):
    cls()
    genre_list = sorted(list(set([g["genre"] for g in games])))

    print_header("FILTER BERDASARKAN GENRE")
    
    print(f"\n{Colors.BOLD}Genre Tersedia:{Colors.RESET}")
    for i, g in enumerate(genre_list, 1):
        print(f"  {Colors.GREEN}{i}.{Colors.RESET} {g}")

    try:
        pilih = int(input(f"\n{Colors.YELLOW}Pilih genre: {Colors.RESET}")) - 1
        if pilih < 0 or pilih >= len(genre_list):
            print_error("Pilihan tidak valid!")
            pause()
            return
        genre = genre_list[pilih]
    except:
        print_error("Input salah!")
        pause()
        return

    cls()
    print_header(f"GAME GENRE {genre.upper()}")
    
    hasil = [g for g in games if g["genre"] == genre]
    
    if not hasil:
        print_warning(f"Tidak ada game dengan genre {genre}")
    else:
        for g in hasil:
            print_game_card(g, show_detail=False)
    
    pause()


def detail_game(games):
    cls()
    print_header("DETAIL GAME")
    
    try:
        idx = int(input(f"{Colors.YELLOW}Nomor game: {Colors.RESET}")) - 1
        
        if idx < 0 or idx >= len(games):
            print_error("Nomor game tidak valid!")
            pause()
            return
            
        g = games[idx]
    except:
        print_error("Input salah!")
        pause()
        return

<<<<<<< HEAD
    cls()
    print_header(f"DETAIL {g['nama_game'].upper()}", "📖")
    print_game_card(g, show_detail=True)
    pause()

# =========================
# LEADERBOARD
# =========================
=======
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

>>>>>>> 60b0ea8ee8d5b11fecfe4ed71325d583a9d0e8a0
def leaderboard():
    cls()
    games = load_games()

    if not games:
        print_warning("Belum ada data game.")
        pause()
        return

<<<<<<< HEAD
    print_header("LEADERBOARD")
    
    print(f"\n{Colors.BOLD}Pilih Kategori:{Colors.RESET}")
    print(f"  {Colors.GREEN}1.{Colors.RESET} Top Rating")
    print(f"  {Colors.GREEN}2.{Colors.RESET} Most Played")
    print(f"  {Colors.GREEN}3.{Colors.RESET} Most Downloaded")
=======
    print("\n=== LEADERBOARD ===")
    print("1. Top Rating")
    # print("2. Most Played")
    # print("3. Most Downloaded")
>>>>>>> 60b0ea8ee8d5b11fecfe4ed71325d583a9d0e8a0

    pilih = input(f"\n{Colors.BOLD}{Colors.YELLOW} Pilih: {Colors.RESET}").strip()

    if pilih == "1":
        sorted_games = sorted(games, key=lambda x: x["rating"], reverse=True)
        title = "TOP RATING"
        icon = "🏆"
    elif pilih == "2":
        sorted_games = sorted(games, key=lambda x: x["played"], reverse=True)
        title = "MOST PLAYED"
        icon = "🎮"
    elif pilih == "3":
        sorted_games = sorted(games, key=lambda x: x["downloads"], reverse=True)
        title = "MOST DOWNLOADED"
        icon = "📥"
    else:
        print_error("Pilihan tidak valid!")
        pause()
        return

    cls()
    print_header(f"{title} LEADERBOARD", icon)
    
    medals = ["🥇", "🥈", "🥉"]
<<<<<<< HEAD
    
    print(f"\n{Colors.BOLD}{'#'*55}{Colors.RESET}")
    
    for i, g in enumerate(sorted_games[:10], 1):  # Tampilkan top 10
        if i <= 3:
            rank = f"{medals[i-1]}"
        else:
            rank = f"{i:2}."
        
        # Baris leaderboard yang rapi
        rating_star = "★" * int(g['rating']) if g['rating'] > 0 else "⏳"
        
        if pilih == "1":
            value_display = f"{rating_star} {g['rating']}"
        elif pilih == "2":
            value_display = f" {g['played']:,} kali"
        else:
            value_display = f" {g['downloads']:,}"
        
        print(f"{Colors.YELLOW}{rank}{Colors.RESET} {Colors.CYAN}{g['nama_game']:<30}{Colors.RESET} {value_display}")
    
    print(f"{Colors.BOLD}{'#'*55}{Colors.RESET}")
    pause()
=======

    print("\n===== Leaderboard top rating =====")
    for i, g in enumerate(sorted_games[:5], 1):
        icon = medals[i-1] if i <= 3 else f"{i}."
        print(f"{icon} {g['nama_game']} - ⭐ {g['rating']}")

>>>>>>> 60b0ea8ee8d5b11fecfe4ed71325d583a9d0e8a0


def search_game():
    cls()
    games = load_games()
    
    print_header("PENCARIAN GAME")
    
    keyword = input(f"{Colors.CYAN} Masukkan keyword: {Colors.RESET}").lower()
    
    if not keyword:
        print_warning("Keyword tidak boleh kosong!")
        pause()
        return
    
    hasil = [g for g in games if keyword in g["nama_game"].lower()]

    if not hasil:
        print_warning(f"Game dengan keyword '{keyword}' tidak ditemukan.")
        pause()
        return

    cls()
    print_header(f"HASIL PENCARIAN: '{keyword}'")
    print_info(f"Ditemukan {len(hasil)} game")
    
    for g in hasil:
        print_game_card(g, show_detail=False)
    
    pause()


def rating_game(user):
    cls()
    games = load_games()
    ratings = load_ratings()

    print_header("BERI RATING GAME", "★")
    
    keyword = input(f"{Colors.CYAN}🔎 Cari game: {Colors.RESET}").lower()
    
    if not keyword:
        print_warning("Keyword tidak boleh kosong!")
        pause()
        return
    
    hasil = [g for g in games if keyword in g["nama_game"].lower()]

    if not hasil:
        print_warning(f"Game dengan keyword '{keyword}' tidak ditemukan")
        pause()
        return

    cls()
    print_header("PILIH GAME")
    
    for i, g in enumerate(hasil, 1):
        print(f"  {Colors.GREEN}{i}.{Colors.RESET} {g['nama_game']} - {g['genre']} (★ {g['rating']})")

    try:
        pilih = int(input(f"\n{Colors.YELLOW}Pilih game: {Colors.RESET}")) - 1
        
        if pilih < 0 or pilih >= len(hasil):
            print_error("Pilihan tidak valid!")
            pause()
            return
            
        game = hasil[pilih]
    except:
        print_error("Input harus angka!")
        pause()
        return

    cls()
    print_header(f"BERI RATING - {game['nama_game']}", "★")
    
    # Tampilkan rating yang tersedia dengan visual
    print(f"\n{Colors.BOLD}Pilih Rating:{Colors.RESET}")
    for i in range(1, 6):
        stars = "★" * i
        print(f"  {Colors.GREEN}{i}.{Colors.RESET} {stars} - {i} bintang")
    
    try:
        nilai = int(input(f"\n{Colors.YELLOW}Rating (1-5): {Colors.RESET}"))
    except:
        print_error("Harus angka!")
        pause()
        return
    
    comment = input("Komentar: ").strip()
    if not comment:
        comment = "-"

    if nilai < 1 or nilai > 5:
        print_error("Rating harus 1-5!")
        pause()
        return


    for r in ratings:
        if r["user_id"] == user["id"] and r["game_id"] == game["id"]:
            print_error("Anda sudah pernah merating game ini!")
            pause()
            return

    # Tambah rating
    new_id = max([r["id"] for r in ratings]) + 1 if ratings else 1
    
    ratings.append({
<<<<<<< HEAD
        "id": new_id,
        "user_id": user["id"],
        "game_id": game["id"],
        "rating": nilai
=======
    "id": len(ratings) + 1,
    "user_id": user["id"],
    "game_id": game["id"],
    "rating": nilai,
    "comment": comment
>>>>>>> 60b0ea8ee8d5b11fecfe4ed71325d583a9d0e8a0
    })


    game["total_rating"] += nilai
    game["jumlah_rating"] += 1
    game["rating"] = round(game["total_rating"] / game["jumlah_rating"], 2)

    save_ratings(ratings)
    save_games(games)

    # buat konfirmasi
    stars_given = "★" * nilai
    print_success(f"Rating {stars_given} ({nilai}) berhasil diberikan untuk '{game['nama_game']}'!")
    print_info(f"Rating baru game: {'★' * int(game['rating'])} {game['rating']}")
    pause()