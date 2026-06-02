from database.utils import read_file, write_file
from my_clear import cls

# WARNA TERMINAL
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

# DATA GENRE
GENRE_LIST = [
    "Action",
    "Adventure",
    "RPG",
    "Strategy",
    "Simulation",
    "Sports",
    "Racing",
    "Puzzle"
]

# UTILITIES
def print_header(text, icon="🔧"):
    print(f"\n{Colors.BLUE}{icon} {Colors.BOLD}{text}{Colors.RESET}")
    print(f"{Colors.CYAN}{'─' * 50}{Colors.RESET}")


def print_success(text):
    print(f"{Colors.GREEN}{text}{Colors.RESET}")


def print_error(text):
    print(f"{Colors.RED}{text}{Colors.RESET}")


def print_warning(text):
    print(f"{Colors.YELLOW}{text}{Colors.RESET}")


def print_info(text):
    print(f"{Colors.CYAN}{text}{Colors.RESET}")


def print_admin_box(title, options):
    print(f"\n{Colors.RED}{'═' * 50}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.YELLOW}{title.center(50)}{Colors.RESET}")
    print(f"{Colors.RED}{'═' * 50}{Colors.RESET}")

    for key, value in options.items():
        print(f"  {Colors.GREEN}{key}.{Colors.RESET} {value}")

    print(f"{Colors.RED}{'═' * 50}{Colors.RESET}")


def pause():
    input(
        f"\n{Colors.CYAN}Tekan Enter untuk melanjutkan...{Colors.RESET}"
    )

# LOAD & SAVE
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
            game_id, nama, genre, rating, total, jumlah, played, downloads = parts

            games.append({
                "id": int(game_id),
                "nama_game": nama,
                "genre": genre,
                "rating": float(rating),
                "total_rating": int(total),
                "jumlah_rating": int(jumlah),
                "played": int(played),
                "downloads": int(downloads)
            })

        except ValueError:
            continue

    return games


def save_games(games):
    data = []

    for g in games:
        data.append(
            f"{g['id']}|"
            f"{g['nama_game']}|"
            f"{g['genre']}|"
            f"{g['rating']}|"
            f"{g['total_rating']}|"
            f"{g['jumlah_rating']}|"
            f"{g['played']}|"
            f"{g['downloads']}\n"
        )

    write_file("games.txt", data)



# LIHAT GAME
def lihat():
    cls()
    games = load_games()

    if not games:
        print_warning("Belum ada game.")
        pause()
        return

    print_header("DAFTAR GAME", "📋")

    print(
        f"\n{Colors.BOLD}{Colors.CYAN}"
        f"{'ID':<5}"
        f"{'Nama Game':<30}"
        f"{'Genre':<15}"
        f"{'Rating'}"
        f"{Colors.RESET}"
    )

    print(f"{Colors.YELLOW}{'-' * 65}{Colors.RESET}")

    for g in games:
        print(
            f"{Colors.GREEN}{g['id']:<5}{Colors.RESET}"
            f"{g['nama_game']:<30}"
            f"{g['genre']:<15}"
            f"{g['rating']:.1f}"
        )

    print(f"{Colors.YELLOW}{'-' * 65}{Colors.RESET}")
    pause()

# TAMBAH GAME
def tambah():
    cls()
    print_header("TAMBAH GAME BARU", "➕")

    games = load_games()

    nama = input(
        f"{Colors.CYAN}Nama Game: {Colors.RESET}"
    ).strip()

    if not nama:
        print_error("Nama game tidak boleh kosong!")
        pause()
        return

    for g in games:
        if g["nama_game"].lower() == nama.lower():
            print_error("Game sudah ada!")
            pause()
            return

    print(f"\n{Colors.CYAN}Pilih Genre:{Colors.RESET}")

    for i, genre in enumerate(GENRE_LIST, start=1):
        print(f"{i}. {genre}")

    try:
        pilihan = int(
            input(
                f"\n{Colors.YELLOW}Pilih nomor genre: {Colors.RESET}"
            )
        )

        if pilihan < 1 or pilihan > len(GENRE_LIST):
            print_error("Pilihan tidak valid!")
            pause()
            return

        genre = GENRE_LIST[pilihan - 1]

    except ValueError:
        print_error("Input harus berupa angka!")
        pause()
        return

    new_id = max(
        [g["id"] for g in games],
        default=0
    ) + 1

    games.append({
        "id": new_id,
        "nama_game": nama,
        "genre": genre,
        "rating": 0.0,
        "total_rating": 0,
        "jumlah_rating": 0,
        "played": 0,
        "downloads": 0
    })

    save_games(games)

    print_success(f"Game '{nama}' berhasil ditambahkan!")
    pause()

