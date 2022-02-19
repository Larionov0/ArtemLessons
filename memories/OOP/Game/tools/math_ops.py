def distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


def get_vector_length(vector):
    return (vector[0] ** 2 + vector[1] ** 2) ** 0.5


def normalize_victor(vector, needed_length):
    """
    Принимает вектор и длину, к которой нужно привести этот вектор.
    И возвращает вектор с тем же направление, но с нужной длиной.
    """
    d = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
    k = needed_length / d if d != 0 else 0
    return [vector[0] * k, vector[1] * k]
