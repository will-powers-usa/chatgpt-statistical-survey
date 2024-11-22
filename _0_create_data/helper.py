
from collections import defaultdict
import json
from datatypes import DataEntity, Relative


def markDuplicates(relatives:list[Relative],kinship=True,gendered=True):
        uniqueRelationshipsDirect = defaultdict(list)
        uniqueRelationshipsInverse = defaultdict(list)
        for relative in relatives:
            rid = relative.id
            r = None
            ir = None
            if kinship and gendered:
                r = relative.inverse_triple.relation.kinship_gendered
                ir = relative.triple.relation.kinship_gendered
            if kinship and not gendered:
                r = relative.inverse_triple.relation.kinship_generic
                ir = relative.triple.relation.kinship_generic
            if not kinship and gendered:
                r = relative.inverse_triple.relation.relationship_gendered
                ir = relative.triple.relation.relationship_gendered
            if not kinship and not gendered:
                r = relative.inverse_triple.relation.relationship_generic
                ir = relative.triple.relation.relationship_generic

            uniqueRelationshipsDirect[r].append(rid)
            uniqueRelationshipsInverse[ir].append(rid)

        multipleOutUnknownSet = set()
        multipleInUnknownSet = set()
        # print(len(uniqueRelationshipsDirect))
        # print(len(uniqueRelationshipsInverse))
        for k in uniqueRelationshipsDirect:
            if len(uniqueRelationshipsDirect[k]) > 1:
                # multipleOutUnkown = False
                multipleOutUnknownSet.update(uniqueRelationshipsDirect[k])
        for k in uniqueRelationshipsInverse:
            if len(uniqueRelationshipsInverse[k]) > 1:
                # multipleOutUnkown = False
                multipleInUnknownSet.update(uniqueRelationshipsInverse[k])


        for relative in relatives:
            rid = relative.id
            relative.multipleOutUnknown = rid in multipleOutUnknownSet
            relative.multipleInUnknown = rid in multipleInUnknownSet




def loadUnknownEntities():
    unkownEntitiesDict = dict()
    unkownEntities = []
    with open("./create-data/found-unkown-entities-full.json") as r:
        unkownEntities = list(map(lambda e:DataEntity(e),list(json.load(r).values())))
        for unkownEntity in unkownEntities:
            unkownEntitiesDict[unkownEntity.id] = unkownEntity
    for uE in unkownEntities:
        markDuplicates(uE.relatives,kinship=True,gendered=True)
    return unkownEntities,unkownEntitiesDict

    

def create_question(relationshipEntity,query_Entity, relationship_direction,grammar):
    relationshipEntity.reset()

    triple = None
    inverse_triple = None

    if relationship_direction == "inverse":
        triple = relationshipEntity.triple
        inverse_triple = relationshipEntity.inverse_triple
    elif relationship_direction == "direct":
        triple = relationshipEntity.inverse_triple
        inverse_triple = relationshipEntity.triple

    triple.relation.setGendered()
    triple.relation.setKinship()
    inverse_triple.relation.setGendered()
    inverse_triple.relation.setKinship()


    tripleSetStructure = None

    if grammar == "possessionOSR":
        tripleSetStructure = triple.setPossessionOSR
    if grammar == "possessionSRO":
        tripleSetStructure = triple.setPossessionSRO
    if grammar == "prepositionORS":
        tripleSetStructure = triple.setPrepositionORS
    if grammar == "prepositionRSO":
        tripleSetStructure = triple.setPrepositionRSO

    unnamed = None

    if query_Entity == "celebrity":
        if  relationship_direction == "inverse":
            unnamed = triple.object
        if relationship_direction == "direct":
            unnamed = triple.subject
    if query_Entity == "relative":
        if  relationship_direction == "inverse":
            unnamed = triple.subject
        if relationship_direction == "direct":
            unnamed = triple.object

    tripleSetStructure()
    unnamed.setInterogative()

    return triple.printText()
