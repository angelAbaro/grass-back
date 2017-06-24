from django.conf.urls import patterns, include, url
from rest_framework import routers
from .views.NaturalPersonView import NaturalPersonViewSet
from .views.UnidadMedidaView import UnidadMedidaViewSet
from .views.ContratoView import ContratoViewSet
from .views.DocumentoView import DocumentoViewSet
from .views.CursoView import CursoViewSet
<<<<<<< HEAD
from views.empresa import EmpresaViewSet
from views.local import LocalViewSet
from views.tipo_cancha import TipoCanchaViewSet
from views.archivo import ArchivoViewSet
from views.cancha import CanchaViewSet
from views.implementos_dep import ImplementoViewSet
from views.catalogo import CatalogoViewSet
from views.persona import PersonaViewSet
from views.reserva import ReservaViewSet
=======

>>>>>>> e219519fb75b28fbb07f83ab06610666f674ad84
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'unidadmedidas', UnidadMedidaViewSet)
router.register(r'naturalpersons', NaturalPersonViewSet)
router.register(r'contratos', ContratoViewSet)
router.register(r'documentos', DocumentoViewSet)
router.register(r'cursos', CursoViewSet)
<<<<<<< HEAD
router.register(r'persona', PersonaViewSet)
router.register(r'reserva', ReservaViewSet)
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tipo-cancha', TipoCanchaViewSet)
router.register(r'empresa', EmpresaViewSet)
router.register(r'local', LocalViewSet)
router.register(r'archivo', ArchivoViewSet)
router.register(r'cancha', CanchaViewSet)
router.register(r'implementos', ImplementoViewSet)
router.register(r'catalogo', CatalogoViewSet)
router.register(r'reserva', ReservaViewSet)
=======

>>>>>>> e219519fb75b28fbb07f83ab06610666f674ad84

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),

)
