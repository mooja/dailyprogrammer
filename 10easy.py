import re


def valid_phone_number(number):
    seperator = r'(\s|\.|\-)?'
    area_code = r'(\(\d{3}\)|\d{3})?'
    pnum = r'(\d{3})' + seperator + r'(\d{4})$'

    import ipdb; ipdb.set_trace()

    if re.search(r'^'+area_code+seperator+pnum, number):
        return True
    return False

if __name__ == '__main__':
    valid_phone_number("845-338-1542")
