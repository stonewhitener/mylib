import binascii


def bytes_from_file(filename, chunksize=8192):
    """
    Convert file to bytes
    """
    with open(filename, 'rb') as f:
        ret = bytes()
        while True:
            chunk = f.read(chunksize)
            if chunk:
                ret += chunk
            else:
                break
        return ret


def bytes_from_int(x: int):
    """
    Convert integer to bytes
    """
    return x.to_bytes((x.bit_length() + 7) // 8, byteorder='big')


def int_from_bytes(b: bytes):
    """
    Convert bytes to integer
    """
    return int.from_bytes(b, byteorder='big')


def str_from_int(x: int):
    """
    Convert integer to string
    """
    return bytes_from_int(x).decode()


def int_from_str(s: str):
    """
    Convert string to integer
    """
    return int_from_bytes(s.encode())


def bytes_from_str(s: str):
    """
    Convert string to bytes
    """
    return s.encode()


def str_from_bytes(b: bytes):
    """
    Convert bytes to string
    """
    return b.decode()
