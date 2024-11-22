from collections import defaultdict
from helper import create_question, loadUnknownEntities
import json

from datatypes import DataEntity, Relative
from helper import markDuplicates

unkownEntities, unkownEntitiesDict = loadUnknownEntities()


newUnkownEntitiesDict =defaultdict(lambda: defaultdict(lambda:defaultdict(dict)))

data = []

for uE in unkownEntities:
    markDuplicates(uE.relatives,kinship=True,gendered=True)
sumOfFames = sum([sum([k.fame for k in uk.relatives]) for uk in unkownEntities])

for uE in unkownEntities:
    
    for rE in uE.relatives:

        removedGenericRelations = ["spouse","unmarried partner"]
        if rE.inverse_triple.relation.relationship_generic in removedGenericRelations or rE.triple.relation.relationship_generic in removedGenericRelations:
            continue

        info = {}
        data.append(info)

        info["id"] =  rE.id+uE.id

        celebrity = {}
        info["celebrity"] = celebrity
        info["id"] = rE.id
        celebrity["id"] = rE.id
        celebrity["name"] = rE.name
        celebrity["industry"] = rE.industry
        celebrity["dead"] = rE.dead
        celebrity["fame"] = rE.fame
        celebrity["popularity"] = rE.fame/sumOfFames
        celebrity["rank"] = rE.rank
        celebrity["ethnicity"] = rE.ethnicity
        celebrity["birthdate"] = rE.birthDate
        celebrity["industry"] = rE.industry
        celebrity["gender"] = rE.gender
        celebrity["acceptable_answers"] = rE.nameVariations
        celebrity["multiple_answers"] = rE.multipleOutUnknown
        celebrity["relationship_generic_genderless"] = rE.triple.relation.relationship_generic
        celebrity["relationship_generic_gendered"] = rE.triple.relation.relationship_gendered
        celebrity["relationship_kinship_genderless"] = rE.triple.relation.kinship_generic
        celebrity["relationship_kinship_gendered"] = rE.triple.relation.kinship_gendered


        relative = {}
        info["relative"] = relative
        relative["name"] = uE.name
        relative["id"] = uE.id
        relative["gender"] = uE.gender
        relative["acceptable_answers"] = uE.nameVariations
        relative["multiple_answers"] = rE.multipleOutCelebrity
        relative["relationship_generic_genderless"] = rE.inverse_triple.relation.relationship_generic
        relative["relationship_generic_gendered"] = rE.inverse_triple.relation.relationship_gendered
        relative["relationship_kinship_genderless"] = rE.inverse_triple.relation.kinship_generic
        relative["relationship_kinship_gendered"] = rE.inverse_triple.relation.kinship_gendered


        for query in ["celebrity","relative"]:
            obj = celebrity if query == "celebrity" else relative
            prompts = obj["prompts"] = {"inRelation":{},"outRelation":{}}
            for direction in ["direct","inverse"]:
                label = "inRelation"
                if  (query == "celebrity" and direction == "direct") or (query == "relative" and direction == "inverse"):
                    label = "outRelation"
                for grammar in ["possessionOSR","possessionSRO","prepositionORS","prepositionRSO"]:
                    question = create_question(rE,query,direction,grammar)
                    prompts[label][grammar] = question



with open(f"data.json","w") as w:
    json.dump(data,w)

