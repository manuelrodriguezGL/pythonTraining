def save_file(object_to_save, path):
    try:
        f = open(path, "a")
        f.write(object_to_save + "\n")
    except Exception:
        print("Could not save file")
    finally:
        f.close()


def read_file(path):
    result = []
    try:
        f = open(path, "r")
        for a in f.readlines():
            result.append(a)
    except Exception:
        print("Could not read file")
    finally:
        f.close()
    return result

