import unittest
from library_system import Livro, Membro, Biblioteca


class TestLivro(unittest.TestCase):
    # Testes Positivos
    def test_emprestar_livro_positivo(self):
        livro = Livro("Livro A", "Autor A", "ISBN001")
        self.assertTrue(livro.emprestar())
        self.assertFalse(livro.disponivel)

    def test_devolver_livro_positivo(self):
        livro = Livro("Livro B", "Autor B", "ISBN002")
        livro.emprestar()
        self.assertTrue(livro.devolver())
        self.assertTrue(livro.disponivel)

    # Testes Negativos
    def test_emprestar_livro_negativo_ja_emprestado(self):
        livro = Livro("Livro C", "Autor C", "ISBN003")
        livro.emprestar()
        self.assertFalse(livro.emprestar())

    def test_devolver_livro_negativo_ja_disponivel(self):
        livro = Livro("Livro D", "Autor D", "ISBN004")
        self.assertFalse(livro.devolver())


class TestMembro(unittest.TestCase):
    # Testes Positivos
    def test_emprestar_livro_membro_positivo(self):
        membro = Membro("Membro 1", "ID001")
        livro = Livro("Livro E", "Autor E", "ISBN005")
        self.assertTrue(membro.emprestar_livro(livro))
        self.assertIn(livro, membro.livros_emprestados)
        self.assertFalse(livro.disponivel)

    def test_devolver_livro_membro_positivo(self):
        membro = Membro("Membro 2", "ID002")
        livro = Livro("Livro F", "Autor F", "ISBN006")
        membro.emprestar_livro(livro)
        self.assertTrue(membro.devolver_livro(livro))
        self.assertNotIn(livro, membro.livros_emprestados)
        self.assertTrue(livro.disponivel)

    # Testes Negativos
    def test_emprestar_livro_membro_negativo_livro_indisponivel(self):
        membro = Membro("Membro 3", "ID003")
        livro = Livro("Livro G", "Autor G", "ISBN007")
        livro.emprestar()  # Livro já emprestado
        self.assertFalse(membro.emprestar_livro(livro))

    def test_devolver_livro_membro_negativo_livro_nao_emprestado(self):
        membro = Membro("Membro 4", "ID004")
        livro = Livro("Livro H", "Autor H", "ISBN008")
        self.assertFalse(membro.devolver_livro(livro))


class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()
        self.livro1 = Livro("Livro I", "Autor I", "ISBN009")
        self.livro2 = Livro("Livro J", "Autor J", "ISBN010")
        self.membro1 = Membro("Membro 5", "ID005")
        self.membro2 = Membro("Membro 6", "ID006")

    # Testes Positivos
    def test_adicionar_livro_positivo(self):
        self.assertTrue(self.biblioteca.adicionar_livro(self.livro1))
        self.assertIn(self.livro1.isbn, self.biblioteca.livros)

    def test_remover_livro_positivo(self):
        self.biblioteca.adicionar_livro(self.livro1)
        self.assertTrue(self.biblioteca.remover_livro(self.livro1.isbn))
        self.assertNotIn(self.livro1.isbn, self.biblioteca.livros)

    def test_adicionar_membro_positivo(self):
        self.assertTrue(self.biblioteca.adicionar_membro(self.membro1))
        self.assertIn(self.membro1.id_membro, self.biblioteca.membros)

    def test_remover_membro_positivo(self):
        self.biblioteca.adicionar_membro(self.membro1)
        self.assertTrue(self.biblioteca.remover_membro(self.membro1.id_membro))
        self.assertNotIn(self.membro1.id_membro, self.biblioteca.membros)

    def test_emprestar_livro_biblioteca_positivo(self):
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.adicionar_membro(self.membro1)
        self.assertTrue(self.biblioteca.emprestar_livro(
            self.livro1.isbn, self.membro1.id_membro))
        self.assertFalse(self.livro1.disponivel)
        self.assertIn(self.livro1, self.membro1.livros_emprestados)

    def test_devolver_livro_biblioteca_positivo(self):
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.adicionar_membro(self.membro1)
        self.biblioteca.emprestar_livro(
            self.livro1.isbn, self.membro1.id_membro)
        self.assertTrue(self.biblioteca.devolver_livro(
            self.livro1.isbn, self.membro1.id_membro))
        self.assertTrue(self.livro1.disponivel)
        self.assertNotIn(self.livro1, self.membro1.livros_emprestados)

    def test_buscar_livro_positivo(self):
        self.biblioteca.adicionar_livro(self.livro1)
        self.assertEqual(self.biblioteca.buscar_livro(
            self.livro1.isbn), self.livro1)

    def test_buscar_membro_positivo(self):
        self.biblioteca.adicionar_membro(self.membro1)
        self.assertEqual(self.biblioteca.buscar_membro(
            self.membro1.id_membro), self.membro1)

    # Testes Negativos
    def test_adicionar_livro_negativo_ja_existe(self):
        self.biblioteca.adicionar_livro(self.livro1)
        self.assertFalse(self.biblioteca.adicionar_livro(self.livro1))

    def test_remover_livro_negativo_nao_existe(self):
        self.assertFalse(self.biblioteca.remover_livro("ISBN_INEXISTENTE"))

    def test_adicionar_membro_negativo_ja_existe(self):
        self.biblioteca.adicionar_membro(self.membro1)
        self.assertFalse(self.biblioteca.adicionar_membro(self.membro1))

    def test_remover_membro_negativo_nao_existe(self):
        self.assertFalse(self.biblioteca.remover_membro("ID_INEXISTENTE"))

    def test_emprestar_livro_biblioteca_negativo_livro_nao_existe(self):
        self.biblioteca.adicionar_membro(self.membro1)
        self.assertFalse(self.biblioteca.emprestar_livro(
            "ISBN_INEXISTENTE", self.membro1.id_membro))

    def test_emprestar_livro_biblioteca_negativo_membro_nao_existe(self):
        self.biblioteca.adicionar_livro(self.livro1)
        self.assertFalse(self.biblioteca.emprestar_livro(
            self.livro1.isbn, "ID_INEXISTENTE"))

    def test_emprestar_livro_biblioteca_negativo_livro_ja_emprestado(self):
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.adicionar_membro(self.membro1)
        self.biblioteca.emprestar_livro(
            self.livro1.isbn, self.membro1.id_membro)
        self.assertFalse(self.biblioteca.emprestar_livro(
            self.livro1.isbn, self.membro1.id_membro))

    def test_devolver_livro_biblioteca_negativo_livro_nao_existe(self):
        self.biblioteca.adicionar_membro(self.membro1)
        self.assertFalse(self.biblioteca.devolver_livro(
            "ISBN_INEXISTENTE", self.membro1.id_membro))

    def test_devolver_livro_biblioteca_negativo_membro_nao_existe(self):
        self.biblioteca.adicionar_livro(self.livro1)
        self.assertFalse(self.biblioteca.devolver_livro(
            self.livro1.isbn, "ID_INEXISTENTE"))

    def test_devolver_livro_biblioteca_negativo_livro_nao_emprestado(self):
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.adicionar_membro(self.membro1)
        self.assertFalse(self.biblioteca.devolver_livro(
            self.livro1.isbn, self.membro1.id_membro))


if __name__ == '__main__':
    unittest.main()
