from collections import defaultdict
import json

import tqdm

from tagging_datasets._datatype import Data

industries_overrepresented =["Business/Finance", "Science/Technology/Medicince", "News/Journalism", "Literary Arts", "Sports", "Visual Arts", "Religion"]

ethnicities_underrepresented = ["Black or African American","Multiracial","North African/Middle Eastern","Asian/Pacific Islander","Hispanic or Latino"]


counts = defaultdict(lambda: defaultdict(int))
count = 0

## GET GENDER
with open("data_overrepresented.jsonl") as f:
        with open("data_overrepresented_historical.jsonl","w") as w:
            for line in f:
                data = Data(json.loads(line))
                if int(data.celebrity.birthdate.year) < 1900:
                    w.write(line)


# from collections import defaultdict
# import json

# from tagging_datasets._datatype import Data

# counts = defaultdict(lambda: defaultdict(int))
# count = 0


# with open("data_underrepresented.jsonl") as f:
#     for i,line in enumerate(f):
#         count+=1
#         datum_obj = Data(json.loads(line))
#         counts["ethnicity"][datum_obj.celebrity.ethnicity] +=1
#         counts["industry"][datum_obj.celebrity.industry] +=1
#         counts["celebrity_gender"][datum_obj.celebrity.gender] +=1
#         counts["relative_gender"][datum_obj.relative.gender] +=1
#         counts["dead"][datum_obj.celebrity.dead] +=1
#         counts["birthdate"][datum_obj.celebrity.birthdate.year] +=1




# for k in counts:
#     print("---------------")
#     print(k)
#     print("---------------")
#     for k2 in counts[k]:
#         print(k2,round(counts[k][k2]/count,ndigits=3))
#     print("---------------")
#     print("---------------")
#     print("---------------")
    




# ---------------
# industry
# ---------------
# Government/Politics 0.112
# Business/Finance 0.038
# Dramatic Arts 0.538
# Musical Arts 0.192
# Science/Technology/Medicince 0.017
# News/Journalism 0.024
# Literary Arts 0.028
# Sports 0.035
# Visual Arts 0.01
# Religion 0.006
# ---------------
# ---------------
# ---------------
# ethnicity
# ---------------
# Black or African American 0.096
# Multiracial 0.029
# White Alone 0.786
# North African/Middle Eastern 0.011
# Asian/Pacific Islander 0.023
# Hispanic or Latino 0.055
# ---------------
# ---------------
# ---------------
# celebrity_gender
# ---------------
# female 0.307
# male 0.689
# genderfluid 0.001
# trans woman 0.002
# non-binary 0.001
# ---------------
# ---------------
# ---------------
# relative_gender
# ---------------
# male 0.475
# female 0.52
# trans woman 0.003
# agender 0.002
# ---------------
# ---------------