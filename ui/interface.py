import sys
import os
from pathlib import Path
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QTextEdit, QLabel, QCheckBox
)
from PyQt5.QtCore import QThread, pyqtSignal


# =========================
# Thread de trabalho
# =========================

class WorkerThread(QThread):
    update = pyqtSignal(str)
    finished = pyqtSignal(Path)

    def __init__(self, headless=True):
        super().__init__()
        self.headless = headless
        self.pdf_path = None

    def run(self):
        from core.app_logic import executar_automacao

        for msg in executar_automacao(headless=self.headless):
            if isinstance(msg, Path):
                self.pdf_path = msg
            else:
                self.update.emit(msg)

        self.finished.emit(self.pdf_path)


# =========================
# Interface
# =========================

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Robô de Relatórios - SauceDemo")
        self.resize(700, 500)

        layout = QVBoxLayout(self)

        self.label = QLabel("Status: parado")
        layout.addWidget(self.label)

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        layout.addWidget(self.log)

        self.headless_cb = QCheckBox("Rodar headless (sem abrir navegador)")
        self.headless_cb.setChecked(True)
        layout.addWidget(self.headless_cb)

        self.btn = QPushButton("Iniciar Automação")
        self.btn.clicked.connect(self.iniciar)
        layout.addWidget(self.btn)

        self.btn_abrir = QPushButton("📂 Abrir pasta do relatório")
        self.btn_abrir.setEnabled(False)
        self.btn_abrir.clicked.connect(self.abrir_pasta)
        layout.addWidget(self.btn_abrir)

    def iniciar(self):
        self.log.clear()
        self.btn.setEnabled(False)
        self.btn_abrir.setEnabled(False)
        self.label.setText("Status: executando...")

        self.thread = WorkerThread(headless=self.headless_cb.isChecked())
        self.thread.update.connect(self.adicionar_log)
        self.thread.finished.connect(self.finalizar)
        self.thread.start()

    def adicionar_log(self, texto):
        self.log.append(texto)

    def finalizar(self, pdf_path):
        self.label.setText("Status: concluído")
        self.btn.setEnabled(True)

        if pdf_path:
            self.log.append(f"\n📄 Relatório salvo em:\n{pdf_path}")
            self.btn_abrir.setEnabled(True)

    def abrir_pasta(self):
        pasta = Path.home() / "Documentos" / "Robo de Relatorios" / "relatorios"
        os.system(f'xdg-open "{pasta}"')


# =========================
# Start
# =========================

def iniciar_gui():
    app = QApplication(sys.argv)
    janela = App()
    janela.show()
    sys.exit(app.exec_())
