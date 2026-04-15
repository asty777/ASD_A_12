def read_file(filename):
    try:
        with open("database/" + filename, "r") as f:
            return f.readlines()
    except:
        return []

def write_file(filename, data):
    with open("database/" + filename, "w") as f:
        f.writelines(data)

        