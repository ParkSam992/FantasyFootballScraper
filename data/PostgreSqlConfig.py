from configparser import ConfigParser

# TODO: Want to finish this and put database login stuff behind config

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}

    full_section = f

