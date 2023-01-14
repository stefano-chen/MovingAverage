class ExamException(Exception):
    pass


class MovingAverage:
    def __init__(self, size: int):
        if not isinstance(size, int):
            raise ExamException('Type Error')
        if size <= 0:
            raise ExamException('Value Error')
        self.n = size

    def compute(self, data: list):
        if not isinstance(data, list):
            raise ExamException("Not a list")
        if not all(isinstance(item, (int, float)) for item in data):
            raise ExamException("Not a list of numeric values")
        if len(data) == 0:
            raise ExamException("Empty list")
        if self.n > len(data) :
            raise ExamException("Window size too big")

        result = []
        i = 0
        while i + self.n <= len(data):
            s = 0
            for item in data[i: i+self.n]:
                s += item
            result.append(s/self.n)
            i += 1
        return result
