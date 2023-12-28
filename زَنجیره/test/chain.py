class Chain:
    def __init__(self, value=None):
        self.values = [value] if value is not None else []

    def __call__(self, next_value):
        for item in self.values:
            if item is None or next_value is None:
                raise Exception("invalid operation")
            elif isinstance(self.values, bool) or isinstance(next_value, bool):
                raise Exception("invalid operation")
            elif isinstance(next_value, (int, float)) and isinstance(item, (int, float)):
                self.values.append(next_value)
                break
            elif isinstance(next_value, str) and isinstance(item, str):
                self.values.append(next_value)
                break
            else:
                raise Exception("invalid operation")
        if next_value is None:
            raise Exception("invalid operation")
        return self

    def __eq__(self, other):
        if any(isinstance(item, (int, float)) for item in self.values):
            return sum(self.values) == other
        elif any(isinstance(item, str) for item in self.values):
            return ' '.join(map(str, self.values)) == other
        else:
            raise Exception("invalid operation")

    def __repr__(self):
        if any(isinstance(item, bool) for item in self.values):
            raise Exception("invalid operation")
        elif any(isinstance(item, (int, float)) for item in self.values):
            if len(self.values) > 1:
                if sum(self.values) % 1 == 0:
                    return f"{int(sum(self.values))}"
                else:
                    return f"{sum(self.values)}"
            else:
                return f"{self.values[0]}"

        elif any(isinstance(item, str) for item in self.values):
            return ' '.join(map(str, self.values))
        else:
            raise Exception("invalid operation")

Chain('Ali')('Safinal')('is')('the')('best.')