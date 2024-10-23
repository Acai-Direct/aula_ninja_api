from ninja import NinjaAPI
from cadastro.api import cadastro_router
from cadastro.api import get_usuario_router
from cadastro.api import att_usuario_router, dell_usuario_router


api = NinjaAPI()

api.add_router("/cadastro", cadastro_router)
api.add_router("/getUsuario", get_usuario_router)
api.add_router("/attUsuario", att_usuario_router)
api.add_router("/dellUsuario", dell_usuario_router)