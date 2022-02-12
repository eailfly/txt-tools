import os


def splittxt():
    """
    title="前言"
    file= title.txt
    f = open(file, 'w')
    for line in lines:
      if not line.match('第*章'):
        f.write(line)
      else:
        title='line.get_titile_name()'
        file=  title.txt
        f.close()
        f = open(file, 'w')
        f.write(line)
    """
    NOVEL_NAME = ''
    SOURCE_PATH = os.getcwd() + '/' + NOVEL_NAME
    lines = open(SOURCE_PATH, 'r')
    title = "前言"
    file = title + '.txt'
    f = open(file, 'w')

    for line in lines:
        pass


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    splittxt()
