from bio.ler_fasta import ler_fasta

def identificar_mutacao(caminho_arquivo_fasta, posicao, nucleotideo_original, nucleotideo_mutado):
    organismos = ler_fasta(caminho_arquivo_fasta)
    mutacoes = {}

    for organismo in organismos:
        sequencia = organismo.sequencia
        if len(sequencia) > posicao and sequencia[posicao] == nucleotideo_mutado:
            mutacoes[organismo.nome] = "Presente"
        else:
            mutacoes[organismo.nome] = "Ausente"

    for organismo, status in mutacoes.items():
        print(f"Organismo: {organismo}, Mutação: {status}")

