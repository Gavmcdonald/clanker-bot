import os 
from dotenv import load_dotenv
from google import genai



def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key == None:
        raise RuntimeError("Gemini API missing")
    
    client = genai.Client(api_key=api_key)
    content = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    print(client.models.generate_content(model="gemini-2.5-flash",contents=content).text)



if __name__ == "__main__":
    main()
