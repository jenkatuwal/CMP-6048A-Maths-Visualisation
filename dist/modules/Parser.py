from Lexer import *
from Nodes import *


# Parser Class: Takes in list of Tokenised items, preforms operation calls, iterates
class Parser:
    def __init__(self, token_list):
        self.current_token = None
        self.token_list = token_list
        self.token_index = -1
        self.go_next()

    # Appends token if index is within range of token list
    def go_next(self):
        self.token_index += 1
        if self.token_index < len(self.token_list):
            self.current_token = self.token_list[self.token_index]
        return self.current_token

    def execute(self):
        output = self.statement()
        if not output.error and self.current_token.reserved_tok != end_token:
            return output.negative(InvalidSyntax(
                "Operator missing"
            ))

        return output

    # Search for Integer/Float and return Numerical node of appropriate token
    def numerical(self):

        # Create a new validate instance to pass results to
        validator = Validate()
        token = self.current_token

        # Condition: +/- is matched
        if token.reserved_tok in (addition_token, subtraction_token):

            validator.start_validate(self.go_next())
            factor = validator.start_validate(self.numerical())

            # Condition: An error is found
            if validator.error:
                return validator

            # After checks, return the +/- tokenised number
            return validator.positive(PositiveNegative(token, factor))

        # Condition: Check token is Integer or Float
        elif token.reserved_tok in (integer_token, float_token):
            validator.start_validate(self.go_next())
            return validator.positive(Numerical(token))

        # Condition: Check for '(' match and continue till ')'
        elif token.reserved_tok == left_bracket_token:
            validator.start_validate(self.go_next())
            expression = validator.start_validate(self.statement())

            # Condition: An error is found
            if validator.error:
                return validator

            # Condition: check for ')' match
            if self.current_token.reserved_tok == right_bracket_token:
                validator.start_validate(self.go_next())
                return validator.positive(expression)
            else:
                return validator.negative(InvalidSyntax(
                    "Expected ')'"
                ))

        return validator.negative(InvalidSyntax(
            "Expected int or float"
        ))

    # Shared function: takes in operator keep checking for numerical operation
    def solve_token(self, solve_type_func, operators):

        validator = Validate()
        left = validator.start_validate(solve_type_func())

        if validator.error:
            return validator

        while self.current_token.reserved_tok in operators:

            op_tok = self.current_token
            validator.start_validate(self.go_next())
            right = validator.start_validate(solve_type_func())

            if validator.error:
                return validator

            left = Calculation(left, op_tok, right)

        return validator.positive(left)

    # Solve type functions below

    # Recursively attempts to solve (Mul/Div/Numerical)
    def expression(self):
        return self.solve_token(
            self.numerical, (multiplication_token, division_token)
        )

    # Recursively attempts to solve (Add/Sub/Expr)
    def statement(self):
        return self.solve_token(
            self.expression, (addition_token, subtraction_token)
        )


# Class ParseValidate: Is the main return class for each statement, acts as a bridge error handler
class Validate:

    # Define the error value and placeholder node value
    def __init__(self):
        self.error = None
        self.node = None

    # Takes in a Validate Instance or a Node
    def start_validate(self, validate_token):

        # Condition: Check if instance its own class
        if isinstance(validate_token, Validate):

            # Condition: Pass through the error value
            if validate_token.error:
                self.error = validate_token.error
            return validate_token.node

        # Returns error-exempt node
        return validate_token

    # Append the given node to own instance and return
    def positive(self, node):
        self.node = node
        return self

    # Append error instead of instance when error occours and return
    def negative(self, error):
        self.error = error
        return self
