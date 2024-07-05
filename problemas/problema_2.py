from bio.ler_fasta import ler_fasta
from bio.sequencia import Sequencia

def traduzir_sequencias(caminho_arquivo_fasta):
    organismos = ler_fasta(caminho_arquivo_fasta)

    for organismo in organismos:
        seq = Sequencia(organismo.sequencia)
        proteina = seq.traduzir()
        print(f'Organismo: {organismo.nome}')
        print(f'Sequência de Proteína: {proteina}\n')

traduzir_sequencias("arquivos/Flaviviridae-genomes.fasta")