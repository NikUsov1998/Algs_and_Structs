class Point:
    def __init__(self, x: float, y: float) -> None:
        self.__x: float = x
        self.__y: float = y

    def __str__(self) -> str:
        return f"Point[x={self.__x}, y={self.__y}]"

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, new_x: float) -> None:
        self.__x = new_x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, new_y:float) -> None:
        self.__y = new_y
