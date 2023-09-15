import openai

#GPTに送信するメッセージです。自由にいじってください！
message_to_gpt = f"""
Give me an interesting random fact in one sentence.
"""

message = [{"role": "user", "content": message_to_gpt}]

def gpt_commit_message_generation():
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-0301",
        messages = message
    )
    return response.choices[0].message.content
