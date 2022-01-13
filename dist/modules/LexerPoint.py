# LexerPoint Class: Keeps track of the index within Lexer
class LexerPoint:

    # In: Pointer Index, String for the Cell
    def __init__(self, pointer_index, user_command):
        self.pointer_index = pointer_index
        self.user_command = user_command

    # Return a copy of pointer pos
    def lex_point_dupe(self):
        return LexerPoint(self.pointer_index, self.user_command)

    # Iterable: Go to the next pointer index
    def go_next(self):
        self.pointer_index = self.pointer_index + 1
        return self.pointer_index
