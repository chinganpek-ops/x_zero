# game.py

from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError
<<<<<<< HEAD


def save_result(result):
    with open('results.txt', 'a', encoding='utf-8') as f:
    f.write(result + '\n')
=======
>>>>>>> d5bd1ee1b1f2b6584052091592cbf235ce42c24f

def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:

        print(f'Ход делают {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята.')
                print('Пожалуйста, введите другие координаты.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        game.display()
        # После каждого хода надо делать проверку на победу и на ничью
        if game.check_win(current_player):
<<<<<<< HEAD
            result = f'Победили {current_player}.'
            print(result)
            save_result(result)
            running = False

        elif game.is_board_full():
            result = 'Ничья!'
            print(result)
            save_result(result)
=======
            print(f'Победили {current_player}.')
            running = False
        elif game.is_board_full():
            print('Ничья!')
>>>>>>> d5bd1ee1b1f2b6584052091592cbf235ce42c24f
            running = False

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    main()
