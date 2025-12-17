from pathlib import Path
import pandas as pd


def coletar_dados(headless=True):
    """
    Simula a coleta de dados do SauceDemo.
    Em um cenário real, aqui entraria Selenium ou Playwright.
    """

    pasta_dados = Path.home() / "Documentos" / "Robo de Relatorios" / "dados"
    pasta_dados.mkdir(parents=True, exist_ok=True)

    dados = [
        {"produto": "Sauce Labs Backpack", "preco": 29.99},
        {"produto": "Sauce Labs Bike Light", "preco": 9.99},
        {"produto": "Sauce Labs Bolt T-Shirt", "preco": 15.99},
        {"produto": "Sauce Labs Fleece Jacket", "preco": 49.99},
    ]

    df = pd.DataFrame(dados)
    df.to_csv(pasta_dados / "produtos.csv", index=False)
