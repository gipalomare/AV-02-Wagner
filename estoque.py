from produto import Produto

LIMITE_ESTOQUE = 100
estoque = [Produto() for _ in range(LIMITE_ESTOQUE)]
qtdProduto = 0

def adicionarproduto():
    global qtdProduto
       if qtdProduto >= LIMITE_ESTOQUE:
        print("O estoque está cheio, não é possível adicionar mais produtos.")
        return

    novoProduto = Produto()
    novoProduto.nomeproduto = input("Digite o nome do novo produto: ")
    novoProduto.quantidade = int(input("Digite a quantidade que deseja adicionar: "))
    novoProduto.preco = float(input("Digite o preço do produto: "))

     estoque[qtdProduto] = novoProduto
    qtdProduto += 1
    print("Produto adicionado")

def listaProdutos():
   if qtdProduto == 0:
        print("O estoque está vazio.")
    else:
        print("Produtos em estoque:")
        for i in range(qtdProduto):
            print(f"Nome: {estoque[i].nomeproduto}, Quantidade: {estoque[i].quantidade}, Preço: R$ {estoque[i].preco:.2f}")
    print()
   
def venderProduto():
    nome = input("Digite o nome do produto que deseja vender: ")
    quantidade = int(input("Digite a quantidade que deseja vender: "))

    for i in range(qtdProduto):
        if nome == estoque[i].nomeproduto:
            if estoque[i].quantidade >= quantidade:
                estoque[i].quantidade -= quantidade
                print("Produto vendido!")
            else:
                print("Quantidade insuficiente no estoque, avise o gerente.")
            return
    print("Produto não encontrado no estoque.")

def removerProduto():
    nome = input("Digite o nome do produto que deseja remover: ")
    quantidade = int(input("Digite a quantidade que deseja remover: "))

    for i in range(qtdProduto):
        if nome == estoque[i].nomeproduto:
            if estoque[i].quantidade >= quantidade:
                estoque[i].quantidade -= quantidade
                print("Produto removido!")
            else:
                print("Quantidade insuficiente no estoque, avise o gerente.")
            return
    print("Produto não encontrado no estoque.")