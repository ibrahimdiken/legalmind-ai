import os, json
from datetime import datetime
import openai
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Log dosyasının yolu
LOG_PATH = os.path.join(os.getcwd(), "logs", "mcp_history.json")

mcp_bp = Blueprint("mcp", __name__)

def handle_mcp_request(data):
    user_id = data.get("user_id", "anonim")
    context = data.get("context", "")
    prompt  = data.get("prompt",  "")

    if not prompt:
        return {"error": "Prompt eksik."}

    full_prompt = f"Kullanıcı: {user_id}\nKontekst: {context}\nSoru: {prompt}"

    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen uzman bir hukuki danışmansın."},
                {"role": "user",   "content": full_prompt}
            ],
            temperature=0.3,
            max_tokens=400
        )
        answer = resp.choices[0].message["content"].strip()
        result = {
            "timestamp": datetime.now().isoformat(),
            "user_id":   user_id,
            "context":   context,
            "prompt":    prompt,
            "answer":    answer
        }
        # Loglama
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(result, ensure_ascii=False) + "\n")
        return result

    except Exception as e:
        return {"error": str(e)}

@mcp_bp.route("/", methods=["POST"])
def mcp_endpoint():
    data = request.get_json(force=True)
    result = handle_mcp_request(data)
    status = 200 if "answer" in result else 400
    return jsonify(result), status
