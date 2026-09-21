import os
from PIL import Image

pasta_entrada = "amagens"
pasta_saida = "convertidas"

os.makedirs(pasta_entrada, exist_ok=True)

for arquivo in os.listdir(pasta_entrada):
    