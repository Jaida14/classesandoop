
class Patient:

    def __init__(self, i, n, a, p, s):
        self.__patient_ID = i
        self.__patient_name = n
        self.__patient_address = a
        self.__patient_phone = p
        self.__patient_status = s

    def get_patientID(self):  # displays the information
        return self.__patient_ID

    def get_patientName(self):  # displays the information
        return self.__patient_name

    def get_patientAddress(self):  # displays the information
        return self.__patient_address

    def get_patientPhone(self):  # displays the information
        return self.__patient_phone

    def get_patientStatus(self):  # displays the information
        return self.__patient_status
