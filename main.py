from motor_calc import MotorCalc
from motor import Motor
from motor_results import MotorResults

if __name__ == "__main__":
    test_motor = Motor()
    limit = 5
    motor_calc = MotorCalc(test_motor, limit=0, kls=10, klr=10, gs=10, gr=10)
    motor_calc.calculate()
    motor_results = MotorResults(motor_calc)
    print(motor_results)


