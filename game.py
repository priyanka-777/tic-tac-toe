#!/usr/bin/python3
l="abcdefghi"
board = { "a":"a", "b" :"b","c":"c","d" : "d","e": "e","f":"f","g":"g","h":"h","i":"i"}
def prin(board):
	print("\n",board["a"] if(board["a"]!="a") else " ",end="")
	print(" |",board["b"] if(board["b"]!="b") else " ",end="")
	print(" |",board["c"] if(board["c"]!="c") else " ",end="")
	print("\n---+---+---\n ",end="")
	print(board["d"] if(board["d"]!="d") else " ",end="")
	print(" |",board["e"] if(board["e"]!="e") else " ",end="")
	print(" |",board["f"] if(board["f"]!="f") else " ",end="")
	print("\n---+---+---\n ",end="")
	print(board["g"] if(board["g"]!="g") else " ",end="")
	print(" |",board["h"] if(board["h"]!="h") else " ",end="")
	print(" |",board["i"] if(board["i"]!="i") else " ")
def win(board):
	if(board["a"]==board["b"]==board["c"] or board["a"]==board["d"]==board["g"] or board["a"]==board["e"]==board["i"]):
		print(player1 if board["a"]=="X" else player2,"Won the game")
		return 1
	elif(board["b"] == board["e"] == board["h"]):
		print(player1 if board["b"]=="X" else player2,"Won the game")
		return 1
	elif(board["c"]==board["f"]==board["i"] or board["c"] == board["e"]==board["g"]):
		print(player1 if board["c"]=="X" else player2,"Won the game")
		return 1
	elif(board["d"]==board["e"]==board["f"]):
		print(player1 if board["d"]=="X" else player2,"Won the game")
		return 1
	elif(board["g"]==board["h"]==board["i"]):
		print(player1 if board["g"]=="X" else player2,"Won the game")
		return 1
	else:
		return 0
a="X"
cv=0
player1=input("Enter Player 1 name:")
player2=input("Enter Player 2 name:")
print("\n a | b | c\n---+---+---\n d | e | f \n---+---+---\n g | h | i ")
print("\n\n\t* * * GAME STARTS * * ")
prin(board)
while(cv<9):
	print("Enter the place for \"",a,"\"and Enter only character between a-i")
	b=input()
	if(b in l):
		if(board[b]!="X" or board[b]!="O"):
			board[b]=a
			cv+=1
			if(cv>2):
				rc=win(board)
				if(rc==1):
					print("Final Board")
					prin(board)
					break
			prin(board)
			if(a=="X"):
				a="O"
			else:
				a="X"
