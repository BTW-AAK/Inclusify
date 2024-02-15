from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv() 

def translate_to_inclusive(inputt="Who is the chairman",tone="Neutral"):
        genai.configure(api_key="AIzaSyDHt49ArGg0gQZWevD3zNzOBQzKtcOTHmM")
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
        Rules:
        1. Replace non-inclusive language with inclusive words.
        2. Do not change words unless necessary.
        3. Keep the output the same if it is already inclusive.
        4. If the input is blank, provide blank output.
        5. Tone should be {tone}

        Examples:
        1. "Stewardess" => "Flight Attendant"
        2. "Blindly following" => "Following aimlessly"
        3. "Chairman" => "Chairperson"
        4. "Lame" => "Unimpressive"
        5. "Manpower" => "Workforce"
        6. "Man up and face the challenge" => "Be resilient and face the challenge"
        7. "Is that the flight attendant?" => "Is that the flight attendant?"
        8. "Stop aimlessly following instructions" => "Stop aimlessly following instructions"
        9. "Don't cry like a girl" => "Express your emotions without conforming to gender stereotypes"
        10. "" => ""
        
        Input is: {inputt}
        Output is: 
        """
     
        response = model.generate_content(prompt)
        print("Result: " + response.text)
        print("__")
        print("Tone: "+ tone)
        return response.text

