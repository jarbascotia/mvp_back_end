from pydantic import BaseModel
from typing import List
from model.agendamento import Agendamento

class ErrorSchema(BaseModel):
    """ Define como uma mensagem de erro será representada
    """
    mesage: str



class RepresentaAgendamento(BaseModel):
    """ Define como um novo agendamento a ser inserido deve ser representado
    """
    id: int = 1
    nome: str = "Anna Luisa"
    telefone: str = "77999999999"
    email: str = "email@email.com"
    sala: str = "Sala 1"
    data_agendamento: str = "2024-10-30"
    hora_agendamento: str = "10:00"


class BuscaAgendamento(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do agendamento.
    """
    nome: str = 'Digite o nome do Profissional'


class ListaAgendamentos(BaseModel):
    """ Define como uma listagem de agendamentos será retornada.
    """
    agendamentos:List[RepresentaAgendamento]


def apresenta_agendamentos(agendamentos: List[Agendamento]):
    """ Retorna uma representação do agendamento seguindo o schema definido em
        AgendamentoSchemaView.
    """
    result = []
    for reserva in agendamentos:
        result.append({
            "id": reserva.id,
            "nome": reserva.nome,
            "telefone": reserva.telefone,
            "email": reserva.email,
            "sala": reserva.sala,
            "data_agendamento": reserva.data_agendamento,
            "hora_agendamento": reserva.hora_agendamento,
        })

    return {"agendamentos": result}


class VisualizaAgendamentos(BaseModel):
    """ Define como um agendamento será retornado
    """
    id: int = 1
    nome: str = "Anna Luisa"
    telefone: str = "77999999999"
    email: str = "email@email.com"
    sala: str = "Sala 1"
    data_agendamento: str = "2024-10-30"
    hora_agendamento: str = "10:00"



class DeletaAgendamentos(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_agendamento(reserva: Agendamento):
    """ Retorna uma representação dos agendamentos seguindo o schema definido em
        AgendamentoSchemaView.
    """
    return {
        "id": reserva.id,
        "nome": reserva.nome,
        "telefone": reserva.telefone,
        "email": reserva.email,
        "sala": reserva.sala,
        "data_agendamento": reserva.data_agendamento,
        "hora_agendamento": reserva.hora_agendamento,
    }
