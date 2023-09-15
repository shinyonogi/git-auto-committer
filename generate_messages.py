import openai

def commit_message_generation():
    content = f"""
    Give me an interesting random fact in one sentence.
    """
    message = [{"role": "user", "content": content}]

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-0301",
        messages = message
    )
    return response.choices[0].message.content
