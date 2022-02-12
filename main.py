import os
import re


def splittxt():
    NOVEL_NAME = ''
    SOURCE_PATH = os.getcwd() + '/' + NOVEL_NAME
    print(f"Split file: {SOURCE_PATH}")
    pattern = r"(第.*章) (.*)\n"
    SOURCE_FILE = open(SOURCE_PATH, 'r')
    lines = SOURCE_FILE.readlines()
    title = "前言"
    index = 0
    file = f"results/{index}.{title}.txt"
    f = open(file, 'w')

    for line in lines:
        if re.search(pattern, line):
            f.close()
            index += 1
            match = re.search(pattern, line)
            title = f"{index}.{match.group(2)}"
            file = f"results/{title}.txt"
            print(f"New file: {file}")
            f = open(file, 'w')
            f.write(line)
            f.write('\n')
        else:
            print("New line\n")
            f.write(line)

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    splittxt()
