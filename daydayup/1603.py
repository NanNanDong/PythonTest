# 1603. 设计停车系统

class ParkingSystem:
    
    def __init__(self, big: int, medium: int, small: int):
        self.parks = [0] * 3
        _parks = self.parks
        _parks[0] = big
        _parks[1] = medium
        _parks[2] = small

    def addCar(self, carType: int) -> bool:
        realT = carType - 1
        if self.parks[realT] > 0:
            self.parks[realT] -= 1
            return True

        return False

x = ParkingSystem(1, 1, 0)
print(x.addCar(1))
print(x.addCar(2))
print(x.addCar(3))
print(x.addCar(1))



