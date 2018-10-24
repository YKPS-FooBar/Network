# Toolkit 404

Build a simple toolkit that supports some basic functions.

## Requirements

- GET `/`: Returns a welcome page
- GET `/time`: Returns current local time (UTC+08:00 in our case) in the format `YYYY/MM/DD HH:MM:SS`
- GET `/weather`: Returns weather information (in any location for any duration of time) in any format
- POST `/add` (with `item` parameter): Stores the value in the `item` key into a grocery list
- GET `/list`: Returns the list of the items in the grocery list in bullet point style
