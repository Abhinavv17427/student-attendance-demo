from attendance import attendance_percentage


def test_attendance():
    assert attendance_percentage(8, 10) == 80


def test_zero_classes():
    assert attendance_percentage(0, 0) == 0
