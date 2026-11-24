from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><title>Bot AI Saya</title></head>
<body style="background:#111; color:#fff; font-family:sans-serif; text-align:center; padding-top:50px;">
    <h1>Halo, ini web AI saya</h1>
    <form method="POST">
        <input type="text" name="pesan" placeholder="Tulis pesan..." style="width:300px; padding:10px; border-radius:5px; border:none;">
        <button type="submit" style="padding:10px; border-radius:5px; border:none; background:#00ff00; cursor:pointer;">Kirim</button>
    </form>
    {% if jawaban %}<p style="margin-top:20px;"><b>Jawaban:</b> {{ jawaban }}</p>{% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    jawaban = None
    if request.method == "POST":
        pesan = request.form.get("pesan", "")
        # Nanti di sini kita sambungkan ke API Gemini
        jawaban = f"Kamu bilang: {pesan} (API belum disambungkan)"
    return render_template_string(HTML, jawaban=jawaban)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
