import os
import sqlite3

import alembic.config
from fire import Fire

from utils.reset_dir import reset_dir


class Commands:
    def reset(self):
        dist_path = 'dist/'
        reset_dir(dist_path)

        filepath = os.path.join(dist_path, 'css_milestone.sqlite')
        sqlite3.connect(filepath).close()
        alembic.config.main(argv=['upgrade', 'head'])


if __name__ == '__main__':
    Fire(Commands)
