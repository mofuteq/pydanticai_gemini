# %%
import os
import google.generativeai as genai
from dotenv import load_dotenv

# .env読み込み
load_dotenv()
# API Key
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
 
gemini_pro = genai.GenerativeModel("gemini-1.5-flash")
prompt = "Hello!"
response = gemini_pro.generate_content(prompt)
print(response.text)
