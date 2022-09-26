from dataclasses import dataclass


def choose_one_operation() -> int:
    result = True
    while result:
        entry_op = input('Choose an option: ')
        op_obj = TreatInputs(entry_op)
        if not op_obj.treat_input_choose():
            print('Indicate an option')
        else:
            return int(entry_op)


def inform_id() -> list:
    ids = input('Give id(s) for selected operation (id1, id2, etc.):')
    id_obj = TreatInputs(ids)
    result = id_obj.treat_input_id()
    return result


@dataclass
class TreatInputs:
    id: str

    def treat_input_id(self) -> list:
        result = self.id.split(',')
        result = [_id.strip().upper() for _id in result if _id != '']

        return result

    def treat_input_choose(self) -> int:
        if self.id.isnumeric():
            if 2 >= int(self.id) >= 1:
                return True
        return False
