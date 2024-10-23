from ninja import Router
from django.http import JsonResponse
from .Schemas import Cadastro, UsuarioSaida
from .models import Cadastro as ModelCadastro
from django.shortcuts import get_object_or_404

cadastro_router = Router()

@cadastro_router.post("/cadastrouser")
def cadastroUser(request, cadastro: Cadastro):
    usuario = ModelCadastro.objects.create(**cadastro.dict())
    usuario = Cadastro.from_orm(cadastro).dict()
    return usuario

get_usuario_router =Router()

@get_usuario_router.get("/getUsuario/{cadastro_id}", response= UsuarioSaida)
def get_usuario(request, cadastro_id: int):
    usuario = get_object_or_404(ModelCadastro, id = cadastro_id)
    return usuario

att_usuario_router = Router()
@att_usuario_router.put("/attUsuario/{cadastro_id}")
def attUsuario(request, cadastro_id: int, cadastro_data: UsuarioSaida):
    cadastro = get_object_or_404(ModelCadastro, id = cadastro_id)
    for attr, value in cadastro_data.dict().items():
        setattr(cadastro, attr, value)
    cadastro.save()
    return {"success": True}
    