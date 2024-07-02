class OrganismoFasta:
    def __init__(self, id, nome, sequencia):
        self.id = id           
        self.nome = nome        
        self.sequencia = sequencia  

    def __repr__(self):
        return f"OrganismoFasta(id={self.id}, nome={self.nome}, sequencia={self.sequencia})"