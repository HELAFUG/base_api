class GreatHelper:
    def __init__(self, name: str, default: str):
        self.name = name
        self.default = default

    def as_dict(self):
        return {"name": self.name, "default": self.default}
