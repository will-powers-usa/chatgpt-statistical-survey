from collections import defaultdict
import json

import tqdm

from _2_tagging_datasets._datatype import Data

count = 0


#### SPLIT DATASETS INTO


with open("dataset.jsonl") as f:
        with open("data_overrepresented_historical.jsonl","w") as w:
            for line in f:
                data = Data(json.loads(line))
                if int(data.celebrity.birthdate.year) < 1900:
                    w.write(line)

