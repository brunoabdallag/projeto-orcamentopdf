from tkinter import *
from tkinter import filedialog
from fpdf import FPDF
import os
import sys
from PIL import ImageTk, Image

def resource_path(relative_path):
    """ Obtenha o caminho absoluto para o recurso, funciona para dev e para PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Application:
    def __init__(self, master=None):
        # Padrão de fonte
        self.fontePadrao = ("Arial", "10")

        # Definindo a cor de fundo do master
        master.configure(bg='#F4F4F4')

        # Centralizar Container
        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=1)
        master.grid_rowconfigure(2, weight=1)
        master.grid_rowconfigure(3, weight=1)
        master.grid_rowconfigure(4, weight=1)
        master.grid_rowconfigure(5, weight=1)
        master.grid_columnconfigure(0, weight=1)

        # Primeiro Container (para título)
        self.primeiroContainer = Frame(master, bg='#F4F4F4')
        self.primeiroContainer.grid(row=0, column=0, pady=10)

        # Segundo Container (para imagem)
        self.segundoContainer = Frame(master, bg='#F4F4F4')
        self.segundoContainer.grid(row=1, column=0, pady=10)

        # Terceiro Container (para outros componentes)
        self.terceiroContainer = Frame(master, bg='#F4F4F4')
        self.terceiroContainer.grid(row=2, column=0, pady=10)

        # Quarto Container
        self.quartoContainer = Frame(master, bg='#F4F4F4')
        self.quartoContainer.grid(row=3, column=0, pady=10)

        # Form Container
        self.formContainer = Frame(master, bg='#F4F4F4')
        self.formContainer.grid(row=4, column=0, pady=10)

        # Visualizar texto Dados do usuário
        self.titulo = Label(self.primeiroContainer, text="Dados do orçamento", bg='#F4F4F4', font=("Arial", "12", "bold"))
        self.titulo.pack()

        # Adicionando uma imagem de fundo
        image_path = resource_path(r"image\logo.png")
        try:
            if os.path.exists(image_path):
                self.logo_image = ImageTk.PhotoImage(Image.open(image_path))
                self.logotipo = Label(self.segundoContainer, image=self.logo_image)
                self.logotipo.pack()
            else:
                raise FileNotFoundError(f"Imagem {image_path} não encontrada.")
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")

        self.outroTexto = Label(self.terceiroContainer, text="", bg='#F4F4F4', font=self.fontePadrao)
        self.outroTexto.pack()

        # Labels e Entradas
        labels_text = ["Projeto:", "Horas Previstas:", "Valor Hora:", "Prazo:", "Nome Arquivo:"]
        self.entries = []

        for i, text in enumerate(labels_text):
            label = Label(self.quartoContainer, text=text, font=self.fontePadrao, bg='#F4F4F4')
            label.grid(row=i, column=0, padx=10, pady=5, sticky=E)

            entry = Entry(self.quartoContainer, font=self.fontePadrao)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky=W)
            self.entries.append(entry)

        # Container para os botões
        self.botaoContainer = Frame(master, bg='#F4F4F4')
        self.botaoContainer.grid(row=len(labels_text)+4, column=0, pady=10)

        # BOTÕES
        # Gerar PDF
        self.gerarPDF = Button(self.botaoContainer, text="Gerar PDF", font=self.fontePadrao, width=12, command=self.gerarPDF_func)
        self.gerarPDF.pack(side=LEFT, padx=5)

        # Sair
        self.sair = Button(self.botaoContainer, text="Sair", font=self.fontePadrao, width=12, command=master.quit)
        self.sair.pack(side=LEFT, padx=5)

        # MENSAGEM
        self.mensagem = Label(master, text="", font=("Verdana", "9", "italic"), bg='#F4F4F4')
        self.mensagem.grid(row=len(labels_text)+6, column=0, columnspan=2, pady=10)

        # Escolher pasta
        self.pasta_destino = ""

        self.escolherPastaButton = Button(master, text="Escolher Pasta", font=self.fontePadrao, command=self.escolherPasta)
        self.escolherPastaButton.grid(row=len(labels_text)+5, column=0, pady=10)

    # Recebe os dados
    def receberDados(self):
        return [entry.get() for entry in self.entries]

    # Escolher lugar para salvar arquivo
    def escolherPasta(self):
        self.pasta_destino = filedialog.askdirectory()
        if self.pasta_destino:
            self.mensagem["text"] = f"Local: {self.pasta_destino}"
        else:
            self.mensagem["text"] = "Nenhuma pasta escolhida"

    def gerarPDF_func(self):
        projeto, horas_previstas, valor_hora, prazo, nome_arquivo = self.receberDados()

        # Efetuando a conta do valor total:
        valor_total = float(horas_previstas) * float((valor_hora).replace(',', "."))

        # Gerando o PDF
        pdf = FPDF()

        # Criando o padrão do PDF
        pdf.add_page()
        pdf.set_font("Arial")

        # Usando um template para inserir informações.
        template_path = resource_path("image/template.png")
        pdf.image(template_path, x=0, y=0)

        # Informando onde irá colocar as informações das variáveis.
        pdf.text(115, 140, projeto)
        pdf.text(115, 153, horas_previstas)
        pdf.text(115, 166, (f"{float((valor_hora).replace(",", ".")):.2f}"))
        pdf.text(115, 180, prazo)
        pdf.text(115, 193, (f"{float(valor_total):.2f}"))

        # Efetuando a exportação e o aviso de mensagem.
        if self.pasta_destino:
            caminho_completo = os.path.join(self.pasta_destino, nome_arquivo + '.pdf')
            pdf.output(caminho_completo)

        # Exibir mensagem de confirmação
        self.mensagem["text"] = "PDF gerado com sucesso!"

# Permite que os widgets sejam utilizados na aplicação
root = Tk()

# Definir o tamanho da janela
root.geometry("600x600")

# Definir o título da janela
root.title("BAC Software Inc - Gerador de Orçamento!")

# Define o ícone da janela
icon_fav = resource_path(r'image\favicon.ico')
root.iconbitmap(icon_fav)

# Vincular a classe ao root
Application(root)

# Exibir a tela
root.mainloop()
