from methods.Calculator import Calculator
from methods.median import median
from methods.Mode import Mode
from methods.popstand import popstand
from methods.variance import variance
from CsvReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self):
        d = []
        for row in self.data.data:
            d.append(row['v'])
        self.result = mean(d)
        return self.result

    def sample_mean(self, sample_size):
        self.result = sample_mean(self.data, sample_size)
        return self.result

    def median(self):
        d = []
        for row in self.data.data:
            d.append(row['v'])
        self.result = median(d)
        return self.result

    def mod(self):
        d = []
        for row in self.data.data:
            d.append(row['v'])
        self.result = Mode(d)
        return self.result

    def psd(self):
        d = []
        for row in self.data.data:
            d.append(row['v'])
        self.result = popstand(d)
        return self.result

    def vpp(self):
        d = []
        for row in self.data.data:
            d.append(row['v'])
        self.result = variance(d)
        return self.result
