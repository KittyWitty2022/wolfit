from app.helpers import pretty_date
from datetime import datetime, timedelta

def test_now():
    assert (pretty_date(datetime.utcnow())) == "just now"

def test_seconds():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=34))) == "34 seconds ago"

