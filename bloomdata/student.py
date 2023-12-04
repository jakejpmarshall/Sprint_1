import random


class Student:

    def __init__(self, sprint=0, job=False):
        self.sprint = sprint
        self.job = job

    def pass_sprint(self, num):
        self.sprint += num
        if self.sprint < 24:
            return f'Good Work! You are now on sprint {self.sprint}'
        return 'Congratulations! You have completed the course!'

    def apply_for_job(self):
        if self.sprint < 24:
            return 'Sorry. You do not have the nescessary skills for this job.'
        x = random.choice([0, 1])
        if x == 0:
            return '''Sorry, we are moving forward with different candidates
                    at the moment.
                    '''
        self.job = True
        return 'Hooray! You got the job!'


class BloomTechStudent(Student):

    def __init__(self, payment, sprint=0, job=False):
        super().__init__(sprint, job)
        self.payment = payment

    def pay(self):
        if self.payment.lower() == 'upfront':
            return 'Paid upfront'
        if self.sprint >= 24:
            self.apply_for_job()
            self.apply_for_job()
            if self.job is False:
                return 'Tuition waived'
            return 'Deferred tuition complete'
        return 'course not yet complete'

    def __repr__(self):
        return f'New student who opted for {self.payment} payment'


def student_generator(num=30):
    '''Generates a list of students with randomly generated payment type.
    By default, this function generates and appends 30 students to a list.
    '''

    students = []

    payment_type = random.choice(['upfront', 'deferred'])

    for _ in range(num):
        students.append(BloomTechStudent(payment_type))
