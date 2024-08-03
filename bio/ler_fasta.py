from bio.organismo_fasta import OrganismoFasta

def ler_fasta(caminho_do_arquivo):
    organismos = []

    with open(caminho_do_arquivo) as file:
        lines = file.readlines()
        for line in lines:
            if line[0] == ">":
                id_organismo, nome = line[1:].rstrip().split("|")
                organismos.append({
                    "id": id_organismo.strip(),
                    "nome": nome.strip(),
                    "sequencia": ""
                })
            else:
                organismos[-1]["sequencia"] += line.rstrip()

    return [OrganismoFasta(
        id=organismo["id"],
        nome=organismo["nome"],
        sequencia=organismo["sequencia"],
    ) for organismo in organismos]