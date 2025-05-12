from dotenv import load_dotenv
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from google import genai

def selecionar_arquivo():
    caminho_inicial='~/Área de trabalho'
    caminho_arquivo = filedialog.askopenfile(title='Selecione uma imagem', initialdir=caminho_inicial,filetypes=[('image files', '.png'), ('image files', '.jpg')])
    return caminho_arquivo.name

load_dotenv()
gemini_api = os.getenv("GEMINI_API")
janela = tk.Tk()
janela.withdraw()

img_path = selecionar_arquivo()
img=Image.open(img_path)

client = genai.Client(api_key=gemini_api)

prompt = "Descreva, com o máximo de detalhes possível, a imagem anexada. Limite sua resposta com o máximo de 200 tokens."
response = client.models.generate_content(
    model="gemini-2.5-pro-exp-03-25",
    contents=[prompt, img]
)

print(response.text)
