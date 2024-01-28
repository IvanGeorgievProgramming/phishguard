import time

from app.services.data_management.delete_json_file import delete_json_file

def remove_expired_routes(temporary_routes):
    """
    Summary: 
        Remove expired routes.

    Description: 
        Get the current time.\n
        Get the routes that have expired.\n
        Delete the json files of the routes that have expired.\n
        Remove the routes that have expired from the temporary_routes dictionary.\n

    Arguments: 
        temporary_routes (dict): The temporary_routes dictionary.

    Returns: 
        None: This function does not return anything.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console.
    """
    try:
        current_time = time.time()
        expired_routes = [route for route, info in temporary_routes.items() if info["expiry"] < current_time]
        for route in expired_routes:
            delete_json_file(route)
            temporary_routes.pop(route, None)
    except Exception as e:
        print(f"Error removing expired routes: {e}")