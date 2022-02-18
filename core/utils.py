class CurrencyToInt:
    def __call__(self, value):
        if not value:
            return 0
        try:
            ext = value[-1]
            raw_value = value[1:-1]
            if ext == "M":
                return int(float(raw_value) * 1000000)
            elif ext == "K":
                return int(float(raw_value) * 1000)
            else:
                return 0
        except:
            return 0


class PositionCategory:
    def __call__(self, value):
        if not value:
            return ''

        if value == 'GK':
            return 'GK'
        elif value in ['LB', 'RB', 'LWB', 'RWB']:
            return 'FB'
        elif value in ['CB', 'LCB', 'RCB', 'CDM', 'LDM', 'RDM', 'CM', 'LCM', 'RCM', 'LM', 'RM']:
            return 'HB'
        elif value in ['CAM', 'LAM', 'RAM', 'LWF', 'RWF', 'CF', 'LCF', 'RCF']:
            return 'FW'
        else:
            return ''
