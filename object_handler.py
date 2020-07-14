from collections import namedtuple
from task import Ticket
from user import User

class ObjectHandler:

    @staticmethod
    def get_cls_name(obj):
        obj_cls_name = type(obj).__name__.lower()
        return obj_cls_name

    @staticmethod
    def get_obj_attrs(obj, *obj_attrs):
        obj_dict = {}
        for k, v in vars(obj).items():
            if k.startswith('_'):
                k = k.replace('_', '', 1)
            obj_dict[k] = v
        return obj_dict

    @staticmethod
    def to_namedtuple(obj):
        type_name = ObjectHandler.get_cls_name(obj)
        fields = ObjectHandler.get_obj_attrs(obj)
        try:
            NamedTuple = namedtuple(type_name, fields.keys())
            namedtuple_obj = NamedTuple(**fields)
            return namedtuple_obj
        except ValueError as e:
            print(e)

    @staticmethod
    def export_obj_data(obj):
        namedtuple_obj = ObjectHandler.to_namedtuple(obj)
        return namedtuple_obj

    @staticmethod
    def get_obj_fields(obj):
        obj_fields = ObjectHandler.to_namedtuple(obj)
        return obj_fields._fields

    @staticmethod
    def get_sorted_attrs(obj, *attrs):
        obj_fields = ObjectHandler.get_obj_fields(obj)
        sorted_attrs = tuple(sorted(attrs, key = lambda field: obj_fields.index(field)))
        return sorted_attrs

    @staticmethod
    def validate_attrs(obj, *stringed_attrs):
        obj_attrs = ObjectHandler.get_obj_fields(obj)
        str_attrs_set = set(stringed_attrs)
        obj_attrs_set = set(obj_attrs)
        return str_attrs_set.issubset(obj_attrs_set)


ticket = Ticket()
user = User()
t = ObjectHandler.export_obj_data(ticket)
print(type(t).__name__)
print(t)
u = ObjectHandler.get_obj_fields(user)
print(u)
print(ObjectHandler.get_sorted_attrs(user, 'user_name', 'user_login', 'user_password'))


