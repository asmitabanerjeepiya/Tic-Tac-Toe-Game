#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import tkinter as tk
from tkinter import messagebox


def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions


def check_draw(board):
    return not any(" " in row for row in board)


def minimax(board, depth, is_maximizing):
    if check_win(board, "O"):
        return 1
    if check_win(board, "X"):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score


def best_move(board):
    best_score = -np.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=" ", font=('normal', 40), width=5, height=2,
                                               command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, i, j):
        if self.board[i][j] == " ":
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if check_win(self.board, self.current_player):
                messagebox.showinfo("Tic-Tac-Toe", f"{self.current_player} wins!")
                self.root.quit()
            elif check_draw(self.board):
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.root.quit()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.ai_move()

    def ai_move(self):
        move = best_move(self.board)
        if move:
            self.board[move[0]][move[1]] = "O"
            self.buttons[move[0]][move[1]].config(text="O")
            if check_win(self.board, "O"):
                messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
                self.root.quit()
            elif check_draw(self.board):
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.root.quit()
            self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()


# In[ ]:




