#!/bin/python3
import subprocess
import sys
import os

if len(sys.argv) != 2:
	print("Sorry! 1 argument required.")
	sys.exit(1)

task = sys.argv[1]

if task != 'backup' and task != 'recover':
	print("Invalid operation. Only 'backup' or 'recover' allowed.")
	sys.exit(1)

def start_operation():
	backup_paths_file = open("backup-paths", "r")
	backup_paths = backup_paths_file.readlines()
	remote_name = None
	for backup_path in backup_paths:
		backup_path = backup_path.strip()
		if backup_path: 	# if backup_path is not None
			if backup_path.startswith('[') and backup_path.endswith(']'):
				remote_name = backup_path[1:len(backup_path)-1]
				continue
			paths = backup_path.split(':')
			local_path = paths[0]
			remote_path = paths[1]

			temp_path = local_path.split(os.path.sep)
			file_dir_name = temp_path.pop() # file or dir name
			if file_dir_name == '':
				file_dir_name = temp_path.pop()

			if task == 'backup':
				print("Backing up: "+file_dir_name)
				if local_path.endswith(os.path.sep): # if dir
					remote_path = remote_path+"/"+file_dir_name
				rclone_output = subprocess.run(["rclone", "copy", "--progress", local_path, remote_name+":"+remote_path], stdout=sys.stdout, stderr=subprocess.STDOUT)
			elif task == 'recover':
				print("Recovering: "+local_path)
				dest_path = os.path.sep.join(temp_path)
				if local_path.endswith(os.path.sep): # if dir
					dest_path = dest_path + os.path.sep + file_dir_name
				remote_path = remote_path+"/"+file_dir_name
				rclone_output = subprocess.run(["rclone", "copy", "--progress",remote_name+":"+remote_path, dest_path], stdout=sys.stdout, stderr=subprocess.STDOUT)
			print("rclone output code: "+str(rclone_output.returncode))
	backup_paths_file.close()

start_operation()
print("Script ended!")
