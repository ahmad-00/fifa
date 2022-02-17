class CurrencyToInt:
    def __call__(self, value):
        if not value:
            return 0
        try:
            ext = value[:-1]
            raw_value = value[1:-1]
            if ext == "M":
                return int(float(raw_value) * 1000000)
            elif ext == "K":
                return int(float(raw_value) * 1000)
            else:
                return 0
        except:
            return 0
