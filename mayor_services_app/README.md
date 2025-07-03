# Mayor Services Event Staffing App

This is a simple Flask-based API to connect contractors with clients for event staffing needs.

## Setup

1. Create a virtual environment (optional but recommended).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```

The API will be available at `http://localhost:5000` by default.

## Endpoints

- `GET /contractors` - List all contractors
- `POST /contractors` - Add a contractor. Provide JSON with contractor details.
- `GET /clients` - List all clients
- `POST /clients` - Add a client. Provide JSON with client details.
- `POST /assign` - Assign a contractor to a client/event. Provide JSON with assignment info.
- `GET /assignments` - List all assignments

All data is stored in memory and will be lost when the app stops running. This is intended as a starting point for further development.
