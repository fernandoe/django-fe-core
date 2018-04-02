from django.test import TestCase

from fe_core.models import Entity


class TestEntidade(TestCase):
    def test_create_entidade_com_nome(self):
        nome = 'nome-entidade'
        entidade = Entity.objects.create_entity(nome)
        self.assertIsNotNone(entidade)
        self.assertEquals(nome, entidade.name)

    def test_create_entidade_sem_nome(self):
        entidade = Entity.objects.create_entity()
        self.assertIsNotNone(entidade)
        self.assertEquals(36, len(entidade.name))
