def register():
    print("\n=== REGISTER ===")

    username = input("Masukkan username: ")
    if not username:
        print("Username tidak boleh kosong!")
        return
    
    password = input("Masukkan password: ")
    if not password:
        print("Password tidak boleh kosong!")
        return

    # Baca data admin
    try:
        with open("database/admin.txt", "r") as f:
            admin_data = f.readlines()
    except FileNotFoundError:
        admin_data = []

    # Baca data user
    try:
        with open("database/user.txt", "r") as f:
            user_data = f.readlines()
    except FileNotFoundError:
        user_data = []

    # Ambil semua username
    semua_username = []

    for admin in admin_data:
        data = admin.strip().split(",")
        if len(data) >= 1:
            semua_username.append(data[0])

    for user in user_data:
        data = user.strip().split(",")
        if len(data) >= 1:
            semua_username.append(data[0])

    # Cek username sudah ada atau belum
    if username in semua_username:
        print("Username sudah digunakan! Coba yang lain.")
        return

    # Simpan ke user.txt
    with open("database/user.txt", "a") as f:
        f.write(f"{username},{password}\n")

    print(f"Berhasil! Akun '{username}' telah dibuat.")