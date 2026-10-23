from src.log_analysis import parse_log_line

def test_parses_valid_line():
    result = parse_log_line('192.0.2.1 - - [23/Oct/2026:09:01:00 +0000] "GET /docs HTTP/1.1" 200 512')
    assert result == ("/docs", 200, 512)

def test_handles_dash_size():
    result = parse_log_line('192.0.2.1 - - [23/Oct/2026:09:01:00 +0000] "GET / HTTP/1.1" 304 -')
    assert result == ("/", 304, 0)

def test_rejects_malformed_line():
    assert parse_log_line("this is not a server log") is None
