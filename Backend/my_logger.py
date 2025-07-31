import logging

def my_log(name,level=logging.DEBUG,log_file="server.log"):
    my_logger=logging.getLogger(name)
    my_logger.setLevel(level)
    file_handler=logging.FileHandler(log_file)
    formatter=logging.Formatter("%(asctime)s - %(name)s -%(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    my_logger.addHandler(file_handler)
    return my_logger


























