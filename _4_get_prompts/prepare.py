
import json
from _2_tagging_datasets._datatype import Data


def getData(index, userMessage,systemMessage=None):

    messages = []

    if systemMessage != None:
        messages.append({"role": "system", "content": systemMessage})
    
    messages.append({"role": "user", "content": userMessage})

    return {
        "custom_id": str(index), 
        "method": "POST", 
        "url": "/v1/chat/completions", 
        "body": {
            "model": "gpt-4o-mini", 
            "messages": messages,
            "max_tokens": 1000,
            "temperature": 0.0,
    }
}

count = 0

with open("_3_get_representative_dataset/data.json") as f:
    with open("messages.jsonl","w") as w:
        dataset = json.load(f)
        for datum in dataset:
            data = Data(datum)
            for person in [data.celebrity,data.relative]:
                for direction in [person.prompts.inRelation, person.prompts.outRelation]:
                    for grammar in [direction.prepositionRSO,direction.prepositionORS,direction.possessionSRO,direction.possessionOSR]:
                        w.write(json.dumps(getData(count, grammar,"Answer with only names"))+"\n")
                        count+=1
        
