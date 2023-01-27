from app.helpers import pretty_date
from datetime import datetime, timedelta

def test_now():
    assert (pretty_date(datetime.utcnow())) == "just now"

def test_seconds():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=34))) == "34 seconds ago"

def test_minute():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=93))) == "a minute ago"

def test_minutes():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=2520))) == "42 minutes ago"

def test_hour():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=4560))) == "an hour ago"
