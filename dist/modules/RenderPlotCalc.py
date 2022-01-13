# Start of imports
from Parser import *
from Interpreter import *


# End of imports

# Feed the input through the LP
def math_lang_process(raw_input):
    # Remove all the whitespaces
    raw_input = raw_input.replace(" ", "")

    # Tuple unpacking for fetching token with an error
    sanitised_tokens, thrown_exception = Lexer(raw_input).tokeniser()

    # Condition: If there is an exception then
    if thrown_exception:
        return None, thrown_exception

    # Generate tree
    syntax_tree = Parser(sanitised_tokens).execute()

    # Condition: check errors for parsing
    if syntax_tree.error:
        return None, syntax_tree.error

    # Pseudo-Condition: Passed all error checks - returns result
    program_feedback = Interpreter().check(syntax_tree.node)

    return program_feedback.answer, program_feedback.exception
