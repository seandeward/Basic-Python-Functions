def get_character_record(name, server, level, rank):
    return { # ? YOU CAN HAVE THE DICTIONARY ON THE RETURN
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}"
    }

if __name__ == "__main__":
    username = "frozenboi"
    server = "server 1"
    level = 5
    rank = 2
    print(get_character_record(username, server, level, rank))
    