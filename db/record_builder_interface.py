from model.elmag_container import ElectromagContainer


class RecordBuilderInterface:

    @staticmethod
    def build_record(data: ElectromagContainer, id: int):
        pass

    @staticmethod
    def parse_record(input_data):
        pass
