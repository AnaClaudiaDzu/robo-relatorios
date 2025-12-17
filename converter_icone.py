from PIL import Image

img = Image.open("assets/robo.png")
img.save("assets/robo.ico", format="ICO", sizes=[(256, 256)])

print("Ícone .ico criado com sucesso!")
