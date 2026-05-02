from logging_middleware.logger import log, log_wrapper
import services.vehicle_service as svc


@log_wrapper
def schedule():
    try:
        log("backend", "info", "controller", "Fetching depots")

        depots = svc.fetch_depots()

        log("backend", "info", "controller", "Fetching vehicles")

        vehicles = svc.fetch_vehicles()

        log("backend", "info", "controller", "Assigning vehicles")

        result = svc.assign_vehicles(vehicles, depots)

        log("backend", "info", "controller", "Returning schedule")

        return {"schedule": result}, 200

    except Exception as e:
        log("backend", "error", "controller", str(e))
        return {"error": "Vehicle scheduling failed"}, 500