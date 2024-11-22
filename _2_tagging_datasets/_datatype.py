import json
from typing import List, Dict, Optional

class Prompts:
    def __init__(self, possessionOSR: str, possessionSRO: str, prepositionORS: str, prepositionRSO: str):
        self.possessionOSR = possessionOSR
        self.possessionSRO = possessionSRO
        self.prepositionORS = prepositionORS
        self.prepositionRSO = prepositionRSO

class Results:
    def __init__(self):
        self.possessionOSR = None
        self.possessionSRO = None
        self.prepositionORS = None
        self.prepositionRSO = None


class PromptCetegories:
    def __init__(self, inRelation: Dict[str, str], outRelation: Dict[str, str]):
        self.inRelation = Prompts(**inRelation)
        self.outRelation = Prompts(**outRelation)

class ResultCategories:
    def __init__(self):
        self.inRelation = Results()
        self.outRelation = Results()

class Date:
    year:str
    day:str
    month:str
    def __init__(self,date):
        date = date[:date.find("T")]
        self.day = date[-2:]
        self.month = date[-5:-3]
        self.year = date[:-6]


class Relative:
    def __init__(self, id:str, name: str,
                 gender: str, acceptable_answers: List[str], multiple_answers: bool,
                 relationship_generic_genderless: str, relationship_generic_gendered: str,
                 relationship_kinship_genderless: str, relationship_kinship_gendered: str,
                 prompts: Dict[str, Dict[str, str]]):
        self.id = id
        self.name = name
        self.gender = gender
        self.acceptable_answers = acceptable_answers
        self.multiple_answers = multiple_answers
        self.relationship_generic_genderless = relationship_generic_genderless
        self.relationship_generic_gendered = relationship_generic_gendered
        self.relationship_kinship_genderless = relationship_kinship_genderless
        self.relationship_kinship_gendered = relationship_kinship_gendered
        self.prompts = PromptCetegories(**prompts)
        self.results = ResultCategories()



class Celebrity:
    def __init__(self, id:str, name: str, industry: Optional[str], dead: bool, fame: float,
                 popularity: float, rank: int, ethnicity: str, birthdate: str,
                 gender: str, acceptable_answers: List[str], multiple_answers: bool,
                 relationship_generic_genderless: str, relationship_generic_gendered: str,
                 relationship_kinship_genderless: str, relationship_kinship_gendered: str,
                 prompts: Dict[str, Dict[str, str]]):
        self.id = id
        self.name = name
        self.industry = industry
        self.dead = dead
        self.fame = fame
        self.popularity = popularity
        self.rank = rank
        self.ethnicity = ethnicity
        self.birthdate = Date(birthdate)
        self.gender = gender
        self.acceptable_answers = acceptable_answers
        self.multiple_answers = multiple_answers
        self.relationship_generic_genderless = relationship_generic_genderless
        self.relationship_generic_gendered = relationship_generic_gendered
        self.relationship_kinship_genderless = relationship_kinship_genderless
        self.relationship_kinship_gendered = relationship_kinship_gendered
        self.prompts = PromptCetegories(**prompts)
        self.results = ResultCategories()


class Data:
    def __init__(self, data: Dict):
        self.id = data["id"]
        # print(f"\r{json.dumps(data)}")
        self.celebrity = Celebrity(**data["celebrity"])
        self.relative = Relative(**data["relative"])

