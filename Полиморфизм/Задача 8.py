class Person:
    def __init__(self, name, patronymic, surname, phones):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.phones = phones

    def get_phone(self):
        return self.phones.get('private')

    def get_name(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    def get_work_phone(self):
        return self.phones.get('work')

    def get_sms_text(self):
        return f"Уважаемый {self.name} {self.patronymic}! Примите участие в нашем беспроигрышном конкурсе для физических лиц"


class Company:
    def __init__(self, name, company_type, phones, *employees):
        self.name = name
        self.company_type = company_type
        self.phones = phones
        self.employees = employees

    def get_phone(self):
        if 'contact' in self.phones:
            return self.phones['contact']
        for employee in self.employees:
            work_phone = employee.get_work_phone()
            if work_phone is not None:
                return work_phone
        return None

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return f"Для компании {self.name} есть супер предложение! Примите участие в нашем беспроигрышном конкурсе для {self.company_type}"


def send_sms(*recipients):
    for recipient in recipients:
        phone = recipient.get_phone()
        if phone is not None:
            print(f"Отправлено СМС на номер {phone} с текстом: {recipient.get_sms_text()}")
        else:
            print(f"Не удалось отправить сообщение абоненту: {recipient.get_name()}")


person1 = Person("Степан", "Петрович", "Джобсов", {"private": 555})
person2 = Person("Боря", "Иванович", "Гейтсов", {"private": 777, "work": 888})
person3 = Person("Семен", "Робертович", "Возняцкий", {"work": 789})
person4 = Person("Леонид", "Арсенович", "Торвальдсон", {})
company1 = Company("Яблочный комбинат", "ООО", {"contact": 111}, person1, person3)
company2 = Company("ПластОкно", "АО", {"non_contact": 222}, person2)
company3 = Company("Пингвинья ферма", "Ltd", {"non_contact": 333}, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)