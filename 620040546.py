def student(sid,fname,lname, cc1,mark1,cc2,mark2,cc3,mark3,cc4,mark4,cc5,mark5,cc6,mark6):
    """Constructor for student"""
    return [sid,[fname,lname],[(cc1,mark1),(cc2,mark2),(cc3,mark3),(cc4,mark4),(cc5,mark5),(cc6,mark6)]]

def get_id(std):
    """Returns students ID"""
    return std[0]

def get_name(std):
    """Returns students Name"""
    return std[1]

def get_courses(std):
    """Returns a list of tuples of course codes and grade"""
    return std[2]

def get_fname(name):
    """Returns first name"""
    return name[0]

def get_lname(name):
    """Returns last name"""
    return name[1]

def get_ccode(course_det):
    """Returns course code part of the tuple"""
    return course_det[0]

def get_grade(course_det):
    """Returns grade part of the tuple"""
    return course_det[1]

       
st1=student('620000101',"John","Doe","CS11Q",80,"CS11R",60,"CS20R",50,"CS20S",60,"CS22Q",65,"CS23Q",80)

credit_list={'CS11Q':6,'CS11R':6,'CS20R':4,'CS23Q':4,'CS22Q':4,'CS20S':4}

qp_list = {"A+":4.3,"A":4.0,"A-":3.7,"B+":3.3,"B":3.0,"B-":2.7,"C+":2.3,"C":2.0,\
      "C-":1.7,"D+":1.3,"D": 1.0,"F": 0.0}
        

## For this fucntion to work you first need to write calc_gpa()
def print_students_gpa(std):
    """Prints the students details and GPA"""
    print "Student Id:", get_id(std)
    print "Student name:", get_fname(get_name(std)), get_lname(get_name(std))
    print "GPA: %.2f" %(calc_gpa(std))

    

    
def compute_letter_grade(n):
    if n>85:
        return 'A+'
    elif n>=70 and n<=85:
        return 'A'
    elif n>=67 and n<=69:
        return 'A-'
    elif n>=63 and n<=66:
        return 'B+'
    elif n>=60 and n<=62:
        return 'B'
    elif n>=57 and n<=59:
        return 'B-'
    elif n>=53 and n<=56:
        return 'C+'
    elif n>=50 and n<=52:
        return 'C'
    elif n>=47 and n<=49:
        return 'C-'
    elif n>=43 and n<=46:
        return 'D+'
    elif n>=36 and n<=42:
        return 'D'
    elif n<=35:
        return 'F'

def calc_letter_grade(stu)
