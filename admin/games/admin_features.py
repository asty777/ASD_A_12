from database.utils import read_file, write_file
from my_clear import cls 

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

def print_header(text, icon="🔧"):
    """Menampilkan header section"""
    print(f"\n{Colors.BLUE}{icon} {Colors.BOLD}{text}{Colors.RESET}")
    print(f"{Colors.CYAN}{'─'*40}{Colors.RESET}")

def print_success(text):
    """Menampilkan pesan sukses"""
    print(f"{Colors.GREEN}{text}{Colors.RESET}")

def print_error(text):
    """Menampilkan pesan error"""
    print(f"{Colors.RED}{text}{Colors.RESET}")

def print_warning(text):
    """Menampilkan pesan warning"""
    print(f"{Colors.YELLOW}{text}{Colors.RESET}")

def print_info(text):
    """Menampilkan pesan info"""
    print(f"{Colors.CYAN}{text}{Colors.RESET}")

def print_admin_box(title, options):
    print(f"\n{Colors.RED}{'═'*50}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.YELLOW}{title}{Colors.RESET}")
    print(f"{Colors.RED}{'═'*50}{Colors.RESET}")
    
    for key, value in options.items():
        print(f"  {Colors.GREEN}{key}.{Colors.RESET} {value}")
    
    print(f"{Colors.RED}{'═'*50}{Colors.RESET}")

def pause():
    """Jeda sampai user tekan Enter"""
    input(f"\n{Colors.CYAN}Tekan Enter untuk melanjutkan...{Colors.RESET}")

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
    cls()  
    games = load_games()

    if not games:
        print_warning("Belum ada game.")
        pause()
        return

<<<<<<< HEAD
    print_header("DAFTAR GAME", "📋")
    
    # tabel
    print(f"\n{Colors.BOLD}{Colors.CYAN}ID  | Nama Game{' ' * 20} | Genre{' ' * 10} | Rating{Colors.RESET}")
    print(f"{Colors.YELLOW}{'-'*55}{Colors.RESET}")
    
=======
    print("\n===== GAME =====")
>>>>>>> 60b0ea8ee8d5b11fecfe4ed71325d583a9d0e8a0
    for g in games:
        rating_star = "★" * int(g['rating']) if g['rating'] > 0 else "★ 0"
        print(f"{Colors.GREEN}{g['id']:3}{Colors.RESET} | {g['nama_game']:<25} | {g['genre']:<15} | {rating_star} {g['rating']}")
    
    print(f"{Colors.YELLOW}{'-'*55}{Colors.RESET}")
    pause()

# tambah game
def tambah():
    cls()
    print_header("TAMBAH GAME BARU", "+")
    
    games = load_games()

    nama = input(f"{Colors.CYAN}Nama game: {Colors.RESET}").strip()
    genre = input(f"{Colors.CYAN} Genre: {Colors.RESET}").strip()

    if not nama or not genre:
        print_error("Input tidak boleh kosong!")
        pause()
        return

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
    print_success(f"Game '{nama}' berhasil ditambahkan!")
    pause()

# update game
def update():
    cls()
    games = load_games()

    if not games:
        print_warning("Belum ada game.")
        pause()
        return

    print_header("UPDATE GAME", "✎")
    
    print(f"\n{Colors.BOLD}Daftar Game:{Colors.RESET}")
    for i, g in enumerate(games, 1):
        print(f"  {Colors.GREEN}{i}.{Colors.RESET} {g['nama_game']} ({g['genre']})")

    try:
        idx = int(input(f"\n{Colors.YELLOW}Pilih nomor game: {Colors.RESET}")) - 1

        if idx < 0 or idx >= len(games):
            print_error("Pilihan tidak valid!")
            pause()
            return

        game_lama = games[idx]['nama_game']
        print_info(f"Game lama: {game_lama}")
        
        nama_baru = input(f"{Colors.CYAN}Nama baru: {Colors.RESET}").strip()

        if not nama_baru:
            print_error("Nama tidak boleh kosong!")
            pause()
            return

        games[idx]["nama_game"] = nama_baru

        save_games(games)
        print_success(f"Game '{game_lama}' berhasil diupdate menjadi '{nama_baru}'!")
        pause()

    except ValueError:
        print_error("Input harus angka!")
        pause()

# hapus game
def delete():
    cls()
    games = load_games()

    if not games:
        print_warning("Belum ada game.")
        pause()
        return

    print_header("HAPUS GAME")
    
    print(f"\n{Colors.BOLD}Daftar Game:{Colors.RESET}")
    for i, g in enumerate(games, 1):
        rating_show = f"★ {g['rating']}" if g['rating'] > 0 else "Belum ada rating"
        print(f"  {Colors.GREEN}{i}.{Colors.RESET} {g['nama_game']} - {rating_show}")

    try:
        idx = int(input(f"\n{Colors.YELLOW}Pilih nomor game: {Colors.RESET}")) - 1

        if idx < 0 or idx >= len(games):
            print_error("Pilihan tidak valid!")
            pause()
            return

        game_hapus = games[idx]['nama_game']
        
        print_warning(f"Anda akan menghapus game '{game_hapus}'")
        konfirmasi = input(f"{Colors.RED}Yakin? (y/n): {Colors.RESET}").lower()
        
        if konfirmasi != "y":
            print_info("Penghapusan dibatalkan.")
            pause()
            return

        games.pop(idx)
        save_games(games)

        print_success(f"Game '{game_hapus}' berhasil dihapus!")
        pause()

    except ValueError:
        print_error("Input harus angka!")
        pause()

# menu admin utama
def admin_menu():
    while True:
        cls() 
        
        print(f"{Colors.RED}{'═'*50}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.YELLOW}  ADMIN CONTROL PANEL  {Colors.RESET}")
        print(f"{Colors.RED}{'═'*50}{Colors.RESET}")
        
        menu_options = {
            "1": "+ Tambah Game",
            "2": "✎ Update Game", 
            "3": " Delete Game",
            "4": "🗐 Lihat Game",
            "5": " Exit to Main Menu"
        }
        
        print_admin_box("MENU ADMIN", menu_options)
        
        pilih = input(f"{Colors.BOLD}{Colors.YELLOW} Pilih menu: {Colors.RESET}").strip()

        if pilih == "1":
            tambah()
        elif pilih == "2":
            update()
        elif pilih == "3":
            delete()
        elif pilih == "4":
            lihat()
        elif pilih == "5":
            print_success("Keluar dari Admin Panel...")
            break
        else:
            print_error("Pilihan tidak valid!")
            pause()