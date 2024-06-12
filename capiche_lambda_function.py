# import json
# import logging
# from openai import OpenAI
# # import openai

# def lambda_handler(event, context):
#     try:
#         prompt = "Can you tell me if this translation is correct? " + event['prompt']
#         api_key = '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'
#         if not api_key:
#             raise ValueError("OpenAI API key not found.")
#         client = OpenAI(api_key=api_key)
#         messages = [{"role": "user", "content": prompt}]
#         completion = client.chat.completions.create(model="gpt-4", messages=messages, max_tokens=250)
#         logging.info("Completion completed")
#         response = completion.choices[0].message.content
#         return {"statusCode": 200, "body": json.dumps({"response": response})}
#     except Exception as e:
#         logging.error(f"Error: {str(e)}")
#         return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}
import openai
import json
import datetime

def query_completion(prompt: str, engine: str = 'gpt-3.5-turbo', temperature: float = 0.2, max_tokens: int = 1500, top_p: int = 1, frequency_penalty: float = 0.2, presence_penalty: float = 0) -> object:
    """
    Function for querying GPT-3.5 Turbo.
    """
    estimated_prompt_tokens = int(len(prompt.split()) * 1.6)
    estimated_answer_tokens = 2049 - estimated_prompt_tokens
    response = openai.ChatCompletion.create(
    model=engine,
    messages=[{"role": "user", "content": prompt}],
    temperature=temperature,
    max_tokens=min(4096-estimated_prompt_tokens-150, max_tokens),
    top_p=top_p,
    frequency_penalty=frequency_penalty,
    presence_penalty=presence_penalty
    )
    return response
    
def lambda_handler(event, context):
    '''Provide an event that contains the following keys:
      - prompt: text of an open ai prompt
    '''
    
    openai.api_key = "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"
    
    print("Init:")
    print(datetime.datetime.now())
    print("Event:")
    print(event)

    # body = json.loads(event['body'])
    prompt = "Can you tell me if this translation is correct? " + event['prompt']        
    max_tokens = 1500
    
    response = query_completion(prompt)
    response_text = response['choices'][0]['message']['content'].strip()

    response = {
        "statusCode": 200,
        "headers": {},
        "body": response_text
    }

    return response