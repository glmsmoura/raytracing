from raytracing.vectors import Vector


v1 = Vector(-1, 2, 2)
v2 = Vector(1, 1, 1)


def test_eq():
    assert str(v1) == str(Vector(-1, 2, 2))

    assert str(v2) == str(Vector(1, 1, 1))
 
def test_inner_product():
    assert v1.inner_product(v1) == 9
    assert v2.inner_product(v2) == 3
    assert v1.inner_product(v2) == 3
    assert v2.inner_product(v1) == 3

def test_module():
    assert v1.module() == 3
    
    assert v2.module() == 3**0.5

def test_normed():
    assert (v1.normed().x, v1.normed().y, v1.normed().z) == (-1/3, 2/3, 2/3)
    assert str(v1.normed()) == str(Vector(-1/3, 2/3, 2/3))

    assert str(v2.normed()) == str(Vector((1/(3**0.5)), (1/(3**0.5)), (1/(3**0.5))))
            
  
def test_mul():
    assert str(v1 * 3) == str(Vector(-3, 6, 6))
    assert str(v2 * 5) == str(Vector(5, 5, 5))

    assert str(v1 - v2) == str((v2 - v1) * -1)
    assert str(-1 * (v1 - v2)) == str((v1 - v2) * -1)

def test_div():
    assert str(v1 / 3) == str(Vector(-1/3, 2/3, 2/3))
    assert str(v2 / 5) == str(Vector(1/5, 1/5, 1/5))

    assert str(v1 - v2) == str((v2 - v1) / -1)
    assert str(-1 / (v1 - v2)) == str((v1 - v2) / -1)
    assert str(-5 / (v2 - v1)) != str((v2 - v1) / -5)

def test_add():
    assert str(v1 + v2) == str(Vector(0, 3, 3))

def test_sub():
    assert str(v1 - v2) == str(Vector(-2, 1, 1))
    assert str(v2 - v1) == str(Vector(2, -1, -1))
 
  
