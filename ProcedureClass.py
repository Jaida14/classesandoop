import PatientClass as pc


class Procedure:

    proceduresComp= []

    def __init__(self, n, d, p, c, i):
        self.__procedure_name = n
        self.__procedure_date = d
        self.__pract_name = p
        self.__procedure_charge = float(c)
        self.__patient_ID = i
        # class name comes first bc it's under the class domain, lec notes
        Procedure.proceduresComp.append(self)

    def get_patientID(self):  # displays the information
        return self.__patient_ID

    def get_procedureName(self):  # displays the information
        return self.__procedure_name

    def get_procedureDate(self):  # displays the information
        return self.__procedure_date

    def get_practName(self):  # displays the information
        return self.__pract_name

    def get_procedureCharge(self):  # displays the information
        return self.__procedure_charge
