import ProcedureClass as procedureC
import PatientClass as pc


def main():

    patient_1 = pc.Patient(
        1, 'Matt Jones', '123 Main st, Waco TX 76706', '254-555-7415', True)

    # did not take arguments so try in parenthesis
    '''
    patient_1.__patient_ID = 1
    patient_1.__patient_name = 'Matt Jones'
    patient_1.__patient_address = '123 Main st, Waco TX 76706'
    patient_1.__patient_phone = '254-555-7415'
    patient_1.__patient_status = True
    '''
    procedure_completed1 = procedureC.Procedure(
        'Physical Exam', '2/15/2022', 'Dr. Irvine', float(250), 1)

    '''
    procedure_completed1.__procedure_name = 'Physical Exam'
    procedure_completed1.__procedure_date = '2/15/2022'
    procedure_completed1.__pract_name = 'Dr. Irvine'
    procedure_completed1.__procedure_charge = 250
    procedure_completed1.__patient_ID = 1
    '''

    procedure_completed2 = procedureC.Procedure(
        'MRI', '2/15/2022', 'Dr. Hamilton', float(1500), 1)

    '''
    procedure_completed2.__procedure_name = 'MRI'
    procedure_completed2.__procedure_date = '2/15/2022'
    procedure_completed2.__pract_name = 'Dr. Hamilton'
    procedure_completed2.__procedure_charge = 1500
    procedure_completed2.__patient_ID = 1
    '''

    procedure_completed3 = procedureC.Procedure(
        'CT Scan', '2/17/2022', 'Dr. Drey', float(1200), 2)

    '''
    procedure_completed3.__procedure_name = 'CT Scan'
    procedure_completed3.__procedure_date = '2/17/2022'
    procedure_completed3.__pract_name = 'Dr. Drey'
    procedure_completed3.__procedure_charge = 1200
    procedure_completed3.__patient_ID = 2
    '''

    total_charge = 0

    print(f"*** Patient Bill ***")
    print(f"Name: {patient_1._Patient__patient_name}\nAddress: {patient_1._Patient__patient_address}\nPhone: {patient_1._Patient__patient_phone}")
    # above: call class name first and then call the attribute how you named with double underscore
    print(f" ")

    for procedure in procedureC.Procedure.proceduresComp:
        if procedure._Procedure__patient_ID == 1:
            print(
                f"Procedure: {procedure._Procedure__procedure_name}\nDate: {procedure._Procedure__procedure_date}\nPractioner: {procedure._Procedure__pract_name}\nCharge: ${procedure._Procedure__procedure_charge:7,.2f}")
            print(f" ")

            total_charge += procedure._Procedure__procedure_charge
    if patient_1._Patient__patient_status == True:
        total_charge -= (.40*total_charge)
    print(f"Total Charges: ${total_charge:7,.2f} ")


main()
