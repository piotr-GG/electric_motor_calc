from model.losses import Losses
import numpy as np
import itertools
from db.record_builder_interface import RecordBuilderInterface


class LossesRecordBuilder(RecordBuilderInterface):

    @staticmethod
    def build_record(loss: Losses, id: int):
        if isinstance(loss, Losses):
            order, loss_val = loss.to_list()
            return zip(order, loss_val, itertools.repeat(id))

    @staticmethod
    def parse_record(input_data):
        unzipped_data = list(zip(*input_data))
        order_new = np.array(unzipped_data[1], dtype="int32")
        value_new = np.array(unzipped_data[2], dtype="float64")
        return Losses(order_new, value_new)
