import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        # Initialize the game
        self.master = master
        self.master.title("Tic Tac Toe")  # Set window title
        self.board = [[' ']*3 for _ in range(3)]  # Initialize empty board
        self.current_player = 'X'  # Start with player X
        self.buttons = [[None]*3 for _ in range(3)]  # Initialize button grid
        self.create_board()  # Create the game board

    def create_board(self):
        # Create the game board with buttons
        for i in range(3):
            for j in range(3):
                # Create a button for each cell, with a command to handle clicks
                self.buttons[i][j] = tk.Button(self.master, text='', font=('Arial', 30), width=5, height=2,
                                                command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)  # Place the button in the grid

    def on_button_click(self, row, col):
        # Handle button clicks
        if self.board[row][col] == ' ':  # If the cell is empty
            self.board[row][col] = self.current_player  # Mark the cell with current player
            self.buttons[row][col].config(text=self.current_player)  # Update button text
            if self.check_win():  # Check for a win
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")  # Show win message
                self.reset_game()  # Reset the game
            elif self.check_tie():  # Check for a tie
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")  # Show tie message
                self.reset_game()  # Reset the game
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'  # Switch player

    def check_win(self):
        # Check for a win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ' or \
                self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True  # If any row or column has same symbols, return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ' or \
            self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True  # If any diagonal has same symbols, return True
        return False  # Otherwise, return False

    def check_tie(self):
        # Check for a tie
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))  # If all cells are filled, return True

    def reset_game(self):
        # Reset the game
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state=tk.NORMAL)  # Reset button text and enable buttons
                self.board[i][j] = ' '  # Reset board cell
        self.current_player = 'X'  # Reset current player to X

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()