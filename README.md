# Vehicle Maintenance Notification System

## Project Overview
A microservices-based system for managing vehicle maintenance notifications and scheduling.

## Project Structure
```
repo/
├── logging_middleware/           # Shared logging utilities
├── notification_app_be/          # Notifications API
│   ├── controllers/              # Request handlers
│   ├── routes/                   # API endpoints
│   ├── services/                 # Business logic
│   └── app.py                    # Application entry point
├── vehicle_maintenance_scheduler/ # Maintenance scheduling API
│   ├── controllers/              # Request handlers
│   ├── routes/                   # API endpoints
│   ├── services/                 # Business logic
│   └── app.py                    # Application entry point
├── notification_system_design.md # System architecture and design
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Services

### Notification App Backend
RESTful API for managing notifications.

**Port:** 5001

**Key Features:**
- Create and manage notifications
- Update notification status
- Retrieve notification history

### Vehicle Maintenance Scheduler
API for scheduling and tracking vehicle maintenance tasks.

**Port:** 5002

**Key Features:**
- Vehicle management
- Maintenance scheduling
- Maintenance history tracking

## Setup

### Prerequisites
- Python 3.8+
- pip

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd repo

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running Services
```bash
# Notification Service
cd notification_app_be
python app.py

# Vehicle Maintenance Scheduler (in a new terminal)
cd vehicle_maintenance_scheduler
python app.py
```

## Documentation
See [notification_system_design.md](notification_system_design.md) for detailed system design and architecture.

## Contributing
(To be defined)

## License
(To be defined)
