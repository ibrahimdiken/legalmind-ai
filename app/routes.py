from flask import Blueprint, render_template, request, jsonify, send_file
import os
import json
from app.mcp.server import handle_mcp_request

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    """
    Anasayfa: Form üzerinden user_id, context, prompt alır,
    MCP handler’a gönderir ve sonucu render eder.
    """
    answer = None
    user_id = request.form.get("user_id", "")
    context = request.form.get("context", "")
    prompt  = request.form.get("prompt", "")

    if request.method == "POST" and prompt:
        result = handle_mcp_request({
            "user_id": user_id,
            "context": context,
            "prompt": prompt
        })
        answer = result.get("answer") or result.get("error")

    return render_template(
        "index.html",
        answer=answer,
        user_id=user_id,
        context=context,
        prompt=prompt
    )

@main.route("/mcp", methods=["POST"])
def mcp_route():
    """
    API endpoint: JSON olarak user_id, context, prompt alır,
    MCP handler ile işleyip JSON cevap döner.
    """
    data = request.get_json(force=True)
    result = handle_mcp_request(data)
    status = 200 if "answer" in result else 400
    return jsonify(result), status

@main.route("/history", methods=["GET"])
def view_history():
    """
    Geçmiş MCP sorgularını logs/mcp_history.json dosyasından okur,
    context ve tarih filtreleri uygular ve history.html ile gösterir.
    """
    log_file = os.path.join(os.getcwd(), "logs", "mcp_history.json")
    entries = []
    if os.path.exists(log_file):
        with open(log_file, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    continue

    # Filtre parametreleri
    context_filter = request.args.get("context", "").lower()
    start_date    = request.args.get("start_date")
    end_date      = request.args.get("end_date")

    def in_date_range(ts):
        date_str = ts.split("T")[0]
        if start_date and date_str < start_date:
            return False
        if end_date and date_str > end_date:
            return False
        return True

    filtered = []
    for e in entries:
        if context_filter and context_filter not in e.get("context", "").lower():
            continue
        if not in_date_range(e.get("timestamp", "")):
            continue
        filtered.append(e)

    return render_template("history.html", entries=filtered)

@main.route("/download_logs", methods=["GET"])
def download_logs():
    """
    MCP log dosyasını JSON olarak indirir.
    """
    path = os.path.join(os.getcwd(), "logs", "mcp_history.json")
    return send_file(path, mimetype="application/json")
