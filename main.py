from auth.login import login
from user.games.game_features import (
    lihat_game,
    leaderboard,
    search_game,
    rating_game
)
from admin.games.admin_features import admin_menu


def main():
    user = None

    #login
    while user is None:
        user = login()

    # Main Menu
    while True:
        print("\n=== MENU UTAMA ===")

        # User Menu
        if user["role"] == "user":
            print("1. Lihat Game")
            print("2. Leaderboard")
            print("3. Search Game")
            print("4. Rating Game")
            print("0. Exit")

            pilih = input("Pilih menu: ").strip()

            if pilih == "1":
                lihat_game()
            elif pilih == "2":
                leaderboard()
            elif pilih == "3":
                search_game()
            elif pilih == "4":
                rating_game(user)
            elif pilih == "0":
                print("\nTerima kasih 🎮")
                break
            else:
                print("Pilihan tidak valid!")

        # admin menu
        elif user["role"] == "admin":
            print("1. Admin Menu")
            print("0. Exit")

            pilih = input("Pilih menu: ").strip()

            if pilih == "1":
                admin_menu()
            elif pilih == "0":
                print("\nTerima kasih 🎮")
                break
            else:
                print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()