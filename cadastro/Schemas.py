from ninja import Schema, ModelSchema
from .models import Cadastro
from typing import Dict,List

class UsuarioSaida(Schema):
    id: int
    nome: str
    sobrenome: str
    email: str
    senha: str
    telefone: int
    
class Cadastro(ModelSchema):
   #localidade: List[str]= [] #TODO este e um novo campo que não funcina
   class Config:
       model = Cadastro
       model_fields = "__all__"
       extra = "forbid"

