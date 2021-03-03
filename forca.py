from random import *
from tkinter import *
from tkinter import messagebox

# Primeira tela ao clicar em cadastro de palavras, será exibido a lista das palavras já cadastradas e uma opção
# para adicionar novas palavras


def cadastro_palavra():
    novo()
    listapalavras = set()
    try:
        listapalavras = leitura_palavra()  # aqui se faz a leitura de todas palavras cadastradas e joga na lista
        entradatx["text"] = "Cadastrar Nova Palavra "
        b2 = Button(quadro, text="NOVA",
                    command=lambda: novapalavra())  # botão para acionar a função de adicionar palavra
        b2.place(x=250, y=10)
        listar_palavras(listapalavras)  # executa e imprime as palavras dentro da lista
    except:
        entradatx['text'] = "Entrada invalida"


# a função abaixo faz a leitura e imprime na tela as palavras cadastradas.
def listar_palavras(lista):
    scroll_bar = Scrollbar(quadro2)
    scroll_bar.pack(side=RIGHT, fill=Y)
    texto = Text(quadro2, background="#aaaaaa", yscrollcommand=scroll_bar.set)
    texto.pack()
    texto.insert(INSERT, "-=Palavras Existentes=-\n")
    texto.insert(INSERT, "\n")
    for palavra in lista:
        texto.insert(INSERT, "{}\n".format(palavra))


# função executada ao clicar no botão de criar nova palavra, ele captura a letra e envia para fuma nova função
def novapalavra():
    novo()
    entradatx["text"] = "Digite a palavra para cadastrar"
    vpalavra = StringVar()
    tpalavra = Entry(quadro2, textvariable=vpalavra)
    tpalavra.pack()
    b3 = Button(quadro2, text="Cadastrar", command=lambda: cadastro_novapalavra(vpalavra.get()))
    b3.pack()


# apos capturar a palavra a função abaixo faz o tratamento da string e adiciona a palavra em uma lista,
# na sequencia ele grava no arquivo.    
def cadastro_novapalavra(palavra):
    palavra = palavra.lower()
    listapalavras.add(palavra)
    with open("palavras.txt", "w", encoding="UTF-8") as leitura:
        for word in listapalavras:
            leitura.write(word + "\n")
    novo()
    entradatx["text"] = "Palavra Cadastrada!"
    b5 = Button(quadro2, text="Listar Palavras", command=lambda: listar_palavras(
        listapalavras))  # botao listar palavras inserido para dar continuidade a tela
    b5.pack()


# função de leitura do arquivo para as palavras cadastradas, caso o arquivo não exista,
# sera criado um novo arquivo ja com duas palavras para o programa ser executado idependente de ter  arquivo ja salvo.
def leitura_palavra():
    global listapalavras
    listapalavras = set()
    try:
        with open("palavras.txt", "r", encoding="UTF-8") as leitura:
            for word in leitura:
                word = word.replace("\n", "").strip()
                listapalavras.add(word)
            return listapalavras
    # caso o arquivo não exista, ele faz a criação de um novo inserindo duas palavras
    # para perfeita execucao do programa
    except:
        with open("palavras.txt", "w", encoding="UTF-8") as leitura:
            leitura.write("banana\nmelancia\n")
            listapalavras = "banana", "melancia"
            return listapalavras


# primeira tela ao clicar em jogar, ele faz a leitura da palavra aleatoria e define a palavra oculta.
def forcaintro():
    novo()
    aleatorio = palavra_aleatoria()
    global palavra, oculto, tentativas
    tentativas = 0
    palavra = aleatorio[0]
    oculto = aleatorio[1]
    desenha_forca()


# função para selecionar na lista uma palavra de maneira aleatoria.
def palavra_aleatoria():
    lista = list(leitura_palavra())
    n = randint(0, len(lista) - 1)
    palavra = lista[n]
    oculto = ["_" for letra in palavra]
    return palavra, oculto


# apartir da primeira jogada o codigo abaixo passa a ser chamado a cada rodada capturando letra a letra,
# abaixo ele faz a verificação se o jogo acabou ou não.
def jogar_forca():
    ocultotx['text'] = oculto
    entradatx['text'] = "Digite uma letra ->"
    ventrada = StringVar()
    tentrada = Entry(quadro, textvariable=ventrada, insertwidth=20).place(x=200, y=6, width=20, height=30)
    b1 = Button(quadro, text="Jogar", command=lambda: letraentrada(ventrada.get()))
    b1.place(x=230, y=10)
    if "_" not in oculto:
        ganhar()
    if tentativas == 8:
        perder(palavra)


