from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv() 

def translate_to_inclusive(inputt="Who is the chairman"):
        genai.configure(api_key="AIzaSyDebrPyaBVnyh2oLD7odFjrBKSahQBv-08")
        model = genai.GenerativeModel('gemini-pro')

        defaults = {
        'model': 'models/text-bison-001',
        'temperature': 0.1,
        'candidate_count': 1,
        'top_k': 20,
        'top_p': 0.15,
        'max_output_tokens': 1024,
        'stop_sequences': [],
        'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_TOXICITY","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_VIOLENCE","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_SEXUAL","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_MEDICAL","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_DANGEROUS","threshold":"BLOCK_NONE"}],
        }

        prompt = f""" 
        The following is a description of an event a student wishes to host, 
        The student is hosting an event to help other students with a particular skills. 
        Rewrite this to description to be precise, and formal:
        {{inputt}}
        """
     
        response = model.generate_content(prompt)
        print("Result: " + response.text)
        print("__")
        print(inputt)
        return response.text

