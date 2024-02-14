from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv() 

def translate_to_inclusive(inputt="Who is the chairman"):
        genai.configure(api_key="AIzaSyDHt49ArGg0gQZWevD3zNzOBQzKtcOTHmM")

        generation_config = {
        "temperature": 0.5,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
        }

        safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        ]


        model = genai.GenerativeModel(model_name="gemini-pro",
                                    generation_config=generation_config,
                                    safety_settings=safety_settings)


        prompt_parts = [
        "If the input has non-inclusive language. Replace ONLY the non-inclusive word with inclusive words. If already inclusive dont change it.",
        "input: Please call the chairman",
        "output: Please call the chairperson",
        "output 2: Gender",
        "input: Is that the stewardess?",
        "output: Is that the flight attendant?",
        "output 2: Gender",
        "input: Stop blindly following instructions",
        "output: Stop aimlessly following instructions",
        "output 2: Disability",
        "input: The team needs a new secretary",
        "output: The team needs a new administrative assistant",
        "output 2: Gender",
        "input: That's so lame",
        "output: That's so unimpressive",
        "output 2: Disability",
        "input: She's such a tomboy",
        "output: She has a sporty and adventurous style",
        "output 2: Gender",
        "input: The company needs more manpower",
        "output: The company needs more workforce",
        "output 2: Gender",
        "input: He's a workaholic",
        "output: He's very dedicated to his work",
        "output 2: Disability",
        "input: The old system is grandfathered in",
        "output: The existing system is maintained",
        "output 2: Age",
        "input: Man up and face the challenge",
        "output: Be resilient and face the challenge",
        "output 2: Gender",
        "input: That's retarded",
        "output: That's not well thought out",
        "output 2: Disability",
        "input: Please call the chairperson",
        "output: Please call the chairperson",
        "output 2: None",
        "input: Is that the flight attendant?",
        "output: Is that the flight attendant?",
        "output 2: None",
        "input: Stop aimlessly following instructions",
        "output: Stop aimlessly following instructions",
        "output 2: None",
        "input: ",
        "output: ",
        "output 2: None",
        "input: "+ {inputt},
        "output: ",
        ]
     
        response = model.generate_content(prompt_parts)

        print("Result:" + response.result)
        return response.result

