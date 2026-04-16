def load_users_txt():
    users = []
    with open("database/users.txt", "r") as f:
        for line in f:
            parts = line.strip().split(",")

            # pastikan format benar
            if len(parts) != 4:
                continue

            id, username, password, role = parts

            users.append({
                "id": int(id),
                "username": username.strip(),
                "password": password.strip(),
                "role": role.strip()
            })

    return users


def login():
    users = load_users_txt()

    print("=== LOGIN ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"\nLogin berhasil sebagai {user['role']}!\n")
            return user

    print("\nUsername atau password salah!\n")
    return None