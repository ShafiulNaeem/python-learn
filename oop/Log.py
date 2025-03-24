import logging
class Log:
   
    def __init__(self, filename):
        self.filename = filename
        logging.basicConfig(filename=filename, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
   
    def log(self, message):
        logging.debug(message)
   
    def read(self):
        with open(self.filename) as file:
            return file.read()

    def __repr__(self):
        return self.filename
    
    def logger(func):
        def log_func(*args, **kwargs):
            logging.info('Running "{}" with arguments {}'.format(func.__name__, args, kwargs))
            return func(*args, **kwargs)
        return log_func
    
