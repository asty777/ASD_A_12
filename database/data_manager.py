import os

def load_data(file, default):
    """Load data dari file txt dengan format per baris"""
    if not os.path.exists(file):
        return default
    
    data = []
    try:
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    # Asumsi format: id|user_id|game_id|rating
                    parts = line.split("|")
                    if len(parts) == 4:
                        data.append({
                            "id": int(parts[0]),
                            "user_id": int(parts[1]),
                            "game_id": int(parts[2]),
                            "rating": int(parts[3])
                        })
    except:
        return default
    
    return data

def save_data(file, data):
    """Save data ke file txt dengan format per baris"""
    with open(file, "w", encoding="utf-8") as f:
        for item in data:
            line = f"{item['id']}|{item['user_id']}|{item['game_id']}|{item['rating']}\n"
            f.write(line)