from dotenv import load_dotenv
import google.generativeai as genai
import json
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


def analysis(inputt="Who is the chairman"):
        genai.configure(api_key="AIzaSyDHt49ArGg0gQZWevD3zNzOBQzKtcOTHmM")
        model = genai.GenerativeModel('gemini-pro')

        defaults = {
        'model': 'models/text-bison-001',
        'temperature': 0.3,
        'candidate_count': 1,
        'top_k': 20,
        'top_p': 0.15,
        'max_output_tokens': 1024,
        'stop_sequences': [],
        'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_TOXICITY","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_VIOLENCE","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_SEXUAL","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_MEDICAL","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_DANGEROUS","threshold":"BLOCK_NONE"}],
        }

        prompt = f""" 
        Rules:
       Rules:
        1. Analyze the non-inclusive language input in JSON format as seen in example.
		3. Output in 
		2. There are 3 parameters 
		TypeNL = type of noninclusive language (Gendered, Disability, Age, None)
		UsedN = the noninclusive language word used  
		UsedI = Any inclusive language  
		Note: If the following are not found replace with "None"
		

        Examples:
        1. "Please call the chairman" => 
		"TypeNL": "Gendered",
  		"UsedN": "chairman",
  		"UsedI": "None"

		2. "Man up and face the challenge" =>
		"TypeNL": "Gendered",
		"UsedN": "Man up",
		"UsedI": "Courageously"

		3. "Please call the chairperson" =>

		"TypeNL": "None",
		"UsedN": "None",
		"UsedI": "chairperson"

		4. "Stop blindly following instructions"
		"TypeNL": "Disability",
		"UsedN": "blindly",
		"UsedI": "None"

        Input is: {inputt}
        """
     
        response = model.generate_content(prompt)
        print("Result: " + response.text)
        json_analysis = json.loads(response.text)
        print(json_analysis)
        
        return json_analysis


# The input 

# Print the resulting JSON object

