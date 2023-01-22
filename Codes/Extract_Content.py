import openai

openai.api_key = "API Key"

model_engine = "text-davinci-003"
prompt = "tell me 100 gk questions"

class process:
    def extract_content():
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
    
        response = completion.choices[0].text
        print(response)

        text_file = open(f"../Contents/content_{prompt}.txt", "w")
        n = text_file.write(response)
        #print(str(n))
        text_file.close()

content = process.extract_content()
