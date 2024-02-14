from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv() 

def translate_to_inclusive(inputt="Who is the chairman"):
        genai.configure(api_key="AIzaSyDHt49ArGg0gQZWevD3zNzOBQzKtcOTHmM")

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
        Rules:
        If the input has non-inclusive language. Replace ONLY the non-inclusive word with inclusive words. 
        Do not change words unless necessary.
        You can keep the output the same if it is already inclusive. 
        If blank input, blank output

        Example Input 1: "Stewardess"
        Example Output 1: "Flight Attendant"

        Example Input 2: "Blindly following"
        Example Output 2: "Following aimlessly"

        Example Input 3: "chairman"
        Example Output 3: "chairperson"

        Example Input 4: "Lame"
        Example Output 4: "Unimpressive"

        Example Input 5: "Tomboy"
        Example Output 5: "Has a sporty and adventurous style"

        Example Input 6: "Manpower"
        Example Output 6: "Workforce"

        Example Input 7: "Workaholic"
        Example Output 7: "Very dedicated to his work"

        Example Input 8: "Grandfathered in"
        Example Output 8: "Existing system is maintained"

        Example Input 9: "Man up and face the challenge"
        Example Output 9: "Be resilient and face the challenge"

        Example Input 10: "Retarded"
        Example Output 10: "Not well thought out"

        Example Input 11: "Please call the chairperson"
        Example Output 11: "Please call the chairperson"

        Example Input 12: "Is that the flight attendant?"
        Example Output 12: "Is that the flight attendant?"

        Example Input 13: "Stop aimlessly following instructions"
        Example Output 13: "Stop aimlessly following instructions"

        Example Input 14: ""
        Example Output 14: ""

        Example Input 5: ""
        Example Output 5: ""
        
        Input is: {inputt}
        Output is: 
        """
     
        response = genai.generate_text(
        **defaults,
        prompt=prompt

        )
        print("Result:" + response.result)
        return response.result

