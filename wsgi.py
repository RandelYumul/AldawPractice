"""WSGI entry point for production servers.

This file exposes the `app` object so WSGI servers (gunicorn, uwsgi)
can import it as `wsgi:app`.
"""
from app.aldaw_wave import app


if __name__ == '__main__':
    # Local debug run
    app.run(host='0.0.0.0', port=5000, debug=False)
