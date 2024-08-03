from bio.ler_fasta import ler_fasta
from bio.sequencia import Sequencia

def analisar_composicao_nucleotideos(caminho_arquivo_fasta):
    organismos = ler_fasta(caminho_arquivo_fasta)

    for organismo in organismos: #para o organismo dentro de organismo
        seq = Sequencia(organismo.sequencia)
        total_bases = len(seq)
        percentual_A = seq.calcular_percentual(["A"]) * 100
        percentual_T = seq.calcular_percentual(["T"]) * 100
        percentual_C = seq.calcular_percentual(["C"]) * 100
        percentual_G = seq.calcular_percentual(["G"]) * 100
        percentual_CG = (percentual_C + percentual_G)

        print(f"Organismo: {organismo.nome}")
        print(f"A: {percentual_A:.2f}%")
        print(f"T: {percentual_T:.2f}%")
        print(f"C: {percentual_C:.2f}%")
        print(f"G: {percentual_G:.2f}%")
        print(f"O percentual de C + G é: {percentual_CG:.2f}%\n:")

analisar_composicao_nucleotideos("arquivos/Flaviviridae-genomes.fasta")