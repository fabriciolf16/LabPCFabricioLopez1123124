def create_board():
    board = [['--' for _ in range(8)] for _ in range(8)]
    return board

def print_board(board, valid_moves):
    # Imprimir letras verticales
    print("   " + "  ".join([chr(97 + i) for i in range(8)]))
    # Imprimir filas
    for i, row in enumerate(board):
        print(f"{i+1} ", end=" ")  # Imprimir número de fila
        # Imprimir contenido de la fila
        for j, square in enumerate(row):
            if (i, j) in valid_moves:
                print(f"[{square}]", end=' ')
            else:
                print(square, end=' ')
        print()
    print()

def parse_position(pos_str):
    if len(pos_str) != 2:
        raise ValueError(f"Posición inválida: {pos_str}. Debe ser en formato <Letra><Número>.")
    
    col_str, row_str = pos_str[0], pos_str[1]
    
    if col_str < 'a' or col_str > 'h' or row_str < '1' or row_str > '8':
        raise ValueError(f"Posición inválida: {pos_str}. La columna debe ser de 'a' a 'h' y la fila de '1' a '8'.")
    
    col = ord(col_str) - ord('a')
    row = 8 - int(row_str)
    return row, col

def position_to_notation(row, col):
    return chr(col + ord('a')) + str(8 - row)

def is_valid_position(row, col):
    return 0 <= row < 8 and 0 <= col < 8

def add_piece(board, piece, color, position):
    row, col = parse_position(position)
    if board[row][col] == '--':
        board[row][col] = color + piece
        return True
    else:
        print("La posición ya está ocupada. Intenta de nuevo.")
        return False

def add_pieces(board):
    while True:
        piece = input("Introduce el tipo de pieza (alfil, peón, torre, reina, rey) o 'listo' para finalizar: ").lower()
        if piece == 'listo':
            break
        if piece not in ['alfil', 'peón', 'torre', 'reina', 'rey']:
            print("Tipo de pieza inválido. Intenta de nuevo.")
            continue
        
        color = input("Introduce el color (blanco, negro): ").lower()
        if color not in ['blanco', 'negro']:
            print("Color inválido. Intenta de nuevo.")
            continue
        color = 'b' if color == 'blanco' else 'n'
        
        position = input("Introduce la posición (ej. 'e4'): ")
        try:
            if not is_valid_position(*parse_position(position)):
                print("Posición inválida. Intenta de nuevo.")
                continue
            if not add_piece(board, piece[0].upper(), color, position):
                continue
        except ValueError as e:
            print(e)

def get_knight_position(board):
    while True:
        color = input("Introduce el color del caballo (blanco, negro): ").lower()
        if color not in ['blanco', 'negro']:
            print("Color inválido. Intenta de nuevo.")
            continue
        color = 'b' if color == 'blanco' else 'n'
        
        position = input("Introduce la posición del caballo (ej. 'e4'): ")
        try:
            row, col = parse_position(position)
            if not is_valid_position(row, col):
                print("Posición inválida. Intenta de nuevo.")
                continue
            if board[row][col] == '--':
                board[row][col] = color + 'C'
                return position, color
            else:
                print("La posición ya está ocupada. Intenta de nuevo.")
        except ValueError as e:
            print(e)

def get_knight_moves(position, board, color):
    # El caballo se mueve en forma de "L"
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    row, col = parse_position(position)
    valid_moves = []

    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if is_valid_position(new_row, new_col):
            if board[new_row][new_col] == '--':
                valid_moves.append((new_row, new_col))
            elif board[new_row][new_col][0] != color:
                valid_moves.append((new_row, new_col))
    
    return valid_moves

def main():
    board = create_board()
    add_pieces(board)
    knight_position, knight_color = get_knight_position(board)
    
    print("\nTablero después de agregar las piezas:")
    valid_moves = get_knight_moves(knight_position, board, knight_color)
    print_board(board, valid_moves)

    print("\nMovimientos válidos del caballo:")
    for move in valid_moves:
        pos_notation = position_to_notation(move[0], move[1])
        print(pos_notation)

    print("\nMatriz del tablero:")
    for row in board:
        print(row)

if __name__ == "__main__":
    main()
