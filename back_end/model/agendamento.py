from sqlalchemy import Column, String, Integer
from  model import Base


class Agendamento(Base):
    __tablename__ = 'copsi'

    id = Column("pk_copsi", Integer, primary_key=True)
    nome = Column(String(140))
    telefone = Column(String(20))
    email = Column(String(100))
    sala = Column(String(10))
    data_agendamento = Column(String(20))
    hora_agendamento = Column(String(20))
 
    def __init__(self, nome:str, telefone:str, email:str, sala: str, data_agendamento:str, hora_agendamento:str):
        """
        Cria um Agendamento

        Arguments:
            nome: nome do profissional.
            tefefone: telefone do profissional que deseja o agendamento
            email: email do profissional que deseja o agendamento
            sala: sala que o profissional deseja reservar
            data_agendamento: data que o profssional deseja reservar
            hora_agendamento: data que o profssional deseja reservar
        
        """
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.sala = sala
        self.data_agendamento = data_agendamento
        self.hora_agendamento = hora_agendamento
    

