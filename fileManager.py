class FileManager:

    def save_file(self, object_to_save, path):
        saved = False
        try:
            f = open(path, "a")
            f.write(object_to_save + "\n")
            saved = True
        except Exception:
            print("Could not save file")
        finally:
            try:
                f.close()
            except Exception:
                print("Could not close file!")
                saved = False
        return saved

    def read_file(self, path):
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

