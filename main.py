# first OpenAPI request
import os
from dotenv import load_dotenv
import openai


# os.getenv('api_key')
load_dotenv()
api_key = os.getenv('API_KEY')


# api key
openai.api_key = api_key

# create a request to complete the answer
response = openai.Completion.create(
    model='text-davinci-003',
    prompt='Who is the Prime Minister of Bangladesh?'
)

print(response)
