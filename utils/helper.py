"""Gerenciamente de conversoes"""
from datetime import date
from datetime import datetime


def date_para_str(data: date) -> str:
    """Data para str"""
    return data.strftime("%d/%m/%Y")


def str_para_date(data: str) -> date:
    """str para datas"""
    return datetime.strptime(data, "%d/%m/%Y")


def formata_float_str_moeda(valor: float) -> str:
    """moedas para str"""
    return f"R$ {valor:,.2f}"
