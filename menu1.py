import subprocess as sp
import os
import cgi
os.system("clear")
while 1:

    os.system("tput setaf 6")
    print("\n")
    print("\t\t\t___________________________________________")
    print("\t\t\t      !!  welcome to Automation Menu !!    ")
    print("\t\t\t___________________________________________")
    print("\n")
    os.system("tput setaf 7")

            # Menu

    print("""
    press 1: LVM (Logical Volume Manager)
    press 2: Docker Configuration
    press 3: Webserver Configuration
    press 4: Basic Linux Command
    Press 5: Hadoop Configuration
    press 6: Exit
    """)

    iput = input("Enter Input: ")
    print("\n")

        # LVM  (Logical Volume Manager)

    if iput == '1' :
        os.system("clear")
        while 1:
            os.system("tput setaf 6")
            print("\n")
            print("\t\t\t___________________________________________")
            print("\t\t\t        !!  welcome to LVM Menu !!         ")
            print("\t\t\t___________________________________________")
            print("\n")
            os.system("tput setaf 7")

            print("""
            press 1: create LVM
            press 2: Extend LVM
            press 3: Reduce LVM
            press 4: Exit
            """)
            print("\n")
            x = input ("Enter the no: ")
            # print("\n")
            if x == '1':
                os.system("tput setaf 3")
                print("\t\t_______________________")
                print("\t\t  LVM CREATE SUB MENU  ")
                print("\t\t_______________________")
                os.system("tput setaf 7")
                while 1:
                    print("""
                    press 1 : PV create
                    press 2 : VG create
                    press 3 : LV create
                    press 4 : Format & Mount
                    press 5 : Exit (Go to Main Menu)
                    """)
                    y = input("Enter valid input: ")

                    if y == '1':
                        os.system("tput setaf 2")
                        print("Wait PV is creating ")
                        os.system("tput setaf 7")
                        #os.system("pvdisplay")
                        os.system("fdisk -l")
                        disk = input("Enter the Disk name: ")
                        os.system("pvcreate {}".format(disk))
                        print("\n")
                        os.system("pvs")
                        print("\n")

                    if y == '2':
                        print("\n")
                        os.system("tput setaf 2")
                        print("Volume Group (VG) ")
                        os.system("tput setaf 7")
                        print("\n")
                        os.system("vgs")
                        print("\n")
                        vg_name = input("Enter Volume_Group (VG) name: ")
                        disk = input("Enter disk name: ")
                        os.system("vgcreate {0} {1} ".format(vg_name,disk))
                        os.system("vgs")
                        print("\n")

                    if y == '3':
                        print("\n")
                        os.system("tput setaf 2")
                        print("Logical Volume (LV) ")
                        os.system("tput setaf 7")
                        print("\n")
                        os.system("lvs")
                        print("\n")
                        lv_name = input("Enter LV name: ")
                        size = input("Enter the LV Size in GB: ")
                        vg_name = input("Enter the VG name: ")
                        os.system("lvcreate --size {0}G --name {1} {2}".format(size,lv_name,vg_name))
                        os.system("lvs")
                        print("\n")

                    if y == '4':
                        print("\n")
                        os.system("tput setaf 2")
                        print("LV format and Mount ")
                        os.system("tput setaf 7")
                        print("\n")
                        #lv_name = input("Enter the LV name: ")
                        os.system('lvdisplay | grep "LV Path" ')
                        print("\n")
                        lv_path = input("Enter the LV Path: ")
                        location = input("Enter mount location: ")
                        os.system("mkfs.ext4 {}".format(lv_path))
                        os.system("mkdir {}".format(location))
                        os.system("mount {0} {1}".format(lv_path,location))
                        print("\n")
                        os.system("df -lh")

                    if y == '5':
                        break
                    os.system("tput setaf 9")
                    input("press enter ")
                    os.system("clear")
                    os.system("tput setaf 7")

            if x == '2':
                print("\n")
                os.system("tput setaf 3")
                print("\t\t---------------")
                print("\t\t!! LV Extend !!")
                print("\t\t---------------")
                os.system("tput setaf 7")
                print("\n")
                lv_name = input("Enter the lv_name: " )
                print("\n")
                os.system("lvdisplay | grep {}".format(lv_name))
                print("\n")
                size = input("Enter the size: ")
                location = input("Enter the LV Path: ")
                os.system("lvextend --size +{0}GB {1}".format(size,location))
                os.system("resize2fs {}".format(location))
                print("\n")
                os.system("df -lh")

            if x == '3':
                print("\n")
                os.system("tput setaf 2")
                print("\t\t----------------------")
                print("\t\t!! Reduse partition !!")
                print("\t\t----------------------")
                os.system("tput setaf 7")
                print("\n")
                os.system("pvs")
                print("\n")
                os.system('lvdisplay | grep "LV Path"')
                print("\n")
                folder = input("Enter mount folder name: ")
                pv_name = input("Enter already created PV name: ")
                size = input("Enter the size to reduse (GB): ")
                lv_path = input("Enter the LV Path: ")
                print("\n")
                os.system("umount {}".format(folder))
                os.system("e2fsck -f {}".format(pv_name))
                os.system("resize2fs {0} {1}G".format(lv_path,size))
                os.system("lvreduce --size {0}G {1}".format(size,lv_path))
                os.system("mount {0} {1}".format(lv_path,folder))

            print("\n")
            os.system("tput setaf 9")
            input("press Enter")
            os.system("tput setaf 7")
            os.system("clear")

            if x == '4':
                os.system("clear")
                break

                # Docker

    if iput == '2':
        os.system("clear")
        os.system("systemctl start docker")
        while 1 :
            os.system("tput setaf 6")
            print("\n")
            print("\t\t\t___________________________________________")
            print("\t\t\t     !!  welcome to Docker Menu !!         ")
            print("\t\t\t___________________________________________")
            print("\n")
            os.system("tput setaf 7")

            print("""
            Press 1  : To Launch Container
            Press 2  : To Start Container
            Press 3  : To Stop Container
            Press 4  : To Delete Container
            Press 5  : To Delete all containers at once
            Press 6  : To See only running containers
            Press 7  : To See all containers
            Press 8  : To Pull docker image
            Press 9  : To See docker images
            Press 10 : To create docker image
            Press 11 : To delete docker image
            press 12 : Exit (Go to Main Menu)
            """)

            os.system("tput setaf 6")
            Docker = input("Enter your choice: ")
            print("\n")
            os.system("tput setaf 7")

            if Docker == '1':
                osname=input("Enter the container name : ")
                oimage=input("Enter the container image : ")
                os.system("tput setaf 2")
                print("---------------------")
                os.system("tput setaf 7")
                cmd= "sudo docker run -dit --name {} {}".format(osname,oimage)
                output = sp.getstatusoutput(cmd)

                status = output[0]
                out = output[1]

                if status == 0:
                    print("\n")
                    print("Container launched..!!")
                    print("Container Name : {}".format(osname))
                    print("Container Image : {}".format(oimage))
                else:
                    print("error : {}".format(out))

            elif Docker == '2':
                print("All Containers which are stopped and running currently : \n")
                os.system("sudo docker ps -a")
                os.system("tput setaf 3")
                print("\t\t\t\t******************")
                os.system("tput setaf 7")
                print("\n")
                osname=input("Enter the container name which you want to start : ")
                cmd="sudo docker start {}".format(osname)
                output = sp.getstatusoutput(cmd)

                status = output[0]
                out = output[1]
                if status==0:
                    print("Container {}  Started..!!".format(osname))
                else:
                    print("error : {}".format(out))

            elif Docker == '3':
                print("Containers already running : \n")
                os.system("sudo docker ps")
                os.system("tput setaf 3")
                print("\t\t\t\t******************")
                os.system("tput setaf 7")
                print("\n")
                osname=input("Enter the container name which you want to stop : ")
                cmd= "sudo docker stop {}".format(osname)
                output = sp.getstatusoutput(cmd)

                status = output[0]
                out = output[1]

                if status==0:
                    print("Container {}  Stopped..!!".format(osname))

                else:
                    print("error : {}".format(out))

            elif Docker == '4':
                print("Containers Available : \n")
                os.system("sudo docker ps -a")
                os.system("tput setaf 3")
                print("\t\t\t\t******************")
                os.system("tput setaf 7")
                print("\n")
                osname=input("Enter the container name which you want to delete : ")
                cmd= "sudo docker container rm -f {}".format(osname)
                output = sp.getstatusoutput(cmd)

                status = output[0]
                out = output[1]

                if status==0:
                    print("{} Container Removed..!!".format(osname))

                else:
                    print("error : {}".format(out))

            elif Docker == '5':
                cmd= "sudo docker rm -f $(docker ps -aq)"
                output = sp.getstatusoutput(cmd)

                status = output[0]
                out = output[1]

                if status==0:
                    print("All Containers removed successfully..!")
                else:
                    print("error : {}".format(out))

            elif Docker == '6':
                cmd= "sudo docker ps"
                output = sp.getstatusoutput(cmd)

                status = output[0]
                out = output[1]

                if status==0:
                    print(out)

                else:
                    print("error : {}".format(out))

            elif Docker == '7':
                cmd= "sudo docker ps -a"
                output = sp.getstatusoutput(cmd)

                status = output[0]
                out = output[1]

                if status==0:
                    print(out)

                else:
                    print("error : {}".format(out))

            elif Docker == '8':
                oimage=input("Enter the image name and its version which you want to pull : ")
                cmd= "docker pull {}".format(oimage)
                output = sp.getstatusoutput(cmd)
                ###print("Wait for a sec.....")
                status = output[0]
                out = output[1]

                if status==0:
                    print("Image pulled successfully..!")

                else:
                    print("error : {}".format(out))

            elif Docker == '9':
                cmd= "sudo docker images"
                output = sp.getstatusoutput(cmd)

                status = output[0]
                out = output[1]

                if status==0:
                    print(out)

                else:
                    print("error : {}".format(out))

            elif Docker == '10':
                osname=input("Enter the container name of which you want to create image : ")
                iname=input("Enter the Image Name : ")
                iversion=input("Enter the Image Version :")
                os.system("tput setaf 2")
                print("---------------------")
                os.system("tput setaf 7")
                cmd= "sudo docker commit {} {}:{}".format(osname,iname,iversion)
                output = sp.getstatusoutput(cmd)

                status = output[0]
                out = output[1]

                if status==0:
                    print("\n")
                    print("Image launched..!!")
                    print("Image Name : {}".format(iname))
                    print("Image version : {}".format(iversion))


                else:
                    print("error : {}".format(out))

            elif Docker == '11':
                print("Images Available : \n")
                os.system("sudo docker images")
                os.system("tput setaf 3")
                print("\t\t\t\t******************")
                os.system("tput setaf 7")
                print("\n")
                oimage=input("Enter the image name and its version which you want to delete : ")
                cmd= "docker rmi -f {}".format(oimage)
                output = sp.getstatusoutput(cmd)

                status = output[0]
                out = output[1]

                if status==0:
                    print("Image deleted successfully..!")

                else:
                    print("error : {}".format(out))

            elif Docker == '12':
                os.system("clear")
                break

            os.system("tput setaf 9")
            input("press enter ")
            os.system("clear")
            os.system("tput setaf 7")

        # Webserver

    if iput == '3':
        os.system("clear")
        import webbrowser
        while 1:
            os.system("tput setaf 6")
            print("\n")
            print("\t\t\t___________________________________________")
            print("\t\t\t     !!  welcome to Webserver Menu !!      ")
            print("\t\t\t___________________________________________")
            print("\n")
            os.system("tput setaf 7")

            print("""
            Press 1 : To Install Web Server
            Press 2 : To Start Web services
            Press 3 : To Stop Web services
            Press 4 : To enable Web services
            Press 5 : To see the status of web services
            Press 6 : To create a web page
            Press 7 : To view the page created
            Press 8 : To deploy the page on webbrowser
            Press 9 : To Exit
            """)

            os.system("tput setaf 6")
            cmd = input("Enter your choice : ")
            print("\n")
            os.system("tput setaf 7")

            if cmd == '1':
                os.system("tput setaf 2")
                print("\t\t\tPlease Wait.. Processing your Dockeruest !")
                print("\t\t\t\t------------------")
                print("\n")
                os.system("tput setaf 7")
                p=sp.getstatusoutput("yum install httpd")
                #print("\n")
                if p[0]==0:
                    print("httpd software installed successfully..!!")
                else:
                    print("Error installing httpd software..!!")

            elif cmd == '2':
                os.system("tput setaf 2")
                print("\t\t\tPlease Wait.. Processing your Dockeruest !")
                print("\t\t\t\t------------------")
                print("\n")
                os.system("tput setaf 7")
                p=sp.getstatusoutput("systemctl start httpd")
                #print("\n")
                if p[0]==0:
                    print("Web services started successfully..!!")
                else:
                    print("Error in starting web services..!!")

            elif cmd == '3':
                os.system("tput setaf 2")
                print("\t\t\tPlease Wait.. Processing your Dockeruest !")
                print("\t\t\t\t------------------")
                print("\n")
                os.system("tput setaf 7")
                p=sp.getstatusoutput("systemctl stop httpd")
                #print("\n")
                if p[0]==0:
                    print("Web services stopped successfully..!!")
                else:
                    print("Error in stopping web services..!!")

            elif cmd == '4':
                os.system("tput setaf 2")
                print("\t\t\tPlease Wait.. Processing your Dockeruest !")
                print("\t\t\t\t------------------")
                print("\n")
                os.system("tput setaf 7")
                p=sp.getstatusoutput("systemctl enable httpd")
                #print("\n")
                if p[0]==0:
                    print("Web services enabled successfully..!!")
                else:
                    print("Error in enabling web services..!!")

            elif cmd == '5':
                p=sp.getoutput("systemctl status httpd")
                print(p)


            elif cmd == '6':
                file=input("Enter the file name for the webpage : ")
                print("\nEnter the data (After entering the data, Press enter then 'ctrl+D' to save the file) : ")
                os.system("tput setaf 2")
                print("---------------------")
                os.system("tput setaf 7")
                sp.getoutput("cat > {}".format(file))
                print("\nFile \"{}\" created successfully..!".format(file))
                os.system("mv /arth-ws/{} /var/www/html".format(file))

            elif cmd == '7':
                file=input("Enter the file name you want to view : ")
                os.system("tput setaf 2")
                print("---------------------")
                os.system("tput setaf 7")
                print("Content of file \'{}\' :".format(file))
                os.system("tput setaf 2")
                print("---------------------")
                os.system("tput setaf 7")
                print("\n")
                os.system("cd /var/www/html; cat {}".format(file))

            elif cmd == '8':
                ip=input("Enter the Public Ip address of your system : ")
                file=input("Enter the file name you want to execute : ")
                os.system("tput setaf 2")
                print("\t\t\t\t------------------")
                print("\t\t\tPlease Wait.. Processing your Dockeruest !")
                print("\t\t\t\t------------------")
                print("\n")
                os.system("tput setaf 7")
                webbrowser.open("http://{}/{}".format(ip,file))
                os.system("sleep 15")

            elif cmd == '9':
                os.system("clear")
                break

            os.system("tput setaf 9")
            input("press enter ")
            os.system("clear")
            os.system("tput setaf 7")

        # Linux

    if iput == '4':
        os.system("clear")
        while 1:
            os.system("tput setaf 6")
            print("\n")
            print("\t\t\t___________________________________________")
            print("\t\t\t      !!  welcome to Linux Menu !!         ")
            print("\t\t\t___________________________________________")
            print("\n")
            os.system("tput setaf 7")

            print("""
                Press 1  : To see the date
                Press 2  : To see the Calendar
                Press 3  : To see list
                Press 4  : Run df -h cmd
                Press 5  : Run free -m cmd
                Press 6  : To see info of CPU
                Press 7  : Run whoami cmd
                Press 8  : To see the path of the current directory
                Press 9  : To see the jobs running
                Press 10 : For adding a User
                Press 11 : For setting the password for user
                Press 12 : To Run any other cmd
                press 13 : Exit (Go to Main Menu)
            """)

            cmd = input("Enter your choice: ")
            os.system("tput setaf 6")
            print("\n")
            os.system("tput setaf 7")

            if cmd == '1':
                p=sp.getoutput("date")
                print("\n")
                print(p)

            elif cmd == '2':
                p=sp.getoutput("cal")
                print("\n")
                print(p)

            elif cmd == '3':
                print("\n")
                path=input("Enter the path for which you want to see the list : ")
                p=sp.getoutput("ls "+path)
                print("\n")
                print(p)

            elif cmd == '4':
                p=sp.getoutput("df -h")
                print("\n")
                print(p)

            elif cmd == '5':
                p=sp.getoutput("free -m")
                print("\n")
                print(p)

            elif cmd == '6':
                p=sp.getoutput("lscpu")
                print("\n")
                print(p)

            elif cmd == '7':
                p=sp.getoutput("sudo whoami")
                print("\n")
                print(p)

            elif cmd == '8':
                p=sp.getoutput("sudo pwd")
                print("\n")
                print(p)

            elif cmd == '9':
                p=sp.getstatusoutput("sudo jobs")
                q=bool(p[1])
                print("\n")
                print(p)
                #if(q!= True):
                #       print("\n")
                #       print("No jobs running currently..!")

            elif cmd == '10':
                print("\n")
                name=input("Enter the name for the User : ")
                p=sp.getstatusoutput("useradd "+name)
                status=p[0]
                output=p[1]
                if status==0:
                    print("User Created Successfully!!")
                else:
                    print("Error : {}".format(output))

            elif cmd == '11':
                print("\n")
                user=input("Enter the username : ")
                print("\n ")
                p=sp.getstatusoutput("passwd "+user)
                status=p[0]
                output=p[1]
                if status==0:
                    print("Password Created Successfully!!")
                else:
                    print("Error : {}".format(output))

            elif cmd == '12':
                print("\n")
                command=input("Enter the command to run : ")
                p=sp.getoutput(command)
                print(p)

            elif cmd == '13':
                os.system("clear")
                break

            input("Press Enter")
            os.system("clear")

        # Hadoop

    if iput == '5':

        print("\n\n")
        os.system("tput setaf 3")
        print("\t\t------------------")
        print("\t\t Hadoop Automation")
        print("\t\t------------------")
        os.system("tput setaf 6")
        print("""
            press 1: Local
            press 2: Remote
            press 3: Exit (Go to Main Menu)
        """)

        hadoop_input = input ("Enter your choice: ")

        while 1:
            if hadoop_input == '1':
                print("\n\n\n !! Menu !! ")
                os.system("tput setaf 7")
                print("""
                Press 1 : Master setup (Name Node)
                Press 2 : Slave  setup (Data Node)
                Press 3 : Replication  (By default 3)
                Press 4 : Block size   (By default 64 MB)
                Press 5 : Replicatio and Block Size
                Press 6 : JPS          (To check NN/DN)
                Press 7 : Put          (Upload)
                Press 8 : Read
                Press 9 : Remove
                Press 10: Exit (Go to Main Menu)
                """)
                print("\n\n")

                type = input("Enter your choice: ")

                if type == '1' :
                        folder = input("Enter Folder Name: ")
                        ip = input("Enter ip: ")
                        port_ = input("Enter port no: ")
                        print("Processing... ")
                        print("\n")
                        sp.getoutput('echo \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/{}</value>\n</property>\n</configuration> \' > /etc/hadoop/hdfs-site.xml'.format(folder))
                        sp.getoutput('echo \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:{1}</value>\n</property>\n</configuration> \' > /etc/hadoop/core-site.xml'.format(ip,port_))
                        sp.getoutput("rf -rf /{}".format(folder))
                        sp.getoutput("mkdir /{}".format(folder))
                        os.system("hadoop namenode -format")
                        sp.getoutput("hadoop-daemon.sh start namenode")
                        print("\n")
                        os.system("tput setaf 2")
                        os.system("jps")
                        os.system("tput setaf 7")
                        print("\n")

                if type == '2':
                        folder = input("Enter Folder Name: ")
                        print("\n")
                        ip = input("Enter master ip: ")
                        port_ = input("Enter master port-no: ")
                        print("Processing... ")
                        print("\n")
                        sp.getoutput('echo \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/{0}</value>\n</property>\n</configuration> \' > /etc/hadoop/hdfs-site.xml'.format(folder))
                        sp.getoutput('echo \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:{1}</value>\n</property>\n</configuration> \' > /etc/hadoop/core-site.xml'.format(ip,port_))
                        sp.getoutput("mkdir /{}".format(folder))
                        sp.getoutput("hadoop-daemon.sh start datanode")
                        print("\n")
                        os.system("tput setaf 2")
                        os.system("jps")
                        os.system("tput setaf 7")
                        print("\n")

                if type == '3':
                        os.system("tput setaf 2")
                        print("\n")
                        print("By default replicatin 3 ")
                        os.system("tput setaf 7")
                        print("\n")
                        replication_ = input("Enter no of replication: ")
                        ip = input("Enter the master ip: ")
                        port_ = input("Enter port no: ")
                        print("\n")
                        sp.getoutput('echo \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.replication</name>\n<value>{0}</value>\n</property>\n</configuration> \' > /etc/hadoop/hdfs-site.xml'.format(replication_))
                        sp.getoutput('echo \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:{1}</value>\n</property>\n</configuration> \' > /etc/hadoop/core-site.xml'.format(ip,port_))
                        os.system("hadoop fs -ls / ")
                        print("\n")
                if type == '4':
                        os.system("tput setaf 2")
                        print("\n")
                        print("By default Block size 64 ")
                        os.system("tput setaf 7")
                        print("\n")
                        ip = input("Enter the master ip: ")
                        port_ = input("Enter port no: ")
                        size = input("Enter Size in Bytes: ")
                        print("\n")
                        sp.getoutput('echo \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.block.size</name>\n<value>{0}</value>\n</property></configuration> \' > /etc/hadoop/hdfs-site.xml'.format(size))
                        print("\n")

                if type == '5':
                        replication_ = input("Enter no of replication: ")
                        ip = input("Enter the master ip: ")
                        port_ = input("Enter port no: ")
                        size = input("Enter Size in Bytes: ")
                        sp.getoutput('echo \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.replication</name>\n<value>{0}</value>\n</property>\n<property>\n<name>dfs.block.size</name>\n<value>{1}</value>\n</property></configuration> \' > /etc/hadoop/hdfs-site.xml'.format(replication_,size))
                        sp.getoutput('echo \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:{1}</value>\n</property>\n</configuration> \' > /etc/hadoop/core-site.xml'.format(ip,port_))

                if type == '6' :
                        os.system("tput setaf 1")
                        os.system("tput setaf 7")
                        os.system("jps")

                if type == '10':
                    os.system("clear")
                    break

            if hadoop_input == '2':

                print("\n\n\n !! Menu !! ")
                os.system("tput setaf 7")
                print("""
                Press 1 : Master setup (Name Node)
                Press 2 : Slave  setup (Data Node)
                Press 3 : Put          (Upload)
                Press 4 : Read
                Press 5 : Remove       (Delete)
                Press 6 : JPS          (To check NN/DN)
                Press 7 : Exit (Go to main mainu)
                """)
                type = input("Enter your choice: ")

                if type == '1':
                    folder_name = input("Enter your folder name: ")
                    remote_ip = input("Enter the Remote IP: ")
                    port_no = input ("Enter the Port No: ")
                    os.system(f"""ssh root@{remote_ip} mkdir /{folder_name}
        echo \'<?xml version=\"1.0\"?>
        <?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>

        <!-- Put site-specific property overrides in this file. -->

        <configuration>
        <property>
        <name>dfs.name.dir</name>
        <value>/{folder_name}</value>
        </property>
        </configuration>\' | ssh root@{remote_ip} -T \'cat > /etc/hadoop/hdfs-site.xml\'
        """)
                    os.system(f"""
        echo \'<?xml version=\"1.0\"?>
        <?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>

        <!-- Put site-specific property overrides in this file. -->

        <configuration>
        <property>
        <name>fs.default.name</name>
        <value>hdfs://{ip}:{port_no}</value>
        </property>
        </configuration>\' | ssh root@{remote_ip} -T \'cat > /etc/hadoop/core-site.xml\'
        """)
                    os.system("ssh root@{remote_ip} hadoop namenode -format")
                    os.system("ssh root@{remote_ip} hadoop-daemon.sh start namenode")
                    os.system("ssh root@{remote_ip} jps")

                if type == '2':
                    folder_name = input("Enter your folder name: ")
                    remote_ip = input("Enter the Remote IP: ")
                    port_no = input ("Enter the Port No: ")
                    os.system(f"""ssh root@{remote_ip} mkdir /{folder_name}
        echo \'<?xml version=\"1.0\"?>
        <?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>

        <!-- Put site-specific property overrides in this file. -->

        <configuration>
        <property>
        <name>dfs.data.dir</name>
        <value>/{folder_name}</value>
        </property>
        </configuration>\' | ssh root@{remote_ip} -T \'cat > /etc/hadoop/hdfs-site.xml\'
        """)
                    os.system(f"""
        echo \'<?xml version=\"1.0\"?>
        <?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>

        <!-- Put site-specific property overrides in this file. -->

        <configuration>
        <property>
        <name>fs.default.name</name>
        <value>hdfs://{ip}:{port_no}</value>
        </property>
        </configuration>\' | ssh root@{remote_ip} -T \'cat > /etc/hadoop/core-site.xml\'
        """)
                    os.system("ssh root@{remote_ip} hadoop-daemon.sh start datanode")
                    os.system("ssh root@{remote_ip} jps")
                    
                if type == '6':
                    os.system('ssh root@{remote_ip} jps')

                if type == '7':
                    os.system("clear")
                    break

            if hadoop_input == '3':
                os.system("clear")
                break

            os.system("tput setaf 9")
            input("press Enter")
            os.system("tput setaf 7")
            os.system("clear")


    if iput == '6':
        os.system("clear")
        break