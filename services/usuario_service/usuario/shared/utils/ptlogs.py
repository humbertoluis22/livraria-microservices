import functools
import logging
from re import sub
from time import perf_counter


def config_logger(logger: logging.Logger) -> None:
    # StreamHandler (logs para o terminal)
    novo_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    novo_handler.setFormatter(formatter)
    logger.addHandler(novo_handler)
    logger.propagate = False


# 🧠 Nome do projeto baseado na pasta onde o script está sendo executado
project = 'fast-agente-virtual'
logger = logging.getLogger(project)
logger.setLevel(logging.DEBUG)
config_logger(logger)


# 🧩 Decorador para logging de funções individuais
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [
            sub(r'\d{11,19}', '***', str(repr(a)).replace('\n', '')[:20])
            for a in args
        ]
        kwargs_repr = [
            k + '=' + sub(r'\d{11,19}', '***', str(v).replace('\n', '')[:20])
            for k, v in kwargs.items()
        ]
        signature = ', '.join(args_repr + kwargs_repr)

        logger.warning(f'{func.__name__} ( {signature} )')

        try:
            result = func(*args, **kwargs)
            return result
        except Exception as ex:
            logger.exception(
                f'Exception raised in {func.__name__}. exception: {str(ex)}'
            )
            raise ex

    return wrapper


# 🔐 Função para sanitizar kwargs com dados sensíveis
def sanitize_kwargs(kwargs: dict) -> dict:
    """Filtra parâmetros sensíveis, mascarando valores."""
    kwargs_repr = {
        k: sub(r'\d{11,19}', '***', str(v).replace('\n', '')[:20])
        for k, v in kwargs.items()
    }
    return {
        k: ('****' if k in {'user', 'password'} else v)
        for k, v in kwargs_repr.items()
    }


# 🏷️ Decorador para aplicar logging em todos os métodos de uma classe
def log_methods(cls):
    """Adiciona logging a todos os métodos da classe, filtrando credenciais."""
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not attr_name.endswith('__'):

            def wrapper(method):
                def logged_method(*args, **kwargs):
                    config_logger(logger)

                    sanitized_kwargs = sanitize_kwargs(kwargs)
                    logger.debug(
                        f'Chamando {cls.__name__}.{method.__name__} '
                        + f'com {args=}, kwargs={sanitized_kwargs}'
                    )
                    inicio = perf_counter()
                    try:
                        resul = method(*args, **kwargs)
                    except Exception as ex:
                        tempo_total = perf_counter() - inicio
                        logger.error(
                            f'Exceção no método: {cls.__name__}'
                            f'.{method.__name__} '
                            f'Tempo Execução: {tempo_total:.3f}s ex: {ex}'
                        )
                        raise
                    tempo_total = perf_counter() - inicio
                    logger.debug(
                        f'Finalizada: {cls.__name__}.{method.__name__} '
                        f'Tempo Execução: {tempo_total:.3f}s '
                        f'Resultado: {resul}'
                    )
                    return resul

                return logged_method

            setattr(cls, attr_name, wrapper(attr_value))
    return cls
