from pytracov import module1

def test_add():
    assert module1.add_numbers(0,0) == 0
    assert module1.add_numbers(1,2) == 3
    
def test_mult():
    assert module1.multiply_numbers(0,0) == 0
    assert module1.multiply_numbers(1,2) == 2
    
    
    