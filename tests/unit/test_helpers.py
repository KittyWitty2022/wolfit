from app.helpers import pretty_date
from datetime import datetime, timedelta

def test_now():
    assert (pretty_date(datetime.utcnow())) == "just now"

def test_about_now():
    assert (pretty_date(datetime.utcnow() - timedelta(days=-1))) == "just about now"

def test_seconds():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=34))) == "34 seconds ago"

def test_minute():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=93))) == "a minute ago"

def test_minutes():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=2520))) == "42 minutes ago"

def test_hour():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=4560))) == "an hour ago"

def test_hours():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=57600))) == "16 hours ago"

def test_day_yesterday():
    assert (pretty_date(datetime.utcnow() - timedelta(days=1))) == "Yesterday"

def test_day_days():
    assert (pretty_date(datetime.utcnow() - timedelta(days=3))) == "3 days ago"

def test_weeks():
    assert (pretty_date(datetime.utcnow() - timedelta(days=17))) == "2 weeks ago"

def test_months():
    assert (pretty_date(datetime.utcnow() - timedelta(days=103))) == "3 months ago"

def test_years():
    assert (pretty_date(datetime.utcnow() - timedelta(days=375))) == "1 years ago"



