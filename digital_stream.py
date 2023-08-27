import random
import shutil
import sys
import time


class DigitalStream:
    def __init__(self):
        self.MIN_STREAM_LENGTH = 6
        self.MAX_STREAM_LENGTH = 14
        self.PAUSE = 0.1
        self.STREAM_CHARS = ['0', '1']
        self.DENSITY = 0.02
        self.WIDTH = shutil.get_terminal_size()[0] - 1

    def run(self):
        print('Digital Stream')
        print('Press Ctrl-C to quit.')
        time.sleep(2)

        try:
            columns = [0] * self.WIDTH
            while True:
                self.update_columns(columns)
                self.display_columns(columns)
                time.sleep(self.PAUSE)
        except KeyboardInterrupt:
            sys.exit()

    def update_columns(self, columns):
        for i in range(self.WIDTH):
            if columns[i] == 0:
                if random.random() <= self.DENSITY:
                    columns[i] = random.randint(
                        self.MIN_STREAM_LENGTH, self.MAX_STREAM_LENGTH)

    def display_columns(self, columns):
        for i in range(self.WIDTH):
            if columns[i] > 0:
                print(random.choice(self.STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print()
        sys.stdout.flush()


if __name__ == '__main__':
    stream = DigitalStream()
    stream.run()
