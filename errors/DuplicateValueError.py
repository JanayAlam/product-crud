class DuplicateValueError(Exception):

    def __init__(self, msg) -> None:
        """ Default constructor. """
        super().__init__(msg)
        self.message = msg

    def get_message(self) -> str:
        """ returns the error message """
        return self.message
