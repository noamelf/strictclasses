def strict(cls):
    def validate(self):
        for attr, _type in self.__annotations__.items():
            assert isinstance(getattr(self, attr), _type), f'{attr} is not an instance of {_type}'

    cls.validate = validate
    return cls
