import os
import shutil


def reset_dir(dir: str):
    """
    引数`dir`で指定したディレクトリがなければ作成、あれば削除後に作成
    """
    shutil.rmtree(dir, ignore_errors=True)
    os.makedirs(dir, exist_ok=True)
