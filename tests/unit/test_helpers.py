from app.helpers import pretty_date
from datetime import datetime, timedelta

def test_now():
    assert (pretty_date(datetime.utcnow())) == "just now"


