
class Entity:
    def __init__(self,data):
        self.id = data["entity"]["id"]
        self.name = data["entity"]["name"] 
        self.gender = data["entity"]["genderLabel"]
        self.dead = True if "deathdate" in data["entity"] and data["entity"]["deathdate"] != "" else False
        self.foundInWikipedia = data["entity"]["genderLabel"]

class Relationship:
    def __init__(self,data,ended):
        self.relationship_generic = data["relationship_generic"]
        self.relationship_gendered = data["relationship_gendered"]
        self.kinship_generic = data["kinship_generic"]
        self.kinship_gendered = data["kinship_gendered"]
        self.ended = ended


class StatusEntity():
    isLabeled = True
    isInterogative = False
    isPronoun = False 
    
    def __init__(self,e:Entity):
        self.gender = e.gender
        self.id = e.id
        self.name = e.name

    def setLabel(self):
        self.isLabeled = True
        self.isInterogative = False
        self.isPronoun = False 
    
    def setInterogative(self):
        self.isLabeled = False
        self.isInterogative = True
        self.isPronoun = False 

    def setPronoun(self):
        self.isLabeled = False
        self.isInterogative = False
        self.isPronoun = tuple 

    def reset(self):
        self. isLabeled = True
        self.isInterogative = False
        self.isPronoun = False 
        
class StatusRelation():
    isGeneric = True
    isKinship = False
    isGendered = True
    def __init__(self,r:Relationship):
        self.relationship_generic = r.relationship_generic
        self.relationship_gendered = r.relationship_gendered
        self.kinship_generic = r.kinship_generic
        self.kinship_gendered = r.kinship_gendered
        self.ended = r.ended

    def setKinship(self):
        self.isGeneric = False
        self.isKinship = True

    def setGeneric(self):
        self.isGeneric = True
        self.isKinship = False

    def setGendered(self):
        self.isGendered = True
    
    def setGeneric(self):
        self.isGendered = False

    def reset(self):
        self.isGeneric = True
        self.isKinship = False
        self.isGendered = True


class Triple:

    isPossessionSRO = True
    isPossessionOSR = False
    isPrepositionORS = False
    isPrepositionRSO = False
    

    def __init__(self,subject:Entity,relation:Relationship,object:Entity):
        self.subject = StatusEntity(subject)
        self.relation = StatusRelation(relation)
        self.object = StatusEntity(object)


    def setPossessionSRO(self):
        self.isPossessionSRO = True
        self.isPossessionOSR = False
        self.isPrepositionORS = False
        self.isPrepositionRSO = False
    def setPossessionOSR(self):
        self.isPossessionSRO = False
        self.isPossessionOSR = True
        self.isPrepositionORS = False
        self.isPrepositionRSO = False
    def setPrepositionORS(self):
        self.isPossessionSRO = False
        self.isPossessionOSR = False
        self.isPrepositionORS = True
        self.isPrepositionRSO = False
    def setPrepositionRSO(self):
        self.isPossessionSRO = False
        self.isPossessionOSR = False
        self.isPrepositionORS = False
        self.isPrepositionRSO = True

    def reset(self):
        self.setPossessionSRO()
        self.object.reset()
        self.subject.reset()
        self.relation.reset()

    def printText(self,Suffix=""):
        subject = None
        subjectPossessive = None
        if self.isPrepositionORS or self.isPrepositionRSO:
            if self.subject.isLabeled:
                subject = self.subject.name
            if self.subject.isInterogative:
                subject = "whom"
            if self.subject.isPronoun:
                if self.subject.gender == "male":
                    subject = "him"
                elif self.subject.gender == "female":
                    subject = "her"
                else:
                    subject = "them"
        if self.isPossessionSRO or self.isPossessionOSR:
            if self.subject.isLabeled:
                subjectPossessive = self.subject.name+"'s"
            if self.subject.isInterogative:
                subjectPossessive = "whose"
            if self.subject.isPronoun:
                if self.subject.gender == "male":
                    subjectPossessive = "his"
                elif self.subject.gender == "female":
                    subjectPossessive = "her"
                else:
                    subjectPossessive = "their"

        relation = None
        if self.relation.isGeneric and self.relation.isGendered:
            relation = self.relation.relationship_gendered
        if self.relation.isGeneric and not self.relation.isGendered:
            relation = self.relation.relationship_generic
        if self.relation.isKinship and self.relation.isGendered:
            relation = self.relation.kinship_gendered
        if self.relation.isKinship and not self.relation.isGendered:
            relation = self.relation.kinship_generic
        
        
        
        object = None

        if self.object.isLabeled:
                object = self.object.name

        if self.isPossessionSRO or self.isPrepositionRSO:
            if self.object.isInterogative:
                object = "whom"
            if self.object.isPronoun:
                if self.object.gender == "male":
                    object = "him"
                elif self.object.gender == "female":
                    object = "her"
                else:
                    object = "whom"
        if self.isPossessionOSR or self.isPrepositionORS:
            if self.object.isInterogative:
                object = "who"
            if self.object.isPronoun:
                if self.object.gender == "male":
                    object = "he"
                elif self.object.gender == "female":
                    object = "she"
                else:
                    object = "who"

        punctuation = "."
        if self.object.isInterogative or self.subject.isInterogative:
            punctuation = "?"

        def CapitalizeStart(string:str):
            letter = string[0].upper()
            string = letter + string[1:]
            return string
        
        instanceTense = "is"
        if self.relation.ended:
            instanceTense = "was"


        Suffix = Suffix+" " if Suffix else ""

        if self.isPossessionSRO:
            return CapitalizeStart(f"{Suffix}{subjectPossessive} {relation} {instanceTense} {object}{punctuation}") #APOSTROPHE/possessive pronoun
        
        if self.isPossessionOSR:
            return CapitalizeStart(f"{Suffix}{object} {instanceTense} {subjectPossessive} {relation}{punctuation}") #APOSTROPHE/possessive pronoun

        if self.isPrepositionORS:
            return CapitalizeStart(f"{Suffix}{object} {instanceTense} the {relation} of {subject}{punctuation}") #Preposition
        
        if self.isPrepositionRSO:
            return CapitalizeStart(f"{Suffix}the {relation} of {subject} {instanceTense} {object}{punctuation}") #Preposition


