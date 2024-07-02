from .constantes import DNA_PARA_AMINOACIDO

class Sequencia:
    COMPLEMENTO = str.maketrans('ATCG', 'TAGC')

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
        return Sequencia(self.sequencia.translate(self.COMPLEMENTO))

    def complementar_reversa(self):
        return Sequencia(self.sequencia.translate(self.COMPLEMENTO)[::-1])

    def transcrever(self):
        return Sequencia(self.sequencia.replace('T', 'U'))

    def traduzir(self, parar=False):
        proteina = []
        for i in range(0, len(self.sequencia), 3):
            codon = self.sequencia[i:i+3]
            if len(codon) < 3:
                break  
            aminoacido = DNA_PARA_AMINOACIDO.get(codon, 'X') 
            if parar and aminoacido == '*':
                break  
            proteina.append(aminoacido)
        return ''.join(proteina)

    def calcular_percentual(self, bases):
        total_bases = len(self.sequencia)
        if total_bases == 0:
            return 0.0  
        count = sum(self.sequencia.count(base) for base in bases)
        return count / total_bases
