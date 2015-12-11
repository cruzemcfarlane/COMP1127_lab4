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

    
def compute_letter_grade(grade): 
    if grade ==0:
        return 0
    elif grade > 85:
        return "A+"
    elif grade >=70 and grade <=85:
        return "A"
    elif grade >=67 and grade <=69:
        return "A-"
    elif grade >=63 and grade <=66:
        return "B+"
    elif grade >=60 and grade <=62:
        return "B"
    elif grade >=57 and grade <=59:
        return "B-"
    elif grade >=53 and grade <=56:
        return "C+"
    elif grade >=50 and grade <=52:
        return "C"
    elif grade >=47 and grade <=49:
        return "C-"
    elif grade >=43 and grade <=46:
        return "D"
    elif grade >=36 and grade <=42:
        return "D+"
    elif grade <= 35:
        return "F"

def calc_letter_grade(st1):
    list_1=[]
    list_2=[]
    list_3=[]
    for x in range(0,6):
        list_1.append(st1[2][x][0])
        list_2.append(st1[2][x][1])
    list_3=zip(list_1,map(compute_letter_grade,list_2))
    return list_3

def convert_to_wtqp(Course_Det):
    return (credit_list[get_ccode(Course_Det)],qp_list[get_grade(Course_Det)])

def calc_gpa(Stud_Rec):
    crt_wtlist = map(lambda x: credit_list[x],[Stud_Rec[2] [n] [0] for n in range(0,len(Stud_Rec[2]))])
    crt_gplist1 = map(compute_letter_grade,[Stud_Rec[2] [n] [1] for n in range(0,len(Stud_Rec[2]))])
    crt_gplist = map(lambda y: qp_list[y] ,crt_gplist1)
    list4 = zip(crt_wtlist,crt_gplist)
    grade_point = sum(map(lambda f: f[0] * f[1] , list4))
    gpa= grade_point / sum(crt_wtlist)
    return gpa 
    
    

    
