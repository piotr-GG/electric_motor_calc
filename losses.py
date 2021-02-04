from elmag_container import ElectromagContainer


class Losses(ElectromagContainer):
    def __init__(self, order, losses):
        super(Losses, self).__init__(order, losses)

    @property
    def losses(self):
        return self.elmag_qty

    @losses.setter
    def losses(self, array):
        self.elmag_qty = array

    def __add__(self, other):
        if isinstance(self, Losses) and isinstance(other, Losses):
            return super(Losses, self).__add__(other)
        else:
            raise TypeError("Wrong operands type!")

    def __eq__(self, other):
        if isinstance(self, Losses) and isinstance(other, Losses):
            return super(Losses, self).__eq__(other)
        else:
            raise TypeError("Wrong operands type!")


if __name__ == "__main__":
    import numpy as np

    order = np.array([1, 2, 3, 4, 5])
    losses = np.array([4.3, 2.3, 0.3, 0.001, 2e-3])
    loss = Losses(order, losses)
    loss.sort(ascending=True)
    print(loss)

    other_loss = Losses(order, losses)
    print(other_loss)
    print(loss == other_loss)

    loss1 = Losses(order, 3)
