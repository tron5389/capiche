from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="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",
)

def query_gpt(prompt, model_name="linguist_helper"):
    # openai.api_key = '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'
    # openai.api_key = "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"
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        max_tokens=500
    )
    return response.choices[0].message.content

def main():
    user_input = input("Enter your prompt: ")
    response = query_gpt(user_input)
    print("Response from GPT:", response)

if __name__ == "__main__":
    main()