class Relative():
    def __init__(self,data,primary:Entity):
        self.name = data["entity"]["title"] if "title" in data["entity"] else data["entity"]["name"]
        self.gender = data["entity"]["genderLabel"]
        self.id = data["entity"]["id"]
        self.dead = True if "deathdate" in data["entity"] and data["entity"]["deathdate"] != "" else False
        ended = False
        if "endTime" in data and data["endTime"] != "":
            ended = True
        if primary.dead or self.dead:
            ended = True
        self.triple = Triple(primary,Relationship(data['relationship'],ended=ended),self)
        self.inverse_triple= Triple(self,Relationship(data['inverse_relationship'],ended=ended),primary)
        self.fame = float(data["entity"]["fame"]) if "fame" in data["entity"] else None
        self.rank =  int(data["entity"]["rank"]) if "rank" in data["entity"] else None
        self.birthDate = data["entity"]["birthdate"] if "birthdate" in data["entity"] else None
        self.ethnicity = data["entity"]["ethnicity"] if "ethnicity" in data["entity"] else None
        self.industry = data["entity"]["industry"] if "industry" in data["entity"] else None
        self.relationshipFoundInWikipedia = data["found"] if "found" in data else False
        self.multipleOutCelebrity = data["multipleOutCelebrity"]
        self.multipleInCelebrity = data["multipleInCelebrity"]
        self.multipleOutUnknown = False
        self.multipleInUnknown = False
        self.nameVariations = data["entity"]["nameVariations"]

    def reset(self):
        self.triple.reset()
        self.inverse_triple.reset()

class DataEntity(Entity):
    def __init__(self,data):
        self.gender = data["entity"]["genderLabel"]
        self.name = data["entity"]["title"] if "title" in data["entity"] else data["entity"]["name"]
        self.id = data["entity"]["id"]
        self.dead = True if "deathdate" in data["entity"] and data["entity"]["deathdate"] != "" else False
        self.relatives = list(map(lambda e: Relative(e,self),data["relations"]))
        self.fame = float(data["entity"]["fame"]) if "fame" in data["entity"] else None
        self.rank =  int(data["entity"]["rank"]) if "rank" in data["entity"] else None
        self.nameVariations = data["entity"]["nameVariations"]

       # self.relatives = list(map(lambda r: {"relative":r,"triple":Triple(self,r.relationship,r),"inverse_triple":Triple(r,r.inverse_relationship,self)},relatives))
