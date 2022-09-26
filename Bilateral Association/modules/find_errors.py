
class ValidateInput:
    @staticmethod
    def type_person(parameter, class_) -> bool:
        from .person import Person
        if isinstance(class_, Person):
            return True
        else:
            RaiseError.raise_error(parameter, "Person")

    @staticmethod
    def type_local(parameter, class_) -> bool:
        from .house import House
        if isinstance(class_, House):
            return True
        else:
            RaiseError.raise_error(parameter, "House")


class RaiseError:
    @staticmethod
    def raise_error(parameter, class_):
        raise TypeError(f'Parameter "{parameter}" must be instance of class "{class_}".')
