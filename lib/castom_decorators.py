import functools
from os import sep as os_separator
from datetime import datetime

def logger_decorator(path_to_logs=''):

    def actual_decorator(tracked_function):

        @functools.wraps(tracked_function)
        def wrapper(*args, **kwargs):    
            logger_dict = dict()
            call_date = datetime.today().strftime('%H:%M:%S-%d.%m.%Y')
            tracked_funcktion_name = tracked_function.__name__
            result = tracked_function(*args, **kwargs)

            logger_dict['date_of_call'] = call_date
            logger_dict['function_name'] = tracked_funcktion_name
            logger_dict['function_args'] = args
            logger_dict['function_kwargs'] = kwargs
            logger_dict['function_result'] = result

            lags_path = f"logs" if str(path_to_logs) == '' else str(path_to_logs)

            with open(f'{lags_path}{os_separator}logs.txt','a+', encoding='utf-8') as log:
                for key,val in logger_dict.items():
                    log.write(f'{key}: "{val}"\n')
                log.write(f"\n")    

            print(logger_dict)

            return tracked_function(*args, **kwargs)

        return wrapper

    return actual_decorator