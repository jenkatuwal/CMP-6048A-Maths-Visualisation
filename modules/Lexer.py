# Start of Imports
from LexerPoint import *
from NumToken import *
from ErrorHandler import *
from Reserved import *


# End of Imports


# Lexer Class: Checks the syntax of user input to check if it is valid or not
class Lexer:

    # Receive the user input upon class instantiation
    def __init__(self, raw_user_input):

        # Setup class variables and pass function
        self.raw_user_input = raw_user_input
        self.main_index = None

        # Get the new pointer index
        self.pointer_index = LexerPoint(-1, raw_user_input)

        # Iterate forwards
        self.go_next()

    # Iterable method to push pointer
    def go_next(self):

        self.pointer_index.go_next()

        if self.pointer_index.pointer_index < len(self.raw_user_input):
            self.main_index = self.raw_user_input[self.pointer_index.pointer_index]

        else:
            self.main_index = None

    # Iterate through the input and generate tokens depending on user input
    def tokeniser(self):

        # Placeholder list to append tokens to
        prepared_list = []

        # Iterate through the given ruleset for the
        while self.main_index is not None:

            # Ruleset: Addition
            if self.main_index == "+":
                prepared_list.append(Token(addition_token, index_start=self.pointer_index))
                self.go_next()

            # Ruleset: Subtract
            elif self.main_index == "-":
                prepared_list.append(Token(subtraction_token, index_start=self.pointer_index))
                self.go_next()

            # Ruleset: Multiply
            elif self.main_index == "*":
                prepared_list.append(Token(multiplication_token, index_start=self.pointer_index))
                self.go_next()

            # Ruleset: Divide
            elif self.main_index == "/":
                prepared_list.append(Token(division_token, index_start=self.pointer_index))
                self.go_next()

            # Ruleset: Open Bracket
            elif self.main_index == "(":
                prepared_list.append(Token(left_bracket_token, index_start=self.pointer_index))
                self.go_next()

            # Ruleset: Close Bracket
            elif self.main_index == ")":
                prepared_list.append(Token(right_bracket_token, index_start=self.pointer_index))
                self.go_next()

            # Ruleset: Create Int/Float
            elif self.main_index in numerical_values:
                prepared_list.append(self.make_number())

            # Ruleset: Ignore whitespaces
            elif self.main_index in " \t":
                self.go_next()

            # Ruleset: Character not found
            else:
                char = self.main_index
                self.go_next()

                # Return an Error
                return [], InvalidCharacter(
                    "'" + char + "'"
                )

        prepared_list.append(Token(end_token, index_start=self.pointer_index))
        return prepared_list, None

    # Assign a number either as a float or as an integer
    def make_number(self):

        # Temporary variable holders
        temporary_number = ""
        decimal_places = 0
        pos_start = self.pointer_index.lex_point_dupe()

        # Loop when a number is found
        while (self.main_index is not None) and (self.main_index in numerical_values + "."):

            # Condition: Check if there is a proceeding decimal point
            if self.main_index == ".":

                # Condition: Check
                if decimal_places == 1:
                    break

                # Increment the decimal place values
                decimal_places = decimal_places + 1
                temporary_number = temporary_number + ""

            # If there is no decimal point add number onto the main list
            else:

                temporary_number = temporary_number + self.main_index

            # Iterate
            self.go_next()

        # Condition: If there are no decimal places then create an integer, otherwise a float
        if decimal_places == 0:

            # Return a class with, the token, the number the start of the number and the index it ended on
            return Token(
                integer_token, int(temporary_number), pos_start, self.pointer_index
            )
        else:
            # Return a class with, the token, the number the start of the number and the index it ended on
            return Token(
                float_token, float(temporary_number), pos_start, self.pointer_index
            )