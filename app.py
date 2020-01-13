#!/usr/bin/python3

from os import environ as env

def main():
    print("Hello, world!")
    connect_to_database()
    read_hardcoded_path()

def connect_to_database():
    HOST = env['host']
    PORT = env['port']
    USER = env['user']
    PASS = env['pass']
    DB   = env[ 'db' ]
    print(f"Las credenciales son: {HOST}, {PORT}, {USER}, {PASS}, {DB}")
    print("TODO: que se conecte a la base de datos...")

def read_hardcoded_path():
    print("Debería ser más limpio. Pero no lo es xdxdxdxd")
    hardcode_path = "/data/fichero.txt"
    with open (hardcode_path, 'r') as fichero:
        print(fichero.readline())

if __name__ == "__main__":
    main()