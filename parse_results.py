import json
from typing import List

from _6_parse_results._datatype_results import Data


data:List[Data] = []
with open("_3_get_representative_dataset/data.json") as f:
    for datum in json.load(f):
        datum = Data(datum)
        data.append(datum)


def extractAnswer(obj):
      return obj["response"]["body"]["choices"][0]["message"]["content"]

with open("results.jsonl") as f:
    for datum in data:
        for person in [datum.celebrity,datum.relative]:
                for direction in [person.results.inRelation, person.results.outRelation]:
                        direction.prepositionRSO = extractAnswer(json.loads(f.readline().strip()))
                        direction.prepositionORS = extractAnswer(json.loads(f.readline().strip()))
                        direction.possessionSRO = extractAnswer(json.loads(f.readline().strip()))
                        direction.possessionOSR = extractAnswer(json.loads(f.readline().strip()))


with open("dataset_w_results.jsonl","w") as f:
    for datum in data:
         obj = datum.to_dict()
         f.write(json.dumps(obj)+"\n")