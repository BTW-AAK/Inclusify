from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv() 

def translate_to_inclusive(inputt="Who is the chairman"):
        genai.configure(api_key="AIzaSyDHt49ArGg0gQZWevD3zNzOBQzKtcOTHmM")

        defaults = {
        'model': 'models/text-bison-001',
        'temperature': 0.1,
        'candidate_count': 1,
        'top_k': 40,
        'top_p': 0.95,
        'max_output_tokens': 1024,
        'stop_sequences': [],
        'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_TOXICITY","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_VIOLENCE","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_SEXUAL","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_MEDICAL","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_DANGEROUS","threshold":"BLOCK_NONE"}],
        }

        prompt = f"""You are an inclusive language assistant if the input has non-inclusive language. Replace the specific non-inclusive word with inclusive words. do not change words unless necessary.

        Example Input: Stewardess
        Example Output: Flight Attendant 
        Example Input 2: Blindly following
        Example Output 2: Following aimlessly 
        Example Input 3: chairman
        Example Output 3: chairperson 
        Input is: {inputt}
        Output is: 
        """

        response = genai.generate_text(
        **defaults,
        prompt=prompt
        )
        print(response.result)
        return response.result

