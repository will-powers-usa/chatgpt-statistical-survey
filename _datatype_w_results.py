import json
from typing import List, Dict, Optional

class Prompts:
    def __init__(self, possessionOSR: str, possessionSRO: str, prepositionORS: str, prepositionRSO: str):
        self.possessionOSR = possessionOSR
        self.possessionSRO = possessionSRO
        self.prepositionORS = prepositionORS
        self.prepositionRSO = prepositionRSO

    def to_dict(self):
        return self.__dict__

class Results:
    def __init__(self, possessionOSR: str, possessionSRO: str, prepositionORS: str, prepositionRSO: str):
        self.possessionOSR = possessionOSR
        self.possessionSRO = possessionSRO
        self.prepositionORS = prepositionORS
        self.prepositionRSO = prepositionRSO

    def to_dict(self):
        return self.__dict__
    
class Grades:
    def __init__(self):
        self.possessionOSR = None
        self.possessionSRO = None
        self.prepositionORS = None
        self.prepositionRSO = None

    def to_dict(self):
        return self.__dict__



class PromptCategories:
    def __init__(self, inRelation: Dict[str, str], outRelation: Dict[str, str]):
        self.inRelation = Prompts(**inRelation)
        self.outRelation = Prompts(**outRelation)

    def to_dict(self):
        return {
            "inRelation": self.inRelation.to_dict(),
            "outRelation": self.outRelation.to_dict()
        }

class ResultCategories:
    def __init__(self, inRelation: Dict[str, str], outRelation: Dict[str, str]):
        self.inRelation = Prompts(**inRelation)
        self.outRelation = Prompts(**outRelation)

    def to_dict(self):
        return {
            "inRelation": self.inRelation.to_dict(),
            "outRelation": self.outRelation.to_dict()
        }

class GradeCategories:

    def __init__(self, ):
        self.inRelation = Grades()
        self.outRelation = Grades()

    def to_dict(self):
        return {
            "inRelation": self.inRelation.to_dict(),
            "outRelation": self.outRelation.to_dict()
        }


class Date:
    def __init__(self, day,month,year):
        self.day = day
        self.month = month
        self.year = year

    def to_dict(self):
        return self.__dict__

class Relative:
    def __init__(self, id: str, name: str,
                 gender: str, acceptable_answers: List[str], multiple_answers: bool,
                 relationship_generic_genderless: str, relationship_generic_gendered: str,
                 relationship_kinship_genderless: str, relationship_kinship_gendered: str,
                 prompts: Dict[str, Dict[str, str]],results: Dict[str, Dict[str, str]]):
        self.id = id
        self.name = name
        self.gender = gender
        self.acceptable_answers = acceptable_answers
        self.multiple_answers = multiple_answers
        self.relationship_generic_genderless = relationship_generic_genderless
        self.relationship_generic_gendered = relationship_generic_gendered
        self.relationship_kinship_genderless = relationship_kinship_genderless
        self.relationship_kinship_gendered = relationship_kinship_gendered
        self.prompts = PromptCategories(**prompts)
        self.results = ResultCategories(**results)
        self.grades = GradeCategories()


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "acceptable_answers": self.acceptable_answers,
            "multiple_answers": self.multiple_answers,
            "relationship_generic_genderless": self.relationship_generic_genderless,
            "relationship_generic_gendered": self.relationship_generic_gendered,
            "relationship_kinship_genderless": self.relationship_kinship_genderless,
            "relationship_kinship_gendered": self.relationship_kinship_gendered,
            "prompts": self.prompts.to_dict(),
            "results": self.results.to_dict(),
            "grades": self.grades.to_dict()
        }

class Celebrity:
    def __init__(self, id: str, name: str, industry: Optional[str], dead: bool, fame: float,
                 popularity: float, rank: int, ethnicity: str, birthdate: str,
                 gender: str, acceptable_answers: List[str], multiple_answers: bool,
                 relationship_generic_genderless: str, relationship_generic_gendered: str,
                 relationship_kinship_genderless: str, relationship_kinship_gendered: str,
                 prompts: Dict[str, Dict[str, str]],results: Dict[str, Dict[str, str]]):
        self.id = id
        self.name = name
        self.industry = industry
        self.dead = dead
        self.fame = fame
        self.popularity = popularity
        self.rank = rank
        self.ethnicity = ethnicity
        self.birthdate = Date(**birthdate)
        self.gender = gender
        self.acceptable_answers = acceptable_answers
        self.multiple_answers = multiple_answers
        self.relationship_generic_genderless = relationship_generic_genderless
        self.relationship_generic_gendered = relationship_generic_gendered
        self.relationship_kinship_genderless = relationship_kinship_genderless
        self.relationship_kinship_gendered = relationship_kinship_gendered
        self.prompts = PromptCategories(**prompts)
        self.results = ResultCategories(**results)
        self.grades = GradeCategories()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "industry": self.industry,
            "dead": self.dead,
            "fame": self.fame,
            "popularity": self.popularity,
            "rank": self.rank,
            "ethnicity": self.ethnicity,
            "birthdate": self.birthdate.to_dict(),
            "gender": self.gender,
            "acceptable_answers": self.acceptable_answers,
            "multiple_answers": self.multiple_answers,
            "relationship_generic_genderless": self.relationship_generic_genderless,
            "relationship_generic_gendered": self.relationship_generic_gendered,
            "relationship_kinship_genderless": self.relationship_kinship_genderless,
            "relationship_kinship_gendered": self.relationship_kinship_gendered,
            "prompts": self.prompts.to_dict(),
            "results": self.results.to_dict(),
            "grades": self.grades.to_dict()
        }

class Data:
    def __init__(self, data: Dict):
        self.id = data["id"]
        self.celebrity = Celebrity(**data["celebrity"])
        self.relative = Relative(**data["relative"])

    def to_dict(self):
        return {
            "id": self.id,
            "celebrity": self.celebrity.to_dict(),
            "relative": self.relative.to_dict()
        }