import sys

board = sys.stdin.readline()

board = board.replace('XXXX', 'AAAA') # 4개 붙어있으면 AAAA로 
board = board.replace('XX', 'BB') # 2개 붙어있으면 BB로
 
if 'X' in board :
    print(-1)
    
else :
    print(board)
