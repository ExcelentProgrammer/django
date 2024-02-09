from django.core.exceptions import ObjectDoesNotExist


def dd(data=''):
    try:
        raise Exception(data)
    except ObjectDoesNotExist:
        return False
