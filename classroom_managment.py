classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]

def index_student(name):
    for student in classroom:
        if student['name'] == name:
            return student
    return -1
def add_student(name, email=None):
    """Add a new student to the classroom
    with the following keys:
    'name': the given name
    'email': if email is given use it otherwise use <name>@example.com
             in lowercase, you can use the `s.lower()` method
    'grade': initialize with empty list
    """
    student = {}
    student['name'] = name
    student['email'] = email if email  else f'{name}@example.com'
    student['grades'] = []
    classroom.append(student)




def delete_student(name):
    """Delete a student from the classroom"""
    classroom.remove(index_student(name))


def set_email(name, email):
    """Sets the email of the student"""
    index_student(name)['email'] = email


def add_grade(name, profession, grade):
    """Adds a new grade to the student grades"""
    index_student(name)['grades'].append((profession,grade))


def avg_grade(name, profession):
    """Returns the average of grades of the student
    in the specified profession
    """
    total,count=0,0
    for prof,g in index_student(name)['grades']:
        if prof == profession:
            total+=g
            count+=1
    return total/count

def get_professions(name):
    """Returns a list of unique professions that student has grades in"""
    return list(set_grades:=set(index_student(name)['grades']))
