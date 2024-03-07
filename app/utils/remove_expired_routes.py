import time

from app.services.data_management.delete_json_file import delete_json_file

def remove_expired_routes(temporary_routes):
    try:
        current_time = time.time()
        expired_routes = [route for route, info in temporary_routes.items() if info["expiry"] < current_time]
        for route in expired_routes:
            delete_json_file(route)
            temporary_routes.pop(route, None)
    except Exception as e:
        print(f"Error removing expired routes: {e}")
