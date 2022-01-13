# Error Class: Returns Errors with appropriate details
class Error:

    # Take input of error name and info
    def __init__(self, err_type, extra_info):
        self.err_type = err_type
        self.extra_info = extra_info

    # Log function to return a prepared string
    def log(self):
        prepared_string = "%s: %s\n" % (self.err_type, self.extra_info)
        return prepared_string


# Subclass: Invalid Character Error
class InvalidCharacter(Error):
    def __init__(self, extra_info):
        super().__init__('Invalid Character', extra_info)


# Subclass: Invalid Syntax
class InvalidSyntax(Error):
    def __init__(self, extra_info=""):
        super().__init__('Invalid Syntax', extra_info)


# Subclass: Invalid Operation
class InvalidOperation(Error):
    def __init__(self, extra_info):
        super().__init__('Invalid Operation', extra_info)


# Class: Handle answers and errors
class ErrorHandler:
    def __init__(self):
        self.answer = None
        self.exception = None

    # Append the answer to the current value
    def accept(self, value):
        self.answer = value
        return self

    # Append the error to the instance
    def throw_exception(self, error):
        self.exception = error
        return self

    # For passed numericals only
    def new_err(self, raw_answer):
        # Condition: Check if there is an error with passed answer
        if raw_answer.exception:
            self.exception = raw_answer.exception
        return raw_answer.answer
