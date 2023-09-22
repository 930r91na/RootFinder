"""### Error Handling"""

class CustomError(Exception):
    pass


class InvalidInput(Exception):
    def _init_(self, message="You input a not valid character. Check the instructions of the requested formats"):
        self.message = message
        super().__init__(self.message)

    def _str_(self):
        return f"[Error]: {self.message}"


class NotSolved(Exception):
    def _init_(self,
                 message="The method you choose within the entries you set do not converge to a solution. Try another "
                         "method or different bounds."):
        self.message = message
        super().__init__(self.message)

    def _str_(self):
        return f"[Error]: {self.message}"