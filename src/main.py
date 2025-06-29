import os, shutil
from classes.textnode import TEXT_TYPE, TextNode

def main():
    shutil.rmtree('./public')
    os.mkdir('./public')
    copy_static('static', 'public')

def copy_static(origin, destination):
    print(f"origin: {origin}, destination: {destination}")
    static_files = os.listdir(origin)

    for path in static_files:
        src_path = f"{origin}/{path}"
        out_path= f"{destination}/{path}"

        is_file = os.path.isfile(src_path)
        print(f"{src_path} is file? {is_file}")

        if is_file:
            shutil.copy(src_path, out_path)
            continue

        os.mkdir(out_path)
        copy_static(src_path, out_path)


if __name__ == "__main__":
    main()
