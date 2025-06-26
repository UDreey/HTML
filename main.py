from flask import Flask, render_template, request, send_file
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image
import io
from reportlab.lib.utils import ImageReader
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def convite_poetico_ousado():
    if request.method == "POST":
        resposta = request.form["resposta"].strip().lower()  
        if resposta == "sim":
            mensagem_final = "🎬💋 Sabia que esse seria o final feliz... ou melhor, só o começo."
        elif resposta == "não":
            mensagem_final = f"🎭🖤 Tudo bem. Até os melhores filmes têm cenas cortadas... mas eu sempre gravo as melhores."
        else:
            mensagem_final = "😉 Resposta misteriosa... parece até plot twist. Vou esperar ansioso pela sequência."

        return render_template("index.html",  resposta=resposta, mensagem_final=mensagem_final)

    return render_template("index.html", nome="", resposta="", mensagem_final=None)


@app.route("/gerar-pdf")
def gerar_pdf():
    image_path = "Convite.png"
    image = Image.open(image_path)
    largura, altura = image.size

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=(largura, altura))
    imagem = ImageReader(image_path)
    pdf.drawImage(imagem, 0, 0, width=largura, height=altura)
    pdf.save()
    buffer.seek(0)

    return send_file(
        buffer,
        mimetype="application/pdf",
        download_name="convite_visual.pdf"
    )
if __name__ == "__main__":
    app.run()