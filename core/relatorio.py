import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from pathlib import Path


# =========================
# Pastas do usuário
# =========================

def pasta_base():
    home = Path.home()
    base = home / "Documentos" / "Robo de Relatorios"
    base.mkdir(parents=True, exist_ok=True)
    return base


def pasta_dados():
    p = pasta_base() / "dados"
    p.mkdir(exist_ok=True)
    return p


def pasta_relatorios():
    p = pasta_base() / "relatorios"
    p.mkdir(exist_ok=True)
    return p


# =========================
# Gráfico
# =========================

def gerar_grafico(df):
    caminho_img = pasta_dados() / "grafico.png"

    plt.figure(figsize=(8, 4.5))
    plt.bar(df['produto'], df['preco'])
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Preço (USD)')
    plt.tight_layout()
    plt.savefig(caminho_img)
    plt.close()

    return caminho_img


# =========================
# PDF
# =========================

def gerar_pdf(caminho_csv=None):
    if caminho_csv is None:
        caminho_csv = pasta_dados() / "produtos.csv"

    df = pd.read_csv(caminho_csv)

    img = gerar_grafico(df)

    saida_pdf = pasta_relatorios() / "relatorio_saucedemo.pdf"

    doc = SimpleDocTemplate(str(saida_pdf), pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Relatório de Produtos - SauceDemo", styles['Title']))
    story.append(Spacer(1, 12))

    story.append(Paragraph(f"Produtos coletados: {len(df)}", styles['Normal']))
    story.append(Spacer(1, 12))

    dados_tabela = [df.columns.tolist()] + df.values.tolist()
    tabela = Table(dados_tabela, hAlign='LEFT')
    tabela.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4b6eaf')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    story.append(tabela)
    story.append(Spacer(1, 12))
    story.append(Image(str(img), width=450, height=280))

    doc.build(story)

    return saida_pdf
