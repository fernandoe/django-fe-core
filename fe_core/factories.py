import factory

from .models import User, Entity


class EntityFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Entidade Nome: {0}'.format(n))

    class Meta:
        model = Entity


class UserFactory(factory.django.DjangoModelFactory):
    entity = factory.SubFactory(EntityFactory)
    email = factory.Sequence(lambda n: u'{0}@test.com'.format(n))
    is_staff = False
    is_active = True

    class Meta:
        model = User

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        from django.contrib.auth.hashers import make_password
        password = kwargs.get('password')
        if password:
            kwargs['password'] = make_password(kwargs['password'])
        return super(UserFactory, cls)._create(model_class, *args, **kwargs)
