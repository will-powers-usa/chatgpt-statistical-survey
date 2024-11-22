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



## GET GENDER known 
with open("data.json") as f:
    with open("tagging-datasets/gender-known-prompts.jsonl","w") as w:
        data = [Data(datum) for datum in json.load(f)[:1000]]
        for datum in data:
            id = datum.id
            gender_c = datum.celebrity.gender
            gender_r = datum.relative.gender

            
            dir = random.choice([datum.celebrity.prompts.inRelation, datum.celebrity.prompts.outRelation])
            p = random.choice([dir.possessionOSR,dir.possessionSRO,dir.prepositionORS,dir.prepositionRSO])
            w.write(createExample(p,gender_r)+"\n")


            dir = random.choice([datum.relative.prompts.inRelation, datum.relative.prompts.outRelation])
            p =  random.choice([dir.possessionOSR,dir.possessionSRO,dir.prepositionORS,dir.prepositionRSO])
            w.write(createExample(p,gender_c)+"\n")


## GET GENDER unknown
with open("data.json") as f:
    with open("tagging-datasets/gender-unknown-prompts.jsonl","w") as w:
        data = [Data(datum) for datum in json.load(f)[:1000]]
        for datum in data:
            id = datum.id
            gender_c = datum.celebrity.gender
            gender_r = datum.relative.gender
        
            dir = random.choice([datum.celebrity.prompts.inRelation, datum.celebrity.prompts.outRelation])
            p = random.choice([dir.possessionOSR,dir.possessionSRO,dir.prepositionORS,dir.prepositionRSO])
            w.write(createExample(p,gender_c)+"\n")

            dir = random.choice([datum.relative.prompts.inRelation, datum.relative.prompts.outRelation])
            p =  random.choice([dir.possessionOSR,dir.possessionSRO,dir.prepositionORS,dir.prepositionRSO])
            w.write(createExample(p,gender_r)+"\n")



# # GET BIRTHYEAR
# with open("data.json") as f:
#     with open("tagging-datasets/birthyear-prompts.jsonl","w") as w:
#         w.write(f"id\tyear\tis_present\tprompt\n")
#         data = [Data(datum) for datum in json.load(f)[:1000]]
#         for datum in data:
#             id = datum.id
#             year = datum.celebrity.birthdate.year
        
#             for dir in [datum.celebrity.prompts.inRelation, datum.celebrity.prompts.outRelation]:
#                 for p in [dir.possessionOSR,dir.possessionSRO,dir.prepositionORS,dir.prepositionRSO]:
#                     w.write(f"{id}\t{year}\t{False}\t{p}\n")
#                     w.write(createExample(p,year)+"\n")


#             for dir in [datum.relative.prompts.inRelation, datum.relative.prompts.outRelation]:
#                 for p in [dir.possessionOSR,dir.possessionSRO,dir.prepositionORS,dir.prepositionRSO]:
#                     w.write(f"{id}\t{year}\t{True}\t{p}\n")
#                     w.write(createExample(p,year)+"\n")



# GET INDUSTRY
with open("data.json") as f:
    with open("tagging-datasets/industry-prompts.jsonl","w") as w:
        data = [Data(datum) for datum in json.load(f)[:1000]]
        for datum in data:
            id = datum.id
            industry = datum.celebrity.industry
        
            dir = random.choice([datum.celebrity.prompts.inRelation, datum.celebrity.prompts.outRelation])
            p = random.choice([dir.possessionOSR,dir.possessionSRO,dir.prepositionORS,dir.prepositionRSO])
            w.write(createExample(p,industry)+"\n")

            dir = random.choice([datum.relative.prompts.inRelation, datum.relative.prompts.outRelation])
            p =  random.choice([dir.possessionOSR,dir.possessionSRO,dir.prepositionORS,dir.prepositionRSO])
            w.write(createExample(p,industry)+"\n")



# GET DIRECTION
with open("data.json") as f:
    with open("tagging-datasets/direction-prompts.jsonl","w") as w:
        data = [Data(datum) for datum in json.load(f)[:1000]]
        for datum in data:
            id = datum.id
            for person in [datum.celebrity, datum.relative]:

                dir = person.prompts.inRelation
                p = random.choice([dir.possessionOSR,dir.possessionSRO,dir.prepositionORS,dir.prepositionRSO])
                w.write(createExample(p,"inbound relationship")+"\n")

                dir = person.prompts.outRelation
                p =  random.choice([dir.possessionOSR,dir.possessionSRO,dir.prepositionORS,dir.prepositionRSO])
                w.write(createExample(p,"outbound relationship")+"\n")


# GET GRAMMAR
with open("data.json") as f:
    with open("tagging-datasets/grammar-prompts.jsonl","w") as w:
        data = [Data(datum) for datum in json.load(f)[:1000]]
        for datum in data:
            id = datum.id

            for person in [datum.celebrity, datum.relative]:
                for dir in [person.prompts.inRelation, person.prompts.outRelation]:
                    dir: Prompts
                    prompt = random.choice([0,1,2,3])
                    if prompt == 0:
                        w.write(createExample(dir.possessionOSR,"possession Object Subject Relation")+"\n")
                    if prompt == 1:
                        w.write(createExample(dir.possessionSRO,"possession Subject Relation Object")+"\n")
                    if prompt == 2:
                        w.write(createExample(dir.prepositionORS,"preposition Object Relation Subject")+"\n")
                    if prompt == 3:
                        w.write(createExample(dir.prepositionRSO,"preposition Relation Subject Object")+"\n")



# GET ETHNICITY
with open("data.json") as f:
    with open("tagging-datasets/ethnicity-prompts.jsonl","w") as w:
        data = [Data(datum) for datum in json.load(f)[:1000]]
        for datum in data:
            id = datum.id
            ethnicity = datum.celebrity.ethnicity
        
            dir = random.choice([datum.celebrity.prompts.inRelation, datum.celebrity.prompts.outRelation])
            p = random.choice([dir.possessionOSR,dir.possessionSRO,dir.prepositionORS,dir.prepositionRSO])
            w.write(createExample(p,ethnicity)+"\n")


            dir = random.choice([datum.relative.prompts.inRelation, datum.relative.prompts.outRelation])
            p =  random.choice([dir.possessionOSR,dir.possessionSRO,dir.prepositionORS,dir.prepositionRSO])
            w.write(createExample(p,ethnicity)+"\n")


# GET Celebrity Status
with open("data.json") as f:
    with open("tagging-datasets/known-prompts.jsonl","w") as w:
        data = [Data(datum) for datum in json.load(f)[:1000]]
        for datum in data:
            id = datum.id
        
            dir = random.choice([datum.celebrity.prompts.inRelation, datum.celebrity.prompts.outRelation])
            p = random.choice([dir.possessionOSR,dir.possessionSRO,dir.prepositionORS,dir.prepositionRSO])
            w.write(createExample(p,"unknown")+"\n")

            dir = random.choice([datum.relative.prompts.inRelation, datum.relative.prompts.outRelation])
            p =  random.choice([dir.possessionOSR,dir.possessionSRO,dir.prepositionORS,dir.prepositionRSO])
            w.write(createExample(p,"celebrity")+"\n")