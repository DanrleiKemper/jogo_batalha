import random

#atributos e metodos
class Personangem: 
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel

    #metodo exibir detalhes
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
    
    #metodo receber ataque
    def receber_ataque(self, dano):
        self.__vida -= dano

        if self.__vida <= 0:
            self.__vida = 0
    
    #metodo  ataque
    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4) # Baseado no vível
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano")
    

class Heroi(Personangem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel,)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8) # Dano aumentado
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano")
    

class Inimigo(Personangem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"
    

class Jogo:
    """ 
        Classe orquestradora do jogo
    """
    def __init__(self) -> None:
        self.heroi = Heroi(nome="Heroi", vida=100, nivel=5, habilidade="fogo")
        self.inimigo = Inimigo(nome="Morcego", vida=80, nivel=5, tipo="caçador")
    
    def iniciar_batalha(self
    ):
        """
            Fazer a gestão da batalha em turnos 
        """
        print("Iniciando a batalha")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens: ")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione ENTER para atacar")
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial):")

            if escolha =='1':
                self.heroi.atacar(self.inimigo)
            elif escolha =='2':
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha inválida. Escolha novamente.")

            if self.inimigo.get_vida() > 0:
                #inimigo ataca heroi
                self.inimigo.atacar(self.heroi)
        
        if self.heroi.get_vida() > 0:
            print("Você venceu a batalha.")
        else:
            print("Você foi derrotado.")


# Criar instância do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()




#heroi = Heroi(nome="Heroi", vida=100, nivel=5, habilidade="fogo")
#print(heroi.exibir_detalhes())
#inimigo = Inimigo(nome="Morcego", vida=80, nivel=3, tipo="caçador")
#print(inimigo.exibir_detalhes())


