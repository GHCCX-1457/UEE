from peewee import CharField

from entity.BaseEntity import BaseEntity


class HZUser(BaseEntity):

    username = CharField(max_length=35)
    password = CharField(max_length=35)
    email = CharField(max_length=35)
    phone = CharField(max_length=35)
    address = CharField(max_length=35)
    name = CharField(max_length=35)
    role = CharField(max_length=35)

    class Meta:
        table_name = 'hz_user'