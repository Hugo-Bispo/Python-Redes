import os

def folder(nameFolder):
    try:
        os.mkdir(nameFolder)
    except FileExistsError:
        print("Pasta já existente")