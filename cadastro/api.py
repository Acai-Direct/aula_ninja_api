from ninja import Router
from .Schemas import Cadastro, UsuarioSaida
from .models import Cadastro as ModelCadastro
from django.shortcuts import get_object_or_404

cadastro_router = Router()

@cadastro_router.post("/cadastrouser")
def cadastroUser(request, cadastro: Cadastro):
    usuario = ModelCadastro.objects.create(**cadastro.dict())
    usuario = Cadastro.from_orm(cadastro).dict()
    return usuario

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
