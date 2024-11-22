from openai import OpenAI
client = OpenAI(api_key=open("openAI.key").read())

batch_input_file = client.files.create(
  file=open("messages.jsonl", "rb"),
  purpose="batch"
)


batch_input_file_id = batch_input_file.id

client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/chat/completions",
    completion_window="24h",
    metadata={
      "description": "Messages for Bias validation"
    }
)