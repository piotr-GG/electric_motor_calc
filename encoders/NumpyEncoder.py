import json
from typing import Any

import numpy as np


class NumpyEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, np.ndarray):
            return o.tolist()
        return json.JSONEncoder.default(self, o)


if __name__ == "__main__":
    test = np.array([[1.2, 1, 55], [2, 5, 2]])
    json_dump = json.dumps(test, cls=NumpyEncoder)
    print(json_dump)
