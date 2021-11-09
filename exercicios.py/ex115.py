from modulos import cadastro
import pickle

pessoas = pickle.load(open("pessoas.dat", "rb"))

cadastro.menu(pessoas)

pickle.dump(pessoas, open("pessoas.dat", "wb"))
