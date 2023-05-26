from colorama import Fore
import colorama

colorama.init()

def main():
    systolic = int(input("Enter systolic blood pressure (mmHg): "))
    diastolic = int(input("Enter diastolic blood pressure (mmHg): "))
    bp = get_blood_pressure(systolic, diastolic)
    if bp:
        systolic, diastolic = bp
        classification = classify_blood_pressure(systolic, diastolic)
        pulse = int(input("Enter heart rate in beats per minute: "))
        pulse_pressure = calculate_pulse_pressure(systolic, diastolic)
        if pulse_pressure > 60 or pulse_pressure < 30:
            print(Fore.RED + "You may need to see a cardiologist for further evaluation.")
        if check_tachycardia(pulse):
            print(Fore.RED + "Probably tachycardia.")
        if check_bradycardia(pulse):
            print(Fore.RED + "Probably bradycardia.")
        print("Blood pressure classification:", get_classification_color(classification))


def get_blood_pressure(systolic, diastolic):
    if systolic <= 0 or diastolic <= 0:
        print("Blood pressure should be a positive number.")
    elif diastolic > systolic:
        print("Diastolic blood pressure should not be higher than systolic blood pressure.")
    else:
        return systolic, diastolic


def classify_blood_pressure(systolic, diastolic):
    if systolic < 90 or diastolic < 60:
        return "Probably hypotension"
    elif systolic < 120 and diastolic < 80:
        return "normal"
    elif systolic < 130 and diastolic < 85:
        return "normal or prehypertension"
    elif systolic < 140 or diastolic < 90:
        return "Probably hypertension stage 1"
    elif systolic < 160 or diastolic < 100:
        return "Probably hypertension stage 2"
    else:
        return "Probably hypertension stage 3"


def check_tachycardia(pulse):
    if pulse >= 100:
        return True
    else:
        return False


def check_bradycardia(pulse):
    if pulse <= 60:
        return True
def calculate_pulse_pressure(systolic, diastolic):
    return systolic - diastolic


def get_classification_color(classification):
    if classification == "Probably hypotension":
        return Fore.RED + classification
    elif classification == "normal":
        return Fore.GREEN + classification
    elif classification == "normal or prehypertension":
        return Fore.YELLOW + classification
    elif classification in ("Probably hypertension stage 1", "Probably hypertension stage 2", "Probably hypertension stage 3"):
        return Fore.RED + classification


if __name__ == "__main__":
    main()
