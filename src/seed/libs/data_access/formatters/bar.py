from seed.libs.data_access.formatters.line import LineFormatter


class BarFormatter(LineFormatter):
    def __init__(self, *args, **kwargs):
        super(BarFormatter, self).__init__(*args, **kwargs)