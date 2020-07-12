import csv
import shutil
from tempfile import NamedTemporaryFile


class Academy:
    def view_course(self, filename):
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            len = 0
            for row in csv_reader:
                if len == 0:
                    len += 1
                    continue
                print(f'Course: {row[0]} Fee: {row[1]}')
        print("!!!You can pay course fee in two installment of Rs.10000 each!!!!")

    def all_student_info(self, filename):
        with open(filename, mode='r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            len = 0
            for row in csv_reader:
                if len == 0:
                    len += 1
                    continue
                else:
                    print(f'ID: {row[0]} \t Name: {row[1]}\t Address: {row[2]}\tCourse: {row[3]}\t Payment done:\
                     {row[4]} \t Amount Due: {row[5]}\t Graduated: {row[6]} ')

    def individual_student_info(self, filename, s_id):
        with open(filename, mode='r') as file:
            csv_reader = csv.DictReader(file, delimiter=',')
            for row in csv_reader:
                if int(row["id"]) == s_id:
                    print(f'ID: {row["id"]} \t Name: {row["name"]}\t Address: {row["address"]}\tCourse: {row["course"]}'
                          f'\t Payment done: {row["diposited"]} \t Amount Due: {row["due"]}. ')

    def add_student(self, filename):
        info_lst = []
        with open(filename, mode='r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            Rows = list(csv_reader)
            new_id = len(Rows) + 1
        with open(filename, mode='a+') as add:
            csv_writer = csv.writer(add)
            info_lst.append(new_id)
            info_lst.append(input("Enter your name:"))
            info_lst.append(input("Enter your address:"))
            info_lst.append((input("Enter Course you want to learn:")))
            info_lst.append(int(input("Enter payment amount:")))
            info_lst.append(20000 - info_lst[-1])
            info_lst.append(False)
            csv_writer.writerow(info_lst)

    def deposit(self, filename, amount, s_id, ):
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        fieldnames = ['id', 'name', 'address', 'course', 'diposited', 'due', 'Is_Graduated']
        with open(filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
            for row in reader:
                if row['id'] == str(s_id):
                    row['diposited'] = int(row['diposited']) + amount
                    row['due'] = int(row['due']) - amount
                    writer.writerow(
                        {"id": row["id"], 'name': row['name'], 'address': row['address'], 'course': row['course'],
                         'diposited': row["diposited"], 'due': int(row["diposited"]),
                         'Is_Graduated': row['Is_Graduated']})
                else:
                    writer.writerow({"id": row["id"], 'name': row['name'],
                                     'address': row['address'], 'course': row['course'],
                                     'diposited': row['diposited'], 'due': row['due'],
                                     'Is_Graduated': row['Is_Graduated']})
            shutil.move(tempfile.name, filename)

    def update(self, filename, s_id, change_column, value):
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        fieldnames = ['id', 'name', 'address', 'course', 'diposited', 'due', 'Is_Graduated']
        with open(filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
            for row in reader:
                if str(s_id) == row['id']:
                    for field in row:
                        if change_column == field:
                            row[field] = value
                    writer.writerow({"id": row["id"], 'name': row['name'],
                                     'address': row['address'], 'course': row['course'],
                                     'diposited': row['diposited'], 'due': row['due'],
                                     'Is_Graduated': row['Is_Graduated']})

                else:
                    writer.writerow({"id": row["id"], 'name': row['name'],
                                     'address': row['address'], 'course': row['course'],
                                     'diposited': row['diposited'], 'due': row['due'],
                                     'Is_Graduated': row['Is_Graduated']})
            shutil.move(tempfile.name, filename)
            print("!!!Successfully updated information!!!!")

    def delete(self, filename, id):
        self.filename = filename
        lines = list()
        with open(filename, 'r') as readfile:
            reader = csv.DictReader(readfile)
            for row in reader:
                lines.append(row)
                if int(row['id']) == id:
                    lines.remove(row)
        keys = lines[0].keys()
        print(list(keys))
        with open(filename, 'w') as writeFile:
            writer = csv.DictWriter(writeFile, keys)
            writer.writeheader()
            writer.writerows(lines)

        print("Successfully removed")

    def refund(self, filename, s_id):
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if bool(row["Is_Graduated"]) is True and int(row["due"]) == 0 and int(row['id']) == s_id:
                    print("You have successfully graduated form {} course and your refund amount is Rs.20000".format(
                        row["course"]))
                    break


if __name__ == "__main__":
    with open("Course_info.csv", "w", newline='') as file:
        fieldnames = ['course', 'amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'course': 'Web Development', 'amount': 20000})
        writer.writerow({'course': 'Data Science', 'amount': 20000})
        writer.writerow({'course': 'IOT', 'amount': 20000})
        writer.writerow({'course': 'Cloud computing', 'amount': 20000})
        writer.writerow({'course': 'AI/ML', 'amount': 20000})
        writer.writerow({'course': 'Ful Stack Development', 'amount': 20000})

    with open("Student_info.csv", "w") as file:
        fieldnames = ['id', 'name', 'address', 'course', 'diposited', 'due', 'Is_Graduated']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"id": 1, 'name': 'Sushmita Rai', 'address': 'Lalitpur', 'course': 'Full Stack Development',
                         'diposited': 20000, 'due': 0, 'Is_Graduated': False})
        writer.writerow({"id": 2, 'name': 'Salina Karki', 'address': 'Shankhamool', 'course': 'Full Stack Development',
                         'diposited': 20000, 'due': 0, 'Is_Graduated': False})
        writer.writerow(
            {"id": 3, 'name': 'Shreya Rai', 'address': 'Patan', 'course': 'IOT', 'diposited': 10000, 'due': 10000,
             'Is_Graduated': False})
        writer.writerow(
            {"id": 4, 'name': 'Upasana Pradhan', 'address': 'Thamel', 'course': 'Cloud computing', 'diposited': 0,
             'due': 20000, 'Is_Graduated': False})
        writer.writerow(
            {"id": 5, 'name': 'Rumi Sing', 'address': 'Lalitpur', 'course': 'Graphic Desogning', 'diposited': 20000,
             'due': 0, 'Is_Graduated': True})
        writer.writerow(
            {"id": 6, 'name': 'Ruchi Sharma', 'address': 'Lamatar', 'course': 'AI/ML', 'diposited': 20000, 'due': 0,
             'Is_Graduated': True})

    while True:
        print("Enter your choice.")
        ch = int(input("1.View course information\n"
                       "2.View all student details\n"
                       "3.View your informations\n"
                       "4.Diposit fee amount\n"
                       "5.Update information\n"
                       "6.Delete information\n"
                       "7.Add student detail\n"
                       "8.Return fee to graduate student. \n"))
        operation = Academy()
        if ch == 1:
            operation.view_course('Course_info.csv')
        elif ch == 2:
            operation.all_student_info('Student_info.csv')
        elif ch == 3:
            id = int(input("Enter you id:"))
            operation.individual_student_info("Student_info.csv", id)
        elif ch == 4:
            id = int(input("Enter you id:"))
            amt = int(input("Enter amount to deposit: "))
            operation.deposit('Student_info.csv', amt, id)
            operation.all_student_info('Student_info.csv')
        elif ch == 5:
            id = int(input("Enter your id: "))
            col = input("Enter column you want to change:")
            val = input("Enter value to change: ")
            operation.update("Student_info.csv", id, col, val)
        elif ch == 6:
            id = int(input("Enter your id: "))
            operation.delete('Student_info.csv', id)
        elif ch == 7:
            operation.add_student('Student_info.csv')
        elif ch == 8:
            id = int(input("Enter your id: "))
            operation.refund('Student_info.csv', id)
        else:
            print("Invalid choice")
