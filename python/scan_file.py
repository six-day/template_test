import os


def traversal_files(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            print(name)
            print(path)
            contents = read_file(path)
            write_file(os.path.join(".target/", root), name, contents)
        for name in dirs:
            print(os.path.join(root, name))


def write_file(root, name, contents):
    if not os.path.exists(root):
        os.makedirs(root)
    path = os.path.join(root, name)
    with open(path, 'w', encoding="utf-8") as file:
        file.write(contents)
    file.close()


def read_file(path):
    with open(path, encoding='utf-8') as file:
        # 读取文件
        contents = file.read()
    file.close()
    # print(contents)
    return contents


if __name__ == '__main__':
    path = 'resource'
    traversal_files(path)
