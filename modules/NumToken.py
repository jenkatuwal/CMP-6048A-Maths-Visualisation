from ErrorHandler import *


# Class Numerical: Represents a number and allows operations to be completed to them
class Numerical:

    # Set the instance to represent the given number
    def __init__(self, raw_number):
        self.primary_number = raw_number

    def __str__(self):
        return str(self.primary_number)

    # Takes in second number, adds
    def addition(self, secondary_number):
        return Numerical(self.primary_number + secondary_number.primary_number), None

    # Takes in second number, substracts
    def subtraction(self, secondary_number):
        return Numerical(self.primary_number - secondary_number.primary_number), None

    # Takes in second number, multiplies
    def multiplication(self, secondary_number):
        return Numerical(self.primary_number * secondary_number.primary_number), None

    # Takes in second number, error checks, then divides
    def division(self, secondary_number):
        # Condition: Check if there is a division by Zero error
        if secondary_number.primary_number == 0:
            return None, InvalidOperation(
                'Division by zero'
            )

        # Otherwise: Commence division
        return Numerical(self.primary_number / secondary_number.primary_number), None


# Class Token: Main token class, is a base for each tokenised string
class Token:

    # Take the type of reserved token, the base val, and the start and ending indexes
    def __init__(self, reserved_val, base_val=None, index_start=None, index_end=None):
        self.reserved_tok = reserved_val
        self.base_val = base_val

        # Condition: If the start index is given, copy the start index for both start and end position
        if index_start:
            self.pos_start = index_start.lex_point_dupe()
            self.pos_end = index_start.lex_point_dupe()
            self.pos_end.go_next()

        # Condition: If the end index is given, assign the instance end as given end index
        if index_end:
            self.pos_end = index_end
