from attendance import is_late

def test_boundary():
    assert is_late("09:09") == False, "9 минут не должно быть опозданием"
    assert is_late("09:10") == True, "10 минут должно быть опозданием"
    print("Тест точной границы пройден успешно!")

if __name__ == "__main__":
    test_boundary()