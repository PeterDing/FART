"""
注意一些壳会把 dexfile[:8] 的 magic code
抹去，让内存搜索 magic code 的方法失效。
所以在 dump 下 dex 后要把 magic code 填回去。
"""
import sys
import shutil
from pathlib import Path


def is_dex(path: Path):
    magic = path.open('rb').read(7)
    if magic == b'dex\n035':
        return True
    else:
        return False


def add_magic(path: Path):
    f = path.open('r+b')
    f.seek(0)
    f.write(b'dex\n035')
    f.close()


def handle_dir(path: Path):
    for dex_path in path.glob('*dex'):
        handle_file(dex_path)


def handle_file(path: Path):
    if not path.exists() or path.is_dir():
        return

    if not is_dex(path):
        if path.suffix == '.dex':
            fixed = Path(str(path) + '.fixed.dex')
            shutil.copyfile(path, fixed)
            print(f'Add magic code for {path} to {fixed}\n')
            add_magic(fixed)


def main():
    paths = sys.argv[1:]
    if not paths:
        return

    for path in paths:
        path = Path(path)
        if not path.exists():
            return

        if path.is_dir():
            handle_dir(path)

        if path.is_file():
            handle_file(path)


if __name__ == '__main__':
    main()
