from bio.constantes import DNA_PARA_AMINOACIDO
from bio.constantes import DNA_STOP_CODONS

class Sequencia:
    COMPLEMENTO = str.maketrans('ATCG', 'TAGC') #cria uma tabela de traducao de forma ++ simples

    def __init__(self, sequencia):
        self.sequencia = sequencia.upper()

    def __repr__(self):
        return f'Sequencia("{self.sequencia}")'

    def __iter__(self):
        return iter(self.sequencia)

    def __str__(self):
        return self.sequencia

    def __len__(self):
        return len(self.sequencia)

    def __eq__(self, outra_sequencia):
        return str(self) == str(outra_sequencia)

    def __getitem__(self, index):
        return self.sequencia[index]

    def complementar(self):
        return Sequencia(self.sequencia.translate(self.COMPLEMENTO)) #traduz todos os caracteres da string

    def complementar_reversa(self):
        return Sequencia(self.sequencia.translate(self.COMPLEMENTO)[::-1]) #pego todos os caracteres da string e inverte

    def transcrever(self):
        return Sequencia(self.sequencia.replace('T', 'U')) #substitui T por U

    def traduzir(self, parar):
        proteina = ""
        for i in range(0, len(self.sequencia), 3):
            codon = self.sequencia[i:i+3]

            if codon in DNA_STOP_CODONS:
                # veriica o parametro parar
                if parar == True:
                    return proteina
                #se nao for..
                elif parar == False:
                    proteina += "*" #add 

            else: #se n for stop codon.. 
                if codon in DNA_PARA_AMINOACIDO:
                    proteina += DNA_PARA_AMINOACIDO[codon] #tradução de fato 
                else: #se nao tiver dentro de dna para aminoacido 
                    proteina += "X"   #add X         
        return proteina

    def calcular_percentual(self, bases):
        total_bases = len(self.sequencia)
        if total_bases == 0:
            return 0.0  # Retorna 0.0 se a sequência estiver vazia
        count = sum(self.sequencia.count(base) for base in bases)
        return count / total_bases  # Retorna a proporção de bases específicas
