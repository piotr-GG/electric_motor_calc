from model.motor_results import MotorResults


class ExcelExport:
    def __init__(self, motor_results: MotorResults, filename: str = ""):
        if not isinstance(motor_results, MotorResults):
            raise TypeError
        if not filename.endswith(".xlsx"):
            filename += ".xlsx"

    @classmethod
    def export_to_xl(cls, motor_results: MotorResults, filename: str = ""):
        if not isinstance(motor_results, MotorResults):
            raise TypeError
        if not filename.endswith(".xlsx"):
            filename += ".xlsx"