# função de captura da letra, faz se o tratamento e verificação se a letra contem na palavra selecionada.
def letraentrada(letraentrada):
    c = 0
    letraentrada = str(letraentrada).lower()
    if letraentrada not in palavra:
        global tentativas
        tentativas += 1
        desenha_forca()
    for letra in palavra:
        if letra == letraentrada:
            oculto[c] = palavra[c]
        c += 1
    ocultotx['text'] = oculto
    jogar_forca()


# função para desenhar o boneco de acordo com os erros do usuario.
def desenha_forca():
    if tentativas == 0:
        forca = Text(quadro2, background="#aaaaaa")
        forca.pack()
        forca.insert(INSERT, "  _______     \n")
        forca.insert(INSERT, " |/      |    \n")
        forca.insert(INSERT, " |            \n")
        forca.insert(INSERT, " |            \n")
        forca.insert(INSERT, " |            \n")
        forca.insert(INSERT, " |            \n")
        forca.insert(INSERT, "_|___         \n")
        forca.insert(INSERT, "\n")
    if tentativas == 1:
        novo()
        forca = Text(quadro2, background="#aaaaaa")
        forca.pack()
        forca.insert(INSERT, "  _______     \n")
        forca.insert(INSERT, " |/      |    \n")
        forca.insert(INSERT, " |      (_)   \n")
        forca.insert(INSERT, " |            \n")
        forca.insert(INSERT, " |            \n")
        forca.insert(INSERT, " |            \n")
        forca.insert(INSERT, "_|___         \n")
        forca.insert(INSERT, "\n")

    if tentativas == 2:
        novo()
        forca = Text(quadro2, background="#aaaaaa")
        forca.pack()
        forca.insert(INSERT, "  _______     \n")
        forca.insert(INSERT, " |/      |    \n")
        forca.insert(INSERT, " |      (_)   \n")
        forca.insert(INSERT, " |      \     \n")
        forca.insert(INSERT, " |            \n")
        forca.insert(INSERT, " |            \n")
        forca.insert(INSERT, "_|___         \n")
        forca.insert(INSERT, "\n")

    if tentativas == 3:
        novo()
        forca = Text(quadro2, background="#aaaaaa")
        forca.pack()
        forca.insert(INSERT, "  _______     \n")
        forca.insert(INSERT, " |/      |    \n")
        forca.insert(INSERT, " |      (_)   \n")
        forca.insert(INSERT, " |      \|    \n")
        forca.insert(INSERT, " |            \n")
        forca.insert(INSERT, " |            \n")
        forca.insert(INSERT, "_|___         \n")
        forca.insert(INSERT, "\n")

    if tentativas == 4:
        novo()
        forca = Text(quadro2, background="#aaaaaa")
        forca.pack()
        forca.insert(INSERT, "  _______     \n")
        forca.insert(INSERT, " |/      |    \n")
        forca.insert(INSERT, " |      (_)   \n")
        forca.insert(INSERT, " |      \|/   \n")
        forca.insert(INSERT, " |            \n")
        forca.insert(INSERT, " |            \n")
        forca.insert(INSERT, "_|___         \n")
        forca.insert(INSERT, "\n")

    if tentativas == 5:
        novo()
        forca = Text(quadro2, background="#aaaaaa")
        forca.pack()
        forca.insert(INSERT, "  _______     \n")
        forca.insert(INSERT, " |/      |    \n")
        forca.insert(INSERT, " |      (_)   \n")
        forca.insert(INSERT, " |      \|/   \n")
        forca.insert(INSERT, " |       |    \n")
        forca.insert(INSERT, " |            \n")
        forca.insert(INSERT, "_|___         \n")
        forca.insert(INSERT, "\n")

    if tentativas == 6:
        novo()
        forca = Text(quadro2, background="#aaaaaa")
        forca.pack()
        forca.insert(INSERT, "  _______     \n")
        forca.insert(INSERT, " |/      |    \n")
        forca.insert(INSERT, " |      (_)   \n")
        forca.insert(INSERT, " |      \|/   \n")
        forca.insert(INSERT, " |       |    \n")
        forca.insert(INSERT, " |      /     \n")
        forca.insert(INSERT, "_|___         \n")
        forca.insert(INSERT, "\n")

    if tentativas == 7:
        novo()
        forca = Text(quadro2, background="#aaaaaa")
        forca.pack()
        forca.insert(INSERT, "  _______     \n")
        forca.insert(INSERT, " |/      |    \n")
        forca.insert(INSERT, " |      (_)   \n")
        forca.insert(INSERT, " |      \|/   \n")
        forca.insert(INSERT, " |       |    \n")
        forca.insert(INSERT, " |      / \   \n")
        forca.insert(INSERT, "_|___         \n")
        forca.insert(INSERT, "\n")
    jogar_forca()
