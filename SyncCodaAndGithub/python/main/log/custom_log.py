import logging

# Create a custom formatter
class MethodNameFormatter(logging.Formatter):
    def format(self, record):
        record.method_name = record.funcName  # Add the method name to the record
        return super().format(record)