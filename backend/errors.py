from http import HTTPStatus


class AppError(Exception):
    def __init__(self, reason: str, status: HTTPStatus):
        super().__init__(f'[{status}] {reason}')
        self.reason = reason
        self.status = status


class ConflictError(AppError):
    def __init__(self, entity: str):
        super().__init__(f'cannot add {entity}', HTTPStatus.CONFLICT)
        self.entity = entity


class NotFoundError(AppError):
    def __init__(self, entity: str):
        super().__init__(f'cannot find {entity}', HTTPStatus.NOT_FOUND)
        self.entity = entity
