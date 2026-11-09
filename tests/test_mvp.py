"""Testes iniciais: T-02, T-04, T-06, T-07, T-08, T-14, T-15, T-19, T-20."""
import pytest
from fastapi import HTTPException
from src.database import connect,initialize
from src import services
def test_lifecycle(tmp_path):
 with connect(str(tmp_path/"db.sqlite3")) as d:
  initialize(d)
  users=[]
  for role in ("colaborador","tecnico","responsavel"):
   c=d.execute("INSERT INTO users(name,email,secret,role) VALUES(?,?,?,?)",(role,role+"@test","x",role));users.append({"id":c.lastrowid,"role":role})
  d.commit();ana,miguel,sofia=users
  t=services.create(d,ana,"Impressora","Não funciona","Equipamento");assert t["state"]=="Aberto"
  t=services.assign(d,sofia,t["id"],miguel["id"]);assert t["state"]=="Aberto"
  services.start(d,miguel,t["id"]);services.resolve(d,miguel,t["id"],"Reparada")
  t=services.reopen(d,ana,t["id"]);assert t["technician_id"]==miguel["id"]
  services.resolve(d,miguel,t["id"],"Nova solução")
  with pytest.raises(HTTPException):services.close(d,miguel,t["id"],True)
  with pytest.raises(HTTPException):services.close(d,sofia,t["id"],False)
  t=services.close(d,sofia,t["id"],True);assert t["state"]=="Fechado"
  with pytest.raises(HTTPException):services.reopen(d,ana,t["id"])
  with pytest.raises(HTTPException):services.create(d,ana,"","Descrição","Equipamento")
