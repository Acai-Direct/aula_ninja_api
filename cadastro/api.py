from ninja import Router
from .Schemas import Cadastro, UsuarioSaida
from .models import Cadastro as ModelCadastro
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

cadastro_router = Router()

@cadastro_router.post("/cadastrouser", response={200: dict, 400: dict, 500: dict})
def cadastroUser(request, cadastro: Cadastro):
    # usuario = ModelCadastro.objects.create(**cadastro.dict())
    # usuario = Cadastro.from_orm(cadastro).dict()
    cadastro = ModelCadastro(**cadastro.dict())
    cadastro.senha = make_password(cadastro.senha)
    try:
        cadastro.full_clean()
        cadastro.save()
    except ValidationError as e:
        return 400, {"errors": e.message_dict}
    except Exception as e:
        return 500, {"errors":"Erro interno do servidor, contate um administrador"}    
    
    return {"success":True}

get_usuario_router = Router()

@get_usuario_router.get("/getUsuario/{cadastro_id}", response= UsuarioSaida)
def get_usuario(request, cadastro_id: int):
    usuario = get_object_or_404(ModelCadastro, id = cadastro_id)
    return usuario

all_usuario_router = Router()

@all_usuario_router.get("/allUsuario/{cadastro_all}", response= list[UsuarioSaida])
def all_usuario(request, cadastro_all: str):
    if cadastro_all == "all" or cadastro_all =="todos":
        usuario = ModelCadastro.objects.all()
    return usuario
    
att_usuario_router = Router()

@att_usuario_router.put("/attUsuario/{cadastro_id}")
def attUsuario(request, cadastro_id: int, cadastro_data: UsuarioSaida):
    cadastro = get_object_or_404(ModelCadastro, id = cadastro_id)
    for attr, value in cadastro_data.dict().items():
        setattr(cadastro, attr, value)
    cadastro_data.dict(exclude_unset= True).items()
    cadastro.save()
    return {"success": True}

dell_usuario_router = Router()

@dell_usuario_router.delete("/dellUsuario/{cadastro_id}")
def delete_usuario(request, cadastro_id: int):
    cadastro = get_object_or_404(ModelCadastro, id = cadastro_id)
    cadastro.delete()
    return {"success": True}
