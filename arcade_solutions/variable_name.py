def variable_name(name):
    return name.replace('_', '').isalnum() and not name[0].isdigit()
