"""Contas fictícias com palavras-passe escolhidas localmente."""
from getpass import getpass
from src.database import connect,initialize
from src.auth import hash_password
def main():
 with connect() as d:
  initialize(d)
  for name,email,role in (("Ana Martins","ana@nexaserv.test","colaborador"),("Miguel Costa","miguel@nexaserv.test","tecnico"),("Sofia Almeida","sofia@nexaserv.test","responsavel")):
   if d.execute("SELECT id FROM users WHERE email=?",(email,)).fetchone():continue
   p=getpass("Palavra-passe (mínimo 8 caracteres) para "+name+": ")
   if len(p)<8:raise ValueError("Palavra-passe demasiado curta")
   d.execute("INSERT INTO users(name,email,secret,role) VALUES(?,?,?,?)",(name,email,hash_password(p),role));d.commit()
if __name__=="__main__":main()
