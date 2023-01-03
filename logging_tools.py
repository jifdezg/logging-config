import logging

# Implementa una versión propia de la clase TimedRotatingFileHandler que permite especificar un namer,
# ya que el archivo de configuración no permite especificarlo
class MyTimedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):
    def __init__(self, filename, when='midnight', interval=1):
        super().__init__(filename=filename, when=when, interval=interval)
        self.namer = rotator_namer

def rotator_namer(filename):
    return filename.replace("current_log.log.", "") + ".log"

# Filtra y devuelve únicamente los registros con nivel de severidad 20 (INFO)
class InfoOnly(logging.Filter):
    def filter(self, record):
        return record.levelno == 20

# Filtra y devuelve únicamente los registros con nivel de severidad 30 (WARNING)
class WarningOnly(logging.Filter):
    def filter(self, record):
        return record.levelno == 30