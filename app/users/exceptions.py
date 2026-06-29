class UserException(Exception):
    pass


class EmailAlreadyExists(UserException):
    pass


class UsernameAlreadyExists(UserException):
    pass


class UserNotFound(UserException):
    pass