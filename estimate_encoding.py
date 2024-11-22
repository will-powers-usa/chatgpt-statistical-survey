import json
import tiktoken

from tagging_datasets._datatype import Data

enc = tiktoken.encoding_for_model("gpt-4o-mini")

totalText_in = 0
totalText_out = 0

with open("./data_overrepresented.jsonl") as f:

    for line in f:
        dataobj = Data(json.loads(line))
        sys_instructs = "Answer with only names"
        prompt = dataobj.celebrity.prompts.inRelation.possessionOSR
        answer = dataobj.celebrity.acceptable_answers[0]

        totalText_in +=  len(enc.encode(sys_instructs+prompt))+4
        totalText_out += len(enc.encode(answer))+2



print(totalText_in)
print(totalText_out)
    