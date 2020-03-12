class StudentFileReader:
    def __init__(self, input_source):
        self._input_source = input_source
        self._input_file = None

    def open(self):
        self._input_file = open(self._input_source, "r")

    def close(self):
        self._input_file.close()
        self._input_file = None

    def fetch_all(self):
        records = list()
        student = self.fetch_record()
        while student is not None:
            records.append(student)
            student = self.fetch_record()
        return records

    def fetch_record(self):
        line = self._input_file.readline()
        if line == "":
            return None

        student = StudentRecord()
        student.id = int(line)
        student.first_name = self._input_file.readline().rstrip()
        student.last_name = self._input_file.readline().rstrip()
        student.class_code = int(self._input_file.readline().rstrip())
        student.gpa = float(self._input_file.readline().rstrip())
        return student


class StudentRecord:
    def __init__(self):
        self.id = 0
        self.first_name = None
        self.last_name = None
        self.class_code = 0
        self.gpa = 0.0