class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return True
        return False


class Membro:
    def __init__(self, nome, id_membro):
        self.nome = nome
        self.id_membro = id_membro
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if livro.disponivel and livro not in self.livros_emprestados:
            self.livros_emprestados.append(livro)
            livro.emprestar()
            return True
        return False

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.devolver()
            return True
        return False


class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.membros = {}

    def adicionar_livro(self, livro):
        if livro.isbn not in self.livros:
            self.livros[livro.isbn] = livro
            return True
        return False

    def remover_livro(self, isbn):
        if isbn in self.livros:
            del self.livros[isbn]
            return True
        return False

    def adicionar_membro(self, membro):
        if membro.id_membro not in self.membros:
            self.membros[membro.id_membro] = membro
            return True
        return False

    def remover_membro(self, id_membro):
        if id_membro in self.membros:
            del self.membros[id_membro]
            return True
        return False

    def emprestar_livro(self, isbn_livro, id_membro):
        livro = self.livros.get(isbn_livro)
        membro = self.membros.get(id_membro)

        if livro and membro:
            if membro.emprestar_livro(livro):
                return True
        return False

    def devolver_livro(self, isbn_livro, id_membro):
        livro = self.livros.get(isbn_livro)
        membro = self.membros.get(id_membro)

        if livro and membro:
            if membro.devolver_livro(livro):
                return True
        return False

    def buscar_livro(self, isbn):
        return self.livros.get(isbn)

    def buscar_membro(self, id_membro):
        return self.membros.get(id_membro)

def main():
    print("Sistema de Biblioteca iniciado.")
    # Exemplo de uso:
    biblioteca = Biblioteca()
    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "978-85-333-0227-3")
    membro1 = Membro("Alice", "M001")

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_membro(membro1)

    if biblioteca.emprestar_livro(livro1.isbn, membro1.id_membro):
        print(f"{membro1.nome} emprestou \"{livro1.titulo}\".")
    else:
        print(f"{membro1.nome} não conseguiu emprestar \"{livro1.titulo}\".")

    if biblioteca.devolver_livro(livro1.isbn, membro1.id_membro):
        print(f"{membro1.nome} devolveu \"{livro1.titulo}\".")
    else:
        print(f"{membro1.nome} não conseguiu devolver \"{livro1.titulo}\".")

if __name__ == "__main__":
    main()


 #teste