Name:  Jonathan Ho
Email:  jlh5360@rit.edu
Date:  2/2/2024


HW2 Installation/Usage Instructions:
  NOTE:  You should not be facing any problems, but you are then, run this command and enter this password:
  		source jlh5360-openrc.sh
  		h3ll()W0rld@gain_
  
  1. Ensure you are the user ubuntu:
       - If not, then run this command in the terminal:
       		su ubuntu

  2. Ansible is already installed
       - Run the "ansible ---version" command to verify

  3. Ensure you are in this path: /home/ubuntu
       - If not, then run this command in the terminal:
       		cd ~

  4. After running the "ls" command, you should see these files:
		jlh5360_hw2_install_sshd_and_git_linux.yml
		jlh5360_hw2_start_winrm_install_openssh_create_user_windows.yml
		linux_inventory.ini
		win_inventory.ini

  5. Test your connection/connectivity with Linux (192.168.2.73) based on the inventory file
     (linux_inventory.ini) by running this command and should get this result:
  		ubuntu@test1:~$ ansible linux -i linux_inventory.ini -m ping
  		192.168.2.73 | SUCCESS => {
		    "ansible_facts": {
			"discovered_interpreter_python": "/usr/bin/python3"
		    },
		    "changed": false,
		    "ping": "pong"
		}

  6. Run the Linux playbook by running this command and should/will get this result:
  		ubuntu@test1:~$ ansible-playbook -i linux_inventory.ini jlh5360_hw2_install_sshd_and_git_linux.yml 

		PLAY [Install SSHD and Git service] ********************************************

		TASK [Gathering Facts] *********************************************************
		ok: [192.168.2.73]

		TASK [Install SSHD] ************************************************************
		ok: [192.168.2.73]

		TASK [Start SSHD] **************************************************************
		ok: [192.168.2.73]

		TASK [Install Git] *************************************************************
		ok: [192.168.2.73]

		PLAY RECAP *********************************************************************
		192.168.2.73               : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

		ubuntu@test1:~$

  7. Test your connection/connectivity with Linux (192.168.1.10) based on the inventory file
     (win_inventory.ini) by running this command and should get this result:
  		ubuntu@test1:~$ ansible windows -i win_inventory.ini -m win_ping
  		192.168.1.10 | SUCCESS => {
		    "changed": false,
		    "ping": "pong"
		}

  8. Run the Windows playbook by running this command and should/will get this result:
  		ubuntu@test1:~$ ansible-playbook -i win_inventory.ini jlh5360_hw2_start_winrm_install_openssh_create_user_windows.yml 

		PLAY [Start WinRM & install OpenSSH & create user] *****************************

		TASK [Gathering Facts] *********************************************************
		ok: [192.168.1.10]

		TASK [Start WinRM service] *****************************************************
		ok: [192.168.1.10]

		TASK [Install OpenSSH Server] **************************************************
		changed: [192.168.1.10]

		TASK [Start OpenSSH Server] ****************************************************
		ok: [192.168.1.10]

		TASK [Create a new user] *******************************************************
		ok: [192.168.1.10]

		PLAY RECAP *********************************************************************
		192.168.1.10               : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

		ubuntu@test1:~$

  9.  This concludes the end of how to prepare and then use/run the Ansible playbooks
  
  10. If you want, you can test or check the changes by going to the instances themselves
        - Linux (target)
        	1. Ensure you are the user ubuntu:
                     - If not, then run this command in the terminal:
       				su ubuntu

		2. Ensure you are in this path: /home/ubuntu
		       - If not, then run this command in the terminal:
		       		cd ~

  		3. After running the "systemctl --type=service --state=runnig | grep ssh" command, you should get this result:
  				ssh.service			loaded active running OpenBSD Secure Shell server

  		4. Finally, after running "git --version", you should get this result:
  				git version 2.34.1

        - Windows (ansible_windows)
        	1. Login the user ansible with these credentials:
        		Username: ansible
        		Password: ansible

        	2. First, you need to check the installment of OpenSSH by going into Windows
        	   Powershell and type the command "ssh", and you will then be provided with
        	   an overview of how to user the "ssh" command

        	3. To check if the user testuser has been added, you will need to logout of
        	   the user ansible, then you should/will see the user testuser in the list
        	   of accounts, and try to login to the user testuser using these credentials:
        	   	Username: testuser
        	   	Password: testuser
        	   	
  11. This concludes the end of verifying the successfullness of each Ansible playbooks
