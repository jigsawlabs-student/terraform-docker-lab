

from app import create_app, db
from app.models import Position, Scraping
from app.settings import db_conn
from app.setup import seed_positions_from_csv, seed_scrapings_from_csv

app = create_app(db_conn)

@app.cli.command("init-db")
def init_db_command():
    """Create database tables and seed data."""
    db.create_all()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Position': Position, 'Scraping': Scraping}

