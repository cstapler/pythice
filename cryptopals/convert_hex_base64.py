import codecs

def hex_to_base64(hex_string):
    return codecs.encode(codecs.decode(hex_string, 'hex'), 'base64').decode()

def main():
    hex_input = input()
    result = hex_to_base64(hex_input)
    print(result)


if __name__ == "__main__":
    main()
