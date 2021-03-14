def find_email_domain(address):
    i = address.index('@')
    return address[i+1:]
