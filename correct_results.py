import json
from typing import List
from _datatype_w_results import Data


def gradeResponse(resp,acceptable_answers):
    for ans in acceptable_answers:
        if ans in resp:
            return "True"
        else:
            return "False"
        

data:List[Data] = []

with open("./dataset_w_results.jsonl") as f:
    for line in f:
        datum = Data(json.loads(line.strip()))
        for person,acceptable_answers in [(datum.celebrity, datum.celebrity.acceptable_answers),(datum.relative, datum.relative.acceptable_answers)]:
                for direction_results, direction_grades in [(person.results.inRelation, person.grades.inRelation), (person.results.outRelation, person.grades.outRelation)]:
                    direction_grades.prepositionRSO = gradeResponse(direction_results.prepositionRSO,acceptable_answers)
                    direction_grades.prepositionORS = gradeResponse(direction_results.prepositionORS,acceptable_answers)
                    direction_grades.possessionSRO = gradeResponse(direction_results.possessionSRO,acceptable_answers)
                    direction_grades.possessionOSR = gradeResponse(direction_results.possessionOSR,acceptable_answers)
        data.append(datum)

with open("dataset_w_grades.jsonl","w") as w:
     for datum in data:
          w.write(json.dumps(datum.to_dict())+'\n')


            

