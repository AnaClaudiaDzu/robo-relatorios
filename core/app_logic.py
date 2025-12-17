from core.relatorio import gerar_pdf
from core.coletor import coletar_dados
from pathlib import Path


def executar_automacao(headless=True):
    yield "🚀 Iniciando automação..."

    yield "🌐 Coletando dados do site..."
    coletar_dados(headless=headless)

    yield "📊 Gerando relatório PDF..."
    caminho_pdf: Path = gerar_pdf()

    yield "✅ Relatório gerado com sucesso!"
    yield caminho_pdf  # 🔥 AQUI está o ponto-chave

    yield "🏁 Processo finalizado."
