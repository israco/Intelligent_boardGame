# Intelligent_boardGame
The game is a simulation of ground warfare and has the following rules:
1. The game board is an NxN grid representing the territory your forces will trample (N=5 in the figures
below). Columns are named A, B, C, … starting from the left, and rows are named 1, 2, 3, … from top.
2. Each player takes turns as in chess or tic-tac-toe. That is, player X takes a move, then player O, then
back to player X, and so forth.
3. Each square has a fixed point value between 1 and 99, based upon its computed strategic and resource
value.
4. The object of the game for each player is to score the most points, where score is the sum of all point
values of all his or her occupied squares minus the sum of all points in the squares occupied by the
other player. Thus, one wants to capture the squares worth the most points while preventing the other
player to do so.
5. The game ends when all the squares are occupied by the players since no more moves are left.
6. Players cannot pass their move, i.e., they must make a valid move if one exists (game is not over).
7. Movement and adjacency relations are always vertical and horizontal but never diagonal.10. On each turn, a player can make one of two moves:
Stake – You can take any open space on the board. This will create a new piece on the board. This move can
be made as many times as one wants to during the game, but only once per turn. However, a Stake cannot
conquer any pieces. It simply allows one to arbitrarily place a piece anywhere unoccupied on the board. Once
you have done a Stake, your turn is complete.
Raid – From any space you occupy on the board, you can take the one next to it (up, down, left, right, but not
diagonally) if it is unoccupied. The space you originally held is still occupied. Thus, you get to create a new
piece in the raided square. Any enemy touching the square you have taken is conquered and that square is
turned to your side (you turn its piece to your side). A Raid can be done even if it will not conquer another
piece. Once you have made this move, your turn is over.
