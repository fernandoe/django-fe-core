from django.test import TestCase

from fe_core.models import User, Entity
from fe_core.factories import UserFactory, EntityFactory


class TestUsuario(TestCase):
    def setUp(self):
        self.email = 'meu_email@domainname.com'
        self.password = 'minha-senha-secreta'
        self.entity = EntityFactory()

    def test_contructor(self):
        usuario = User.objects.create()
        self.assertIsNotNone(usuario)
        self.assertFalse(usuario.is_staff)
        self.assertFalse(usuario.is_superuser)
        self.assertTrue(usuario.is_active)

    def test_check_password(self):
        usuario = UserFactory.create(password=self.password)
        self.assertTrue(usuario.check_password(self.password))

    def test_create_user(self):
        usuario = User.objects.create_user(email=self.email, password=self.password)
        self.assertIsNotNone(usuario)
        self.assertFalse(usuario.is_staff)
        self.assertFalse(usuario.is_superuser)
        self.assertTrue(usuario.is_active)

    def test_create_user_com_entidade(self):
        self.assertEquals(1, Entity.objects.all().count())
        usuario = User.objects.create_superuser(
            email=self.email,
            password=self.password,
            entity=self.entity
        )
        self.assertEquals(self.entity, usuario.entity)
        self.assertEquals(1, Entity.objects.all().count())

    def test_create_user_sem_entidade(self):
        self.assertEquals(1, Entity.objects.all().count())
        usuario = User.objects.create_superuser(
            email=self.email,
            password=self.password
        )
        self.assertIsNone(usuario.entity)
        self.assertEquals(1, Entity.objects.all().count())
