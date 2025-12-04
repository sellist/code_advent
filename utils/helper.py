from typing import TypeVar, Generic, List, Dict, Tuple

T = TypeVar('T')

class GridDict(Generic[T]):
    """
    A class to represent and manipulate a 2D matrix.

    Attributes:
        coord_dict (dict): A dictionary mapping coordinates to their values in the matrix.
        matrix (list[list[T]]): The 2D matrix.
        len_x (int): The number of columns in the matrix.
        len_y (int): The number of rows in the matrix.
    """

    def __init__(self, matrix: List[List[T]]):
        """
        Initializes the GridDict object with a given matrix.

        Args:
            matrix (list[list[T]]): The 2D matrix.
        """
        self.coord_dict = self.matrix_to_coordinate_dict(matrix)
        self.matrix = matrix
        self.len_x = len(matrix[0])
        self.len_y = len(matrix)

    def __repr__(self) -> str:
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __str__(self) -> str:
        return self.__repr__()

    @staticmethod
    def matrix_to_coordinate_dict(matrix: List[List[T]]) -> Dict[Tuple[int, int], T]:
        """
        Converts a matrix to a dictionary of coordinates.

        Args:
            matrix (list[list[T]]): The 2D matrix.

        Returns:
            dict: A dictionary mapping coordinates to their values in the matrix.
        """
        coord_dict = {}
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                value = matrix[i][j]
                if value != 0:
                    coord_dict[(i, j)] = value
        return coord_dict

    def get_coord_value(self, x: int, y: int) -> T:
        """
        Returns the value at the given coordinates if within bounds.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.

        Returns:
            T: The value at the given coordinates, or None if out of bounds.
        """
        if self.check_in_bounds(x, y):
            return self.coord_dict[(y, x)]

    def check_in_bounds(self, x: int, y: int) -> bool:
        """
        Checks if the given coordinates are within the bounds of the matrix.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.

        Returns:
            bool: True if the coordinates are within bounds, False otherwise.
        """
        return -1 < x < self.len_x and -1 < y < self.len_y

    def find_first_value(self, value: T) -> Tuple[int, int]:
        """
        Finds the first occurrence of a value in the matrix.

        Args:
            value (T): The value to find.

        Returns:
            tuple[int, int]: The coordinates of the first occurrence of the value.
        """
        for n_y, y in enumerate(self.matrix):
            for n_x, x in enumerate(y):
                if x == value:
                    return n_x, n_y

    def find_all_value_coords(self, value: T) -> List[Tuple[int, int]]:
        """
        Finds all occurrences of a value in the matrix.

        Args:
            value (T): The value to find.

        Returns:
            list[tuple[int, int]]: A list of coordinates of all occurrences of the value.
        """
        coords = []
        for n_y, y in enumerate(self.matrix):
            for n_x, x in enumerate(y):
                if x == value:
                    coords.append((n_x, n_y))
        return coords

    @staticmethod
    def get_rectangle_coords(x1: int, y1: int, x2: int, y2: int) -> List[Tuple[int, int]]:
        """
        Gets the coordinates of all squares within a rectangle or square defined by two opposite corners.

        Args:
            x1 (int): The x-coordinate of the first corner.
            y1 (int): The y-coordinate of the first corner.
            x2 (int): The x-coordinate of the opposite corner.
            y2 (int): The y-coordinate of the opposite corner.

        Returns:
            list[tuple[int, int]]: A list of coordinates of all squares within the rectangle or square.
        """
        coords = []
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                coords.append((x, y))
        return coords

    def get_line_values(self, x1: int, y1: int, x2: int, y2: int) -> List[T]:
        """
        Gets all values in a 2D matrix in a line given the beginning and end points.

        Args:
            x1 (int): The x-coordinate of the beginning point.
            y1 (int): The y-coordinate of the beginning point.
            x2 (int): The x-coordinate of the end point.
            y2 (int): The y-coordinate of the end point.

        Returns:
            list[T]: A list of values in the matrix along the line.
        """
        points = []
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            points.append((x1, y1))
            if x1 == x2 and y1 == y2:
                break
            e2 = err * 2
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

        line_values = [self.matrix[y][x] for x, y in points if 0 <= y < len(self.matrix) and 0 <= x < len(self.matrix[0])]

        return line_values

    def set_coord_value(self, x: int, y: int, value: T):
        """
        Sets the value at the given coordinates if within bounds.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
            value (T): The value to set at the coordinates.
        """
        if self.check_in_bounds(x, y):
            self.coord_dict[(y, x)] = value
            self.matrix[y][x] = value


class StringUtils:
    """
    class to represent common algorithms used in string processing, i.e. longest common substring
    """

    @staticmethod
    def longest_duplicate_substring(string: str) -> str | None:
        """
        Args:
            string: string to check for longest substring in

        Returns: found substring if repeated, None if no repeating is found
        """

        def has_duplicate_of_length(length: int) -> str | None:
            if length == 0:
                return None

            base = 256
            mod = 2 ** 32 - 1

            hash_val = 0
            power = 1
            for i in range(length):
                hash_val = (hash_val * base + ord(string[i])) % mod
                if i < length - 1:
                    power = (power * base) % mod

            seen_hashes = {hash_val: 0}

            for i in range(1, len(string) - length + 1):
                hash_val = (hash_val - ord(string[i - 1]) * power) % mod
                hash_val = (hash_val * base + ord(string[i + length - 1])) % mod

                if hash_val in seen_hashes:
                    current_substr = string[i:i + length]
                    prev_start = seen_hashes[hash_val]
                    prev_substr = string[prev_start:prev_start + length]
                    if current_substr == prev_substr:
                        return current_substr

                seen_hashes[hash_val] = i

            return None

        left, right = 0, len(string) - 1
        result = None

        while left <= right:
            mid = (left + right) // 2
            duplicate = has_duplicate_of_length(mid)

            if duplicate is not None:
                result = duplicate
                left = mid + 1
            else:
                right = mid - 1

        return result

