import os
import argparse

import server_config
from server import Server

def parser_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=str, help='root directory', default=server_config.ROOT)
    parser.add_argument('--ncpu', type=int, help='number cpu', default=server_config.CPU_NUMBER)
    return parser.parse_args()


def run():
    args = parser_args()
    # Проверка root директории на существование
    if (os.path.exists(args.root)):
        server = Server(args.root, args.ncpu)
        server.start()
    else:
        print('Not valid root directory')


if __name__ == '__main__':
    run()