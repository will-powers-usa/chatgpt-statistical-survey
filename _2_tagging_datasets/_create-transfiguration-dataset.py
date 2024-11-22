from collections import defaultdict
import json
import random


from _datatype import Data, Prompts

ethnicities = defaultdict(int)


def createExample(prompt,response):
    return json.dumps({"messages": 
            [
                {
                 "role": "user", 
                 "content": prompt
                },
                {
                 "role": "assistant", 
                 "content": response
                }
            ]
            })

# GET Celebrity Status
with open("_3_get_representative_dataset/data.json") as f:
    with open("./transfiguration-prompts-celeb.jsonl","w") as wc:
        with open("./transfiguration-prompts-unknown.jsonl","w") as wu:
            data = [Data(datum) for datum in json.load(f)[:1000]]
            for datum in data:
                id = datum.id
                # unknown best: possession Subject Relation Object
                # celebrity best:  preposition Object Relation Subject

                celeb_choices = [
                    datum.celebrity.prompts.inRelation.possessionOSR,
                    datum.celebrity.prompts.inRelation.possessionSRO,
                    datum.celebrity.prompts.inRelation.prepositionORS,
                    datum.celebrity.prompts.inRelation.prepositionRSO,
                    datum.celebrity.prompts.outRelation.possessionOSR,
                    # datum.celebrity.prompts.outRelation.possessionSRO,
                    datum.celebrity.prompts.outRelation.prepositionORS,
                    datum.celebrity.prompts.outRelation.prepositionRSO,
                ]
            
                celeb_choice = random.choice(celeb_choices)
                wc.write(createExample(celeb_choice,datum.celebrity.prompts.outRelation.possessionSRO)+"\n")

                unknown_choices = [
                    datum.relative.prompts.inRelation.possessionOSR,
                    datum.relative.prompts.inRelation.possessionSRO,
                    datum.relative.prompts.inRelation.prepositionORS,
                    datum.relative.prompts.inRelation.prepositionRSO,
                    datum.relative.prompts.outRelation.possessionOSR,
                    datum.relative.prompts.outRelation.possessionSRO,
                    # datum.relative.prompts.outRelation.prepositionORS,
                    datum.relative.prompts.outRelation.prepositionRSO,
                ]

                unknown_choice = random.choice(unknown_choices)
                wu.write(createExample(unknown_choice,datum.relative.prompts.outRelation.prepositionORS)+"\n")