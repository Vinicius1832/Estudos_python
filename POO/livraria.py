class livros:
    livrosLista = []
    def __init__(self, titulo, autor, codigo, ano ):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.ano = ano

    def __str__(self):
        return f'Tiulo {self.titulo} \nAutor: {self.autor} \nCódigo: {self.codigo} Ano: {self.ano}'

    def adicionar(self):
        self.livrosLista.append(self)

    def mostrar1(self):
        return self.livrosLista
