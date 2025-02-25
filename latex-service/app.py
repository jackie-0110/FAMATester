from flask import Flask, request, send_file
import subprocess

app = Flask(__name__)

@app.route("/generate-pdf", methods=["POST"])
def generate_pdf():
    latex = request.json.get("latex")
    with open("template.tex", "w") as f:
        f.write(latex)
    subprocess.run(["pdflatex", "template.tex"], check=True)
    return send_file("template.pdf")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)