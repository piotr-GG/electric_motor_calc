from model.motor import Motor
from model.motor_calc import MotorCalc
import matplotlib.pyplot as plt


class CalculateMatplotlib:
    def __init__(self, limit_lower, limit_upper, motor):
        if isinstance(limit_lower, (int, float)) and isinstance(limit_upper, (int, float)):
            if limit_lower >= 0:
                if int(limit_lower) < int(limit_upper):
                    self.limit_lower = limit_lower
                    self.limit_upper = limit_upper
                else:
                    raise ValueError("Limit lower is greater than limit upper!")
        else:
            raise ValueError("Limit lower is less than 0!")

        if isinstance(motor, Motor):
            self.motor = motor
        else:
            raise TypeError("Wrong type for motor argument")

        self.__Ps = list()
        self.__PAl = list()
        self.__Pss = list()
        self.__Pp = list()
        self.__limits = list()
        self.fig = None

    @property
    def limit_lower(self):
        return self.__limit_lower

    @limit_lower.setter
    def limit_lower(self, value):
        if value > 0:
            self.__limit_lower = int(value)

    @property
    def limit_upper(self):
        return self.__limit_upper

    @limit_upper.setter
    def limit_upper(self, value):
        self.__limit_upper = int(value)

    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self, value):
        self.__motor = value

    def calculate_losses(self):
        step_count = 10
        step_val = int((self.limit_upper - self.limit_lower)/step_count)
        for i in range(self.limit_lower, self.limit_upper + 1, step_val):
            motor_calc = MotorCalc(self.motor, limit=i)
            motor_calc.calculate()
            Ps, PAl, Pss, Pp = motor_calc.get_motor_losses()

            self.__Ps.append(Ps)
            self.__PAl.append(PAl)
            self.__Pss.append(Pss)
            self.__Pp.append(Pp)
            self.__limits.append(i)
        print(self.__limits)

    def plot_losses(self):
        self.fig, self.ax = plt.subplots()
        self.ax.plot(self.__limits, self.__Ps, label="Ps")
        self.ax.plot(self.__limits, self.__PAl, label="PAl")
        self.ax.plot(self.__limits, self.__Pss, label="Pss")
        self.ax.plot(self.__limits, self.__Pp, label="Pp")
        self.ax.set_xlabel("Zakres harmonicznych")
        self.ax.set_ylabel("Straty")
        self.ax.set_title("Straty dodatkowe silnika")
        self.ax.legend()
        plt.show()


if __name__ == "__main__":
    test_motor = Motor()
    t = CalculateMatplotlib(1, 100, test_motor)
    t.calculate_losses()
    t.plot_losses()



