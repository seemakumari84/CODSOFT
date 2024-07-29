import tensorflow as tf
print(tf.__version__)

def is_board_full(board):
  for space in board:
    if space == " ":
      return False
  return True

def is_winner(board, symbol):
  winning_conditions = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8],
      [0, 3, 6], [1, 4, 7], [2, 5, 8],
      [0, 4, 8], [2, 4, 6]
  ]
  for condition in winning_conditions:
    if board[condition[0]] == symbol and board[condition[1]] == symbol and board[condition[2]] == symbol:
      return True
  return False

def print_board(board):
  for i in range(3):
    for j in range(3):
      print(board[i*3 + j], end=" ")
    print()

def main():
  board = [" "] * 9

  current_player = "X"  
  game_over = False

  while not game_over:
    print_board(board)

    while True:
      try:
        move = int(input(f"Player {current_player}, enter your move (1-9): "))
        if 1 <= move <= 9 and board[move - 1] == " ":
          break
        else:
          print("Invalid move. Try again.")
      except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")

    board[move - 1] = current_player

    if is_winner(board, current_player):
      print_board(board)
      print(f"Player {current_player} wins!")
      game_over = True
      break

    if is_board_full(board):
      print_board(board)
      print("It's a tie!")
      game_over = True
      break

    current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
  main()
