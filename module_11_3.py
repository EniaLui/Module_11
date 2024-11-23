def introspection_info(obj):

    info = {
        'type': type(obj).__name__,
        'attributes': [],
        'methods': [],
        'module': obj.__module__ if hasattr(obj, '__module__') else None,
        # Функция hasattr() возвращает флаг, указывающий на то, содержит ли объект obj атрибут __module__.
    }

    attributes = dir(obj)

    for attribute in attributes:
        attr_value = getattr(obj, attribute)
        if callable(attr_value):
            info['methods'].append(attribute)
        else:
            info['attributes'].append(attribute)

    info['str'] = str(obj) if hasattr(obj, '__str__') else None

    if hasattr(obj, '__len__'):
        info['length'] = len(obj)

    return info

number_info = introspection_info(42)
print(number_info)
