#!/usr/bin/python3

import sys


def initialize_board(n):
	"""Initialize an n x n chessboard with empty cells."""
	board = [[' ' for _ in range(n)] for _ in range(n)]
	return board

def mark_attack_spots(board, row, col):
	"""Mark the spots attacked by a queen."""
	n = len(board)
	for i in range(n):
		board[row][i] = 'x'  # Mark horizontally
		board[i][col] = 'x'  # Mark vertically

	if 0 <= row + i < n and 0 <= col + i < n:
		board[row + i][col + i] = 'x'  # Mark diagonally down-right

	if 0 <= row - i < n and 0 <= col - i < n:
		board[row - i][col - i] = 'x'  # Mark diagonally up-left

	if 0 <= row + i < n and 0 <= col - i < n:
		board[row + i][col - i] = 'x'  # Mark diagonally down-left

	if 0 <= row - i < n and 0 <= col + i < n:
		board[row - i][col + i] = 'x'  # Mark diagonally up-right


def recursive_solve(board, row, queens, solutions):
	"""Recursively solve the N-queens puzzle."""
	n = len(board)
	if queens == n:
		solutions.append([row[:] for row in board])
		return solutions

	for col in range(n):
		if board[row][col] == ' ':
			mark_attack_spots(board, row, col)
			board[row][col] = 'Q'
			solutions = recursive_solve(board, row + 1, queens + 1, solutions)
			mark_attack_spots(board, row, col)
			board[row][col] = ' '

	return solutions

def print_solution(solution):
	"""Print the solution in a readable format."""
	formatted_solution = []
	for pos in solution:
		formatted_solution.append([pos[0], pos[1]])
	print(formatted_solution)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: nqueens N")
		sys.exit(1)

	try:
		n = int(sys.argv[1])
	except ValueError:
		print("N must be a number")
		sys.exit(1)

	if n < 4:
		print("N must be a number greater than or equal to 4")
		sys.exit(1)

	board = initialize_board(n)
	solutions = recursive_solve(board, 0, 0, [])
	for solution in solutions:
		print_solution(solution)
