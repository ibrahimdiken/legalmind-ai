import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def process_input(prompt: str) -> str:
    """
    Kullanıcının prompt'unu OpenAI'a gönderir ve cevabı döner.
    """
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen deneyimli bir hukuki danışmansın."},
                {"role": "user",   "content": prompt}
            ],
            temperature=0.3,
            max_tokens=400
        )
        return resp.choices[0].message["content"].strip()
    except Exception as e:
        return f"Hata oluştu: {e}"