# função chamada quando o jogador vence
def ganhar():
    novo()
    entradatx['text'] = "        -=GANHOU=-"
    forca = Text(quadro2, background="#aaaaaa")
    forca.pack()
    forca.insert(INSERT, "Parabéns, Você GANHOU!!! \n")
    forca.insert(INSERT, "A Palavra é {} erros= {}\n".format(palavra, tentativas))
    forca.insert(INSERT, "       ___________      \n")
    forca.insert(INSERT, "      '._==_==_=_.'     \n")
    forca.insert(INSERT, "      .-\\:      /-.    \n")
    forca.insert(INSERT, "     | (|:.     |) |    \n")
    forca.insert(INSERT, "      '-|:.     |-'     \n")
    forca.insert(INSERT, "        \\::.    /      \n")
    forca.insert(INSERT, "         '::. .'        \n")
    forca.insert(INSERT, "           ) (          \n")
    forca.insert(INSERT, "         _.' '._        \n")
    forca.insert(INSERT, "        '-------'       \n")


# função chaada quando o jogador perde
def perder(palavra):
    novo()
    entradatx['text'] = "        || PERDEU ||"
    forca = Text(quadro2, background="#aaaaaa")
    forca.pack()
    forca.insert(INSERT, "Você foi enforcado! \n")
    forca.insert(INSERT, "A palavra era {}\n".format(palavra))
    forca.insert(INSERT, "    _______________         \n")
    forca.insert(INSERT, "   /               \       \n")
    forca.insert(INSERT, "  /                 \      \n")
    forca.insert(INSERT, "//                   \/\  \n")
    forca.insert(INSERT, "\|   XXXX     XXXX   | /   \n")
    forca.insert(INSERT, " |   XXX       XXX   |      \n")
    forca.insert(INSERT, " |                   |      \n")
    forca.insert(INSERT, " \__      XXX      __/     \n")
    forca.insert(INSERT, "   |\     XXX     /|       \n")
    forca.insert(INSERT, "   | |           | |        \n")
    forca.insert(INSERT, "   | I I I I I I I |        \n")
    forca.insert(INSERT, "   |  I I I I I I  |        \n")
    forca.insert(INSERT, "    \___        __/       \n")
    forca.insert(INSERT, "       \_______/           \n")


# função criada para limpeza de tela.
def novo():
    global quadro, quadro2, ocultotx, entradatx
    quadro = Frame(app, borderwidth="2", bg="#aaaaaa", relief="groove")
    quadro.place(x=190, y=100, width=300, height=350)
    quadro2 = Frame(quadro, borderwidth="2", bg="#aaaaaa", relief="groove")
    quadro2.place(x=3, y=50, width=290, height=295)
    ocultotx = Label(quadro, text="", bg="#aaaaaa", font=("Arial", 20), justify="center")
    ocultotx.place(x=70, y=300)
    entradatx = Label(quadro, text=".::MENU::.", bg="#aaaaaa", font=("Arial", 16))
    entradatx.place(x=10, y=10)


def sobre():
    messagebox.showinfo(title="Jogo da Forca",
                        message="Procurando sempre aprimorar! \n"
                                "Para maiores informações ou sugestões: Rafaelmafra@live.com")


app = Tk()
app.title(".:: JOGO DA FORCA ::.")
app.geometry('510x500+300+100')
app.configure(background="#aaaaaa")
barrademenus = Menu(app)
app.config(menu=barrademenus)
menusobre = Menu(barrademenus, tearoff=0)
menusobre.add_command(label="Info", command=sobre)
menusobre.add_command(label="Sair", command=app.quit)
barrademenus.add_cascade(label="Sobre", menu=menusobre)
Button(app, text=".::Cadastrar Palavra::.", command=lambda: cadastro_palavra()).place(x=10, y=100, width=150, height=30)
Button(app, text=".::Jogar Forca ::.", command=lambda: forcaintro()).place(x=10, y=130, width=150, height=30)
Button(app, text='.::Sair::.', command=app.quit).place(x=10, y=160, width=150, height=30)

novo()
menutx = Label(app, text=".:: Jogo Da Forca ::. \o/", bg="#aaaaaa", font=("Arial", 26), justify="center", pady=20)
menutx.pack()

rodape = Label(app, text='Desenvolvido por Rafael Mafra', bg="#aaaaaa", fg="#fff", justify="center")
rodape.place(x=5, y=450, width=500, height=30)

app.mainloop()
