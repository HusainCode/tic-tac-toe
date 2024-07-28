class Player:
    def __init__(self, player_score, symbol, turn):
        self.player_score = player_score
        self.symbol = None
        self.turn = False
        
    def make_move(self, board):
        pass
    
    def get_symbol(self):
        return self.symbol
    
    def get_score(self):
        return self.player_score
    
    def get_turn(self):
        return self.turn
    
        

