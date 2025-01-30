import random
import sys

class FifteenPuzzle:
    def __init__(self):
        self.board = list(range(1, 16)) + ['x']
        self.empty_pos = 15
        self.moves = 0
        self.shuffle_board()

    def shuffle_board(self):
        # Генерация корректного начального состояния
        while True:
            random.shuffle(self.board)
            if self.is_solvable():
                break
        self.empty_pos = self.board.index('x')

    def is_solvable(self):
        # Проверка на разрешимость головоломки
        inversions = 0
        for i in range(len(self.board)):
            for j in range(i + 1, len(self.board)):
                if self.board[i] != 'x' and self.board[j] != 'x' and self.board[i] > self.board[j]:
                    inversions += 1
        return inversions % 2 == 0

    def print_board(self):
        # Вывод поля в консоль
        for i in range(0, 16, 4):
            print(" ".join(str(x).rjust(2) for x in self.board[i:i+4]))
        print()

    def move(self, direction):
        # Перемещение пустой клетки
        x, y = self.empty_pos % 4, self.empty_pos // 4
        if direction == 'w' and y > 0:
            new_pos = self.empty_pos - 4
        elif direction == 's' and y < 3:
            new_pos = self.empty_pos + 4
        elif direction == 'a' and x > 0:
            new_pos = self.empty_pos - 1
        elif direction == 'd' and x < 3:
            new_pos = self.empty_pos + 1
        else:
            print("Невозможный ход!")
            return False

        self.board[self.empty_pos], self.board[new_pos] = self.board[new_pos], self.board[self.empty_pos]
        self.empty_pos = new_pos
        self.moves += 1
        return True

    def is_solved(self):
        # Проверка на завершение игры
        return self.board == list(range(1, 16)) + ['x']

    def play(self):
        print("Добро пожаловать в игру 'Пятнашки'!")
        print("Используйте клавиши WASD для перемещения пустой клетки (x).")
        print("Для выхода нажмите Ctrl+C.\n")
        self.print_board()

        try:
            while not self.is_solved():
                direction = input("Ваш ход (w/a/s/d): ").lower()
                if direction in ['w', 'a', 's', 'd']:
                    if self.move(direction):
                        self.print_board()
                else:
                    print("Некорректный ввод! Используйте только w/a/s/d.")

            print(f"Поздравляем! Вы решили головоломку за {self.moves} ходов.")
        except KeyboardInterrupt:
            print("\nshutting down")
            sys.exit(0)

if __name__ == "__main__":
    game = FifteenPuzzle()
    game.play()