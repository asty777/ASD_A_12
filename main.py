from my_clear import cls
from auth.login import login
from user.games.game_features import (
    lihat_game,
    leaderboard,
    search_game,
    rating_game
)
from admin.games.admin_features import admin_menu

# warna
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

def print_banner():
    """Menampilkan banner aplikasi"""
    banner = f"""
{Colors.CYAN}{'='*60}
{Colors.BOLD}     LEADERBOARD GAME     {Colors.RESET}
{Colors.CYAN}{'='*60}{Colors.RESET}
    """
    print(banner)
    

def print_menu_box(title, options):
    """Menampilkan menu dalam box yang rapi"""
    print(f"\n{Colors.YELLOW}{'─'*50}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN} {title}{Colors.RESET}")
    print(f"{Colors.YELLOW}{'─'*50}{Colors.RESET}")
    
    for key, value in options.items():
        print(f"  {Colors.GREEN}{key}.{Colors.RESET} {value}")
    
    print(f"{Colors.YELLOW}{'─'*50}{Colors.RESET}")

def print_header(text, icon="✦"):
    """Menampilkan header section"""
    print(f"\n{Colors.BLUE}{icon} {Colors.BOLD}{text}{Colors.RESET}")
    print(f"{Colors.CYAN}{'─'*40}{Colors.RESET}")

def print_success(text):
    """Menampilkan pesan sukses"""
    print(f"{Colors.GREEN} {text}{Colors.RESET}")

def print_error(text):
    """Menampilkan pesan error"""
    print(f"{Colors.RED} {text}{Colors.RESET}")

def print_info(text):
    """Menampilkan pesan info"""
    print(f"{Colors.CYAN}  {text}{Colors.RESET}")

def print_warning(text):
    """Menampilkan pesan warning"""
    print(f"{Colors.YELLOW}⚠︎ {text}{Colors.RESET}")

def loading_animation():
    """Animasi loading sederhana"""
    import time
    for i in range(3):
        print(f"{Colors.CYAN}.{Colors.RESET}", end="", flush=True)
        time.sleep(0.3)
    print()

def main():
    cls()
    print_banner()
    
    user = None

    # login -- prosesnya
    print(f"{Colors.CYAN} Memulai proses login...{Colors.RESET}")
    while user is None:
        user = login()

    cls()

    print(f"{Colors.GREEN}✓ Login berhasil!{Colors.RESET}")
    print(f"{Colors.CYAN} Memuat dashboard...{Colors.RESET}", end="")
    loading_animation()

    # menu
    while True:
        cls()
        print(f"\n{Colors.BOLD}{Colors.GREEN} User: {user['username']} ({user['role']}){Colors.RESET}")
        # Menu User
        if user["role"] == "user":
            menu_options = {
                "1": "Lihat Game",
                "2": "Leaderboard", 
                "3": "Search Game",
                "4": "Rating Game",
                "0": "Exit"
            }
            
            print_menu_box("MENU UTAMA", menu_options)
            
            pilih = input(f"{Colors.BOLD}{Colors.YELLOW} Pilih menu: {Colors.RESET}").strip()

            if pilih == "1":
                cls()
                print_header("DAFTAR GAME")
                lihat_game()
            elif pilih == "2":
                cls()
                print_header("LEADERBOARD")
                leaderboard()
            elif pilih == "3":
                cls()
                print_header("PENCARIAN GAME")
                search_game()
            elif pilih == "4":
                cls()
                print_header("BERI RATING")
                rating_game(user)
            elif pilih == "0":
                (cls)
                print_success("\nTerima kasih atas waktunya! Sampai jumpa lagi!!")
                print(f"{Colors.CYAN}{'='*50}{Colors.RESET}")
                break
            else:
                print_error("Pilihan tidak valid! Silakan coba lagi.")

        # Admin
        elif user["role"] == "admin":
            cls()
            print_warning("Anda dalam mode admin")
            print_header("ADMIN DASHBOARD", "🔧")
            admin_menu()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        cls()
        print(f"\n\n{Colors.YELLOW}⚠︎  Program dihentikan oleh pengguna{Colors.RESET}")
        print(f"{Colors.GREEN}Terima kasih!{Colors.RESET}")
    except Exception as e:
        print_error(f"Terjadi error: {str(e)}")