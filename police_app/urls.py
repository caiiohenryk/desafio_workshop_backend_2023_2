from django.urls import path
from .views import PessoaListCreate, OcorrenciaListCreate
from .views import PessoaRUD, OcorrenciaRUD

# URL's do codigo, onde estarão alocadas as fichas
urlpatterns = [
    path('pessoa', PessoaListCreate.as_view(), name="Create-Pessoa-List"),
    path('pessoa/<int:pk>/', PessoaRUD.as_view(), name='pessoa-Details'),
    path('ocorrencia', OcorrenciaListCreate.as_view(), name="Create-Ocorrency-List"),
    path('ocorrencia/<int:pk>/', OcorrenciaRUD.as_view(), name='ocorrency-Details'),
    ]