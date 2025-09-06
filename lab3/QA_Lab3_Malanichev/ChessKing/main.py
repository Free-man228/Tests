
class GameObject:
    """
    Базовый класс для всех объектов в шахматной игре.
    Содержит общие атрибуты, такие как позиция.
    """

    def __init__(self, position):
        self.position = position  # Позиция в формате (x, y), где x - столбец (0-7), y - строка (0-7)

    def __str__(self):
        return f"Object at position {self.position}"


class Piece(GameObject):
    """
    Класс для шахматных фигур, наследует от GameObject.
    Добавляет цвет (white/black) и базовый метод для проверки хода.
    """

    def __init__(self, position, color):
        super().__init__(position)
        self.color = color  # 'white' или 'black'

    def is_valid_move(self, new_position):
        """
        Базовый метод для проверки валидности хода.
        Переопределяется в подклассах.
        """
        raise NotImplementedError("This method should be implemented in subclasses")

    def __str__(self):
        return f"{self.color.capitalize()} Piece at {self.position}"


class Pawn(Piece):
    """
    Класс для пешки, наследует от Piece.
    Реализует логику хода пешки (вперед на 1 или 2 клетки с начальной позиции).
    """

    def __init__(self, position, color):
        super().__init__(position, color)
        self.has_moved = False  # Флаг, чтобы отслеживать первый ход

    def is_valid_move(self, new_position):
        dx = new_position[0] - self.position[0]
        dy = new_position[1] - self.position[1]

        if self.color == 'white':
            direction = 1  # Белые двигаются вверх
        else:
            direction = -1  # Черные двигаются вниз

        # Пешка может двигаться вперед на 1 клетку
        if dx == 0 and dy == direction:
            self.has_moved = True
            return True

        # На первый ход - на 2 клетки
        if not self.has_moved and dx == 0 and dy == 2 * direction:
            self.has_moved = True
            return True

        return False  # Здесь не учитываем взятие, для простоты

    def __str__(self):
        return f"{self.color.capitalize()} Pawn at {self.position}"


class Knight(Piece):
    """
    Класс для коня, наследует от Piece.
    Реализует логику хода коня (L-образный ход).
    """

    def is_valid_move(self, new_position):
        dx = abs(new_position[0] - self.position[0])
        dy = abs(new_position[1] - self.position[1])

        # Конь ходит 2 в одну сторону и 1 в перпендикулярную
        if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
            return True

        return False

    def __str__(self):
        return f"{self.color.capitalize()} Knight at {self.position}"


class Board:
    """
    Класс для шахматной доски.
    Хранит фигуры и позволяет размещать/перемещать их.
    """

    def __init__(self):
        self.pieces = {}  # Словарь: позиция -> фигура

    def place_piece(self, piece):
        if piece.position in self.pieces:
            raise ValueError("Position already occupied")
        self.pieces[piece.position] = piece

    def move_piece(self, piece, new_position):
        if piece.is_valid_move(new_position):
            if new_position in self.pieces:
                print(f"Capturing {self.pieces[new_position]}")
                del self.pieces[new_position]  # Взятие фигуры
            del self.pieces[piece.position]
            piece.position = new_position
            self.pieces[new_position] = piece
            print(f"Moved {piece} to {new_position}")
        else:
            print("Invalid move!")

    def __str__(self):
        board_str = ""
        for y in range(7, -1, -1):  # От 7 до 0 для отображения сверху вниз
            for x in range(8):
                pos = (x, y)
                if pos in self.pieces:
                    board_str += self.pieces[pos].__str__()[0] + " "  # Первая буква фигуры
                else:
                    board_str += ". "
            board_str += "\n"
        return board_str


# Пример использования
if __name__ == "__main__":
    board = Board()

    # Создаем фигуры
    white_pawn = Pawn((0, 1), 'white')  # Пешка на a2
    black_knight = Knight((1, 7), 'black')  # Конь на b8

    # Размещаем на доске
    board.place_piece(white_pawn)
    board.place_piece(black_knight)

    print("Initial board:")
    print(board)

    # Двигаем пешку
    board.move_piece(white_pawn, (0, 3))  # На a4 (первый ход на 2)

    # Двигаем коня
    board.move_piece(black_knight, (2, 5))  # L-ход

    print("After moves:")
    print(board)