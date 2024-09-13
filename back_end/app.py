from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from model import Session, Agendamento
from schemas import *
from flask_cors import CORS

info = Info(title="MVP CoPsi", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)
67
# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
agendamento_tag = Tag(name="Agendamento", description="Reserva de sala na CoPsi, lista de reservas efetuadas e cancelamento de reservas")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/agendamento', tags=[agendamento_tag],
          responses={"200": VisualizaAgendamentos})
def add_agendamento(form: RepresentaAgendamento):
    """Adiciona uma nova reserva de sala

    Retorna uma representação dos agendamentos..
    """
    reserva = Agendamento(
        nome=form.nome,
        telefone=form.telefone,
        email=form.email,
        sala=form.sala,
        data_agendamento=form.data_agendamento,
        hora_agendamento=form.hora_agendamento
    )
    try:
        # criando conexão com a base
        session = Session()
        # adicionando agendamento
        session.add(reserva)
        # efetivando o comando de efetivação de novo agendamento
        session.commit()
        return apresenta_agendamento(reserva), 200

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível realizar agendamento :/"
        return {"mesage": error_msg}, 400


@app.get('/agendamentos', tags=[agendamento_tag],
         responses={"200": ListaAgendamentos})
def get_agendamentos():
    """Apresenta todas as reservas de sala com dados do profissinal, data e horário.

    Retorna uma representação da listagem de agendamentos.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    agendamentos = session.query(Agendamento).all()

    if not agendamentos:
        # se não há agendamentos cadastrados
        return {"agendamentos": []}, 200
    else:
        # retorna a representação de agendamento
        print(agendamentos)
        return apresenta_agendamentos(agendamentos), 200



@app.delete('/agendamento', tags=[agendamento_tag],
            responses={"200": DeletaAgendamentos})
def del_agendamento(query: BuscaAgendamento):
    """Deleta uma reserva a partir do nome do profissional que realizou o agendamento

    Retorna uma mensagem de confirmação da remoção.
    """
    agendamento_nome = unquote(unquote(query.nome))
    print(agendamento_nome)
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Agendamento).filter(Agendamento.nome == agendamento_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        return {"mesage": "Agendamento removido", "id": agendamento_nome}
    else:
        # se o agendamento não foi encontrado
        error_msg = "Agendamento não encontrado na base :/"
        return {"mesage": error_msg}, 404
    
    
    