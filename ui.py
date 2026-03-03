import platform

from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QMessageBox,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class SecurityTool(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RAVENGUARD - System Security")
        self.setFixedSize(950, 500)
        self.setMinimumSize(900, 450)

        self.COLORS = {
            "pink": "#FF1493",
            "dark_pink": "#C71585",
            "light_pink": "#FF69B4",
            "bg": "#0A0A0A",
            "text": "#FFFFFF",
            "border": "#FF1493",
        }

        self.setStyleSheet(f"""
            QWidget {{
                background-color: {self.COLORS['bg']};
                color: {self.COLORS['text']};
                font-family: 'Segoe UI', 'Arial', sans-serif;
            }}
            QPushButton {{
                border: none;
                font-size: 12px;
                font-weight: 600;
                border-radius: 6px;
                background-color: transparent;
                color: white;
            }}
            QFrame#main_container {{
                background-color: transparent;
                border: 2px solid {self.COLORS['border']};
                border-radius: 20px;
                margin: 5px;
            }}
            QFrame#header {{
                background-color: transparent;
                padding: 5px 15px;
            }}
            QFrame#tool_card {{
                background-color: transparent;
                border: 1px solid {self.COLORS['border']};
                border-radius: 12px;
                padding: 15px;
            }}
            QFrame#tool_card:hover {{
                border: 2px solid {self.COLORS['light_pink']};
            }}
            QLabel#main_title {{
                font-size: 28px;
                font-weight: 800;
                color: {self.COLORS['pink']};
                letter-spacing: 1px;
                background-color: transparent;
            }}
            QLabel#subtitle {{
                font-size: 13px;
                color: {self.COLORS['light_pink']};
                font-weight: 500;
                letter-spacing: 0.5px;
                margin: 5px 0 15px 0;
                background-color: transparent;
            }}
            QLabel#tool_title {{
                font-size: 20px;
                font-weight: 700;
                color: white;
                background-color: transparent;
            }}
            QLabel#tool_subtitle {{
                font-size: 12px;
                color: {self.COLORS['light_pink']};
                font-weight: 400;
                margin-bottom: 8px;
                background-color: transparent;
            }}
            QLabel#tool_description {{
                font-size: 11px;
                color: #AAAAAA;
                line-height: 1.4;
                background-color: transparent;
            }}
            QLabel#version {{
                font-size: 11px;
                color: #666666;
                background-color: transparent;
            }}
        """)

        # Layout principal
        main_container = QFrame()
        main_container.setObjectName("main_container")
        main_layout = QVBoxLayout(main_container)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Header com botão X
        header = self.create_header()
        main_layout.addWidget(header)

        # Área de conteúdo
        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: transparent;")
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(20, 10, 20, 15)
        content_layout.setSpacing(15)

        # Subtítulo
        subtitle = QLabel("SISTEMA DE SEGURANÇA E REPARO DO WINDOWS")
        subtitle.setObjectName("subtitle")
        subtitle.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(subtitle)

        # Container das ferramentas em linha
        tools_layout = QHBoxLayout()
        tools_layout.setSpacing(15)

        # Ravenguard Card
        ravenguard_card = self.create_tool_card(
            "🛡️",
            "RAVENGUARD",
            "Malicious Software Removal Tool",
            [
                "• Remoção de malware avançado",
                "• Verificação de rootkits",
                "• Base de dados atualizada"
            ],
            "INICIAR",
            self.run_ravenguard
        )
        tools_layout.addWidget(ravenguard_card)

        # SFC Card
        sfc_card = self.create_tool_card(
            "🔍",
            "SFC SCAN",
            "System File Checker",
            [
                "• Verificação de arquivos do sistema",
                "• Reparo automático",
                "• Proteção de DLLs"
            ],
            "INICIAR",
            self.run_sfc
        )
        tools_layout.addWidget(sfc_card)

        # DISM Card
        dism_card = self.create_tool_card(
            "⚙️",
            "DISM REPAIR",
            "Deployment Image Servicing",
            [
                "• Reparo da imagem do Windows",
                "• Correção de componentes",
                "• Restauração da saúde"
            ],
            "INICIAR",
            self.run_dism
        )
        tools_layout.addWidget(dism_card)

        content_layout.addLayout(tools_layout)

        # Espaço flexível
        content_layout.addStretch()

        main_layout.addWidget(content_widget)

        # Layout final
        window_layout = QVBoxLayout(self)
        window_layout.setContentsMargins(10, 10, 10, 10)
        window_layout.addWidget(main_container)

    def create_header(self):
        header = QFrame()
        header.setObjectName("header")
        header.setFixedHeight(40)
        header.setStyleSheet("background-color: transparent;")
        
        layout = QHBoxLayout(header)
        layout.setContentsMargins(10, 0, 10, 0)
        
        # Título e versão
        title_layout = QHBoxLayout()
        title_layout.setSpacing(8)
        
        main_title = QLabel("RAVENGUARD")
        main_title.setObjectName("main_title")
        main_title.setStyleSheet("font-size: 22px; background-color: transparent;")
        
        version_label = QLabel("v2.0")
        version_label.setObjectName("version")
        version_label.setStyleSheet("color: #666666; padding-top: 3px; background-color: transparent;")
        
        title_layout.addWidget(main_title)
        title_layout.addWidget(version_label)
        
        # Botão X para sair (rosa)
        exit_btn = QPushButton("✕")
        exit_btn.setFixedSize(30, 30)
        exit_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: transparent;
                color: {self.COLORS['pink']};
                font-size: 18px;
                font-weight: bold;
                border: 2px solid {self.COLORS['pink']};
                border-radius: 15px;
            }}
            QPushButton:hover {{
                background-color: {self.COLORS['pink']};
                color: white;
            }}
        """)
        exit_btn.setCursor(Qt.PointingHandCursor)
        exit_btn.clicked.connect(self.confirm_exit)
        
        layout.addLayout(title_layout)
        layout.addStretch()
        layout.addWidget(exit_btn)
        
        return header

    def create_tool_card(self, icon, title, subtitle, features, button_text, callback):
        card = QFrame()
        card.setObjectName("tool_card")
        card.setFixedSize(270, 230)
        card.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(card)
        layout.setSpacing(8)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # Header do card com ícone e título
        header_layout = QHBoxLayout()
        header_layout.setSpacing(8)
        
        icon_label = QLabel(icon)
        icon_label.setStyleSheet("font-size: 24px; background-color: transparent;")
        
        title_label = QLabel(title)
        title_label.setObjectName("tool_title")
        title_label.setStyleSheet("font-size: 18px; background-color: transparent;")
        
        header_layout.addWidget(icon_label)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        # Subtítulo
        subtitle_label = QLabel(subtitle)
        subtitle_label.setObjectName("tool_subtitle")
        subtitle_label.setStyleSheet("background-color: transparent;")
        
        # Features
        features_text = "\n".join(features)
        features_label = QLabel(features_text)
        features_label.setObjectName("tool_description")
        features_label.setWordWrap(True)
        features_label.setStyleSheet("background-color: transparent;")
        
        # Botão sem fundo
        btn = QPushButton(f"{button_text}")
        btn.setStyleSheet(f"""
            QPushButton {{
                color: {self.COLORS['pink']};
                font-weight: bold;
                padding: 6px;
                font-size: 12px;
                border: 1px solid {self.COLORS['pink']};
                border-radius: 4px;
                margin-top: 5px;
                background-color: transparent;
            }}
            QPushButton:hover {{
                background-color: {self.COLORS['pink']};
                color: white;
            }}
        """)
        btn.setCursor(Qt.PointingHandCursor)
        btn.clicked.connect(callback)
        
        layout.addLayout(header_layout)
        layout.addWidget(subtitle_label)
        layout.addWidget(features_label)
        layout.addStretch()
        layout.addWidget(btn)
        
        return card

    def run_ravenguard(self):
        import logic
        logic.run_ravenguard()

    def run_sfc(self):
        import logic
        logic.run_sfc()

    def run_dism(self):
        import logic
        logic.run_dism()

    def confirm_exit(self):
        reply = QMessageBox.question(
            self,
            "Sair",
            "Deseja realmente sair do RAVENGUARD?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            self.close()