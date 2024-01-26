from openai import OpenAI

client = OpenAI(
    api_key=open("chatKEY.txt","r").read().strip('\n'),
    )


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Say Hello World"}],
    #stream=True,
)

print(completion)

#for chunk in stream:
#    if chunk.choices[0].delta.content is not None:
#        print(chunk.choices[0].delta.content, end="\n")
#        out = open("output.txt","a")
      

