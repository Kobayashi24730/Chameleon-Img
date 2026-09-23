import os
from PIL import Image

pasta_entrada = "imagens"
pasta_saida = "convertidas"

os.makedirs(pasta_entrada, exist_ok=True)

for arquivo in os.listdir(pasta_entrada):
    if arquivo.lower().endswith((".jpg", ".jpeg", ".webp", ".png")): 
        caminho_arquivo = os.path.join(pasta_entrada, arquivo)
        imagem = Image.open(caminho_arquivo)
        nome_base = os.path.splitext(arquivo)[0]
        novo_caminho = os.path.join(pasta_saida, f"{nome_base}.png")
        imagem.save(novo_caminho)
        print(f"Imagem {arquivo} convertida para {novo_caminho}")