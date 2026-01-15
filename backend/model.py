from ollama import Client 

client = Client()

messages =[
    {
        'role':'user',
         'content':'Create a resume'
    }
]

for part in client.chat('gpt-oss:120b-cloud', messages=messages, stream=True):
  print(part['message']['content'], end='', flush=True)


