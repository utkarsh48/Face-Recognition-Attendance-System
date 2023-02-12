# Face-Recognition-Attendance-System
Smart Attendance system to mark the in/out time of Employees.

The cascade_classifier is obtained from opencv github repository.

Download the [classifier](https://github.com/kipr/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) (data/haarcascades/haarcascade_frontalface_default.xml) from the above github and place it the folder along with main.py.



## Don't Rename it ##

Install the dependencies:
     
     pip3 install -r requirements.txt

Running the Program:
    
    python3 main.py camera_rstp_http_link

Create a folder named Images.
Create a folder named Data and Move the user_list.txt to that folder

    mkdir Images
    mkdir Data
    mv user_list.txt Data/


  
## Setting Up DB
```
CREATE DATABASE Attendance;

CREATE TABLE `Attendance`.`Users` ( `EMP_ID` INT NOT NULL , `EMP_Name` VARCHAR(50) NOT NULL , `Designation` VARCHAR(20) NOT NULL , `Joined` TIMESTAMP NOT NULL, PRIMARY KEY (`EMP_ID`) ) ENGINE = InnoDB; 

CREATE TABLE `Attendance`.`Logs` ( `EMP_ID` INT NOT NULL, `APPEARANCE` TIMESTAMP NOT NULL) ENGINE = InnoDB;
select * from `attendance`.`users`;

select * from `attendance`.`attendance_in`;
select * from `attendance`.`attendance_out`;
select * from `attendance`.`logs`;
```