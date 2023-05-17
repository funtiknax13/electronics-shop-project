class InstantiateCSVError(Exception):

    def __init__(self, file_name=""):
        self.message = f"Файл {file_name} поврежден"

    def __str__(self):
        return self.message
