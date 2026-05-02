from logging_middleware.logger import log, log_wrapper
import services.notification_service as svc

@log_wrapper
def get_notifications():
    try:
        log("backend", "info", "controller", "Fetching notifications from API")

        data = svc.fetch_notifications()

        log("backend", "info", "controller", "Processing notifications")

        result = svc.process_notifications(data)

        log("backend", "info", "controller", "Returning top 5 notifications")

        return {"notifications": result}, 200

    except Exception as e:
        log("backend", "error", "controller", str(e))
        return {"error": "Failed to fetch notifications"}, 500