# UPDATE GAME
def update():
    cls()
    games = load_games()

    if not games:
        print_warning("Belum ada game.")
        pause()
        return

    print_header("UPDATE GAME", "✎")

    for i, g in enumerate(games, start=1):
        print(
            f"{Colors.GREEN}{i}.{Colors.RESET} "
            f"{g['nama_game']} ({g['genre']})"
        )

    try:
        idx = int(
            input(
                f"\n{Colors.YELLOW}Pilih nomor game: {Colors.RESET}"
            )
        ) - 1

        if idx < 0 or idx >= len(games):
            print_error("Pilihan tidak valid!")
            pause()
            return

        game_lama = games[idx]["nama_game"]

        nama_baru = input(
            f"{Colors.CYAN}Nama Baru: {Colors.RESET}"
        ).strip()

        if not nama_baru:
            print_error("Nama tidak boleh kosong!")
            pause()
            return

        print("\nPilih Genre Baru:")

        for i, genre in enumerate(GENRE_LIST, start=1):
            print(f"{i}. {genre}")

        genre_idx = int(
            input(
                f"{Colors.YELLOW}Pilih genre: {Colors.RESET}"
            )
        )

        if genre_idx < 1 or genre_idx > len(GENRE_LIST):
            print_error("Genre tidak valid!")
            pause()
            return

        genre_baru = GENRE_LIST[genre_idx - 1]

        games[idx]["nama_game"] = nama_baru
        games[idx]["genre"] = genre_baru

        save_games(games)

        print_success(
            f"Game '{game_lama}' berhasil diupdate!"
        )

        pause()

    except ValueError:
        print_error("Input harus angka!")
        pause()

# HAPUS GAME
def hapus_game():
    cls()
    games = load_games()

    if not games:
        print_warning("Belum ada game.")
        pause()
        return

    print_header("HAPUS GAME", "🗑️")

    for i, g in enumerate(games, start=1):
        print(
            f"{Colors.GREEN}{i}.{Colors.RESET} "
            f"{g['nama_game']} ({g['genre']})"
        )

    try:
        idx = int(
            input(
                f"\n{Colors.YELLOW}Pilih nomor game: {Colors.RESET}"
            )
        ) - 1

        if idx < 0 or idx >= len(games):
            print_error("Pilihan tidak valid!")
            pause()
            return

        game_hapus = games[idx]["nama_game"]

        konfirmasi = input(
            f"{Colors.RED}Yakin hapus '{game_hapus}'? (y/n): "
            f"{Colors.RESET}"
        ).lower()

        if konfirmasi != "y":
            print_info("Penghapusan dibatalkan.")
            pause()
            return

        games.pop(idx)

        save_games(games)

        print_success(
            f"Game '{game_hapus}' berhasil dihapus!"
        )

        pause()

    except ValueError:
        print_error("Input harus angka!")
        pause()



# MENU ADMIN
def admin_menu():
    while True:
        cls()

        print(f"{Colors.RED}{'═' * 50}{Colors.RESET}")
        print(
            f"{Colors.BOLD}{Colors.YELLOW}"
            f"{'ADMIN CONTROL PANEL'.center(50)}"
            f"{Colors.RESET}"
        )
        print(f"{Colors.RED}{'═' * 50}{Colors.RESET}")

        menu_options = {
            "1": "+ Tambah Game",
            "2": "✎ Update Game", 
            "3": " Delete Game",
            "4": "🗐 Lihat Game",
            "5": " Exit to Main Menu"
        }

        print_admin_box("MENU ADMIN", menu_options)

        pilih = input(
            f"{Colors.BOLD}{Colors.YELLOW}"
            f"Pilih Menu: "
            f"{Colors.RESET}"
        ).strip()

        if pilih == "1":
            tambah()

        elif pilih == "2":
            update()

        elif pilih == "3":
            hapus_game()

        elif pilih == "4":
            lihat()

        elif pilih == "5":
            print_success("Keluar dari Admin Panel...")
            break

        else:
            print_error("Pilihan tidak valid!")
            pause()         