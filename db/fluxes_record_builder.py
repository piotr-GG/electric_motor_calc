import itertools
import numpy as np
from db.record_builder_interface import RecordBuilderInterface
from model.flux_density import FluxDensity


class FluxesRecordBuilder(RecordBuilderInterface):

    @staticmethod
    def build_record(data: FluxDensity, id: int):
        if isinstance(data, FluxDensity):
            order, flux_val = data.to_list()
            return zip(order, flux_val, itertools.repeat(id))

    @staticmethod
    def parse_record(input_data):
        unzipped_data = list(zip(*input_data))
        order_new = np.array(unzipped_data[1], dtype="int32")
        value_new = np.array(unzipped_data[2], dtype="float64")
        return FluxDensity(order_new, value_new)
