from NumToken import Numerical
from ErrorHandler import ErrorHandler
from Reserved import *


# Class Interpreter:
class Interpreter:

    # Visit all the children of given node type
    def check(self, raw_node):
        method_name = "check_%s" % type(raw_node).__name__.lower()
        method = getattr(self, method_name)
        return method(raw_node)

    # Get the value for the numerical given
    def check_numerical(self, primary_number):
        return ErrorHandler().accept(
            Numerical(primary_number.tokenised_int_float.base_val)
        )

    # Step through rules for +/- numericals
    def check_positivenegative(self, primary_number):
        error_track = ErrorHandler()

        # Validity check of primary number whilst traversing
        number = error_track.new_err(self.check(primary_number.tokenised_int_float))
        if error_track.exception:
            return error_track
        error = None

        # Condition: Check if the operator is a -
        if primary_number.var_operator.reserved_tok == subtraction_token:
            # Multiply for negation by -1
            number, error = number.multiplication(Numerical(-1))

        # Condition: If there is an exception return just the erorr, else return the answer
        if error:
            return error_track.throw_exception(error)
        else:
            return error_track.accept(number)

    # Step through the appropriate calculation preformed and return result or error
    def check_calculation(self, node):
        error_track = ErrorHandler()

        # Validity check of primary number whilst traversing
        primary_number = error_track.new_err(self.check(node.var_l))
        if error_track.exception:
            return error_track

        # Validity check of secondary number whilst traversing
        secondary_number = error_track.new_err(self.check(node.var_r))
        if error_track.exception:
            return error_track

        # Attempt calculation and return either the result or the error
        answer, exception = None, None

        # Addition
        if node.var_operator.reserved_tok == addition_token:
            answer, exception = primary_number.addition(secondary_number)

        # Substraction
        elif node.var_operator.reserved_tok == subtraction_token:
            answer, exception = primary_number.subtraction(secondary_number)

        # Multiplication
        elif node.var_operator.reserved_tok == multiplication_token:
            answer, exception = primary_number.multiplication(secondary_number)

        # Division
        elif node.var_operator.reserved_tok == division_token:
            answer, exception = primary_number.division(secondary_number)

        # Condition: If there is an exception return just the error, else return the answer
        if exception:
            return error_track.throw_exception(exception)
        else:
            return error_track.accept(answer)
