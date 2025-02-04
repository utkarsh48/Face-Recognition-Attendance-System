import FR
import sys

if(len(sys.argv) != 2 ):
    print("Argument Error.")
    print("""use python 0
    where 0 is the camera index""")
    quit(0)

if sys.argv[1].isdigit(): 
    camera_index = int(sys.argv[1])
else:
    camera_index = sys.argv[1]

image_source = 'Images/'
user_path = 'Data/user_list.txt'
reference = "Data/reference.yml"

sql_ip = "127.0.0.1"  #localhost
sql_user = "root"
sql_password = "root"
sql_database = "Attendance"

obj = FR.Recognise(image_source, user_path, reference,camera_index)
obj.connect(sql_ip,sql_user,sql_password,sql_database)

while(1):
    opt = input("\n1.Enroll New User\n2.Track & Mark \n3.Clear data older than 30 days \n4.Exit \nEnter your option:")
    if(opt == '1'):
        obj.enroll()
    if(opt == '2'):
        obj.run()
    if(opt == '3'):
        obj.clear_old_data()
    if(opt == '4' or opt == 'e'):
        quit(0)
