class NotFoundError(Exception):
    def __init__(self, resource: str, id: int):
        self.message = f"{resource} {id} not found"
        super().__init__(self.message)


class ValidationError(Exception):
    def __init__(self, message: str = "title cannot be empty"):
        self.message = message
        super().__init__(self.message)
