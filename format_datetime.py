from datetime import datetime, timedelta, timezone

def get_formated_datetime(item):
    
    try:
        # Tenta converter a data e hora completa
        data_obj = datetime.strptime(item, '%I:%M %p ET (%m/%d/%Y)')
    except ValueError:
        # Se falhar, tenta converter apenas a hora e o período (AM/PM)
        data_obj = datetime.strptime(item, '%I:%M %p ET')
    
    # Define o fuso horário para Eastern Time (ET)
    fuso_horario_et = timezone(timedelta(hours=-5))  # Eastern Time (ET) tem um deslocamento de -5 horas em relação ao UTC
    
    # Aplica o fuso horário
    data_obj = data_obj.replace(tzinfo=fuso_horario_et)
    
    # Verifica se a data está presente ou não
    if data_obj.year == 1:
        # Se a data estiver ausente, retorna apenas a hora formatada
        return data_obj.strftime('%I:%M %p ET')
    else:
        # Caso contrário, retorna a data e a hora formatadas
        return data_obj.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S%z')