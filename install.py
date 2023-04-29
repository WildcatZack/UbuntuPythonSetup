#!/bin/python3
import subprocess
import os



apt_update_cmd = subprocess.run(["sudo", "apt", "update", "-y", ])
print("The exit code was: {rc}".format(rc=apt_update_cmd.returncode))
apt_upgrade_cmd = subprocess.run(["sudo", "apt", "update", "-y"])
print("The exit code was: {rc}".format(rc=apt_update_cmd.returncode))


file_path = os.getcwd()
file_path_list = file_path.split("/")
user = file_path_list[2]
print(user)

user_full_name = input("What is your full name? (type and hit enter)")

user_gh_email = input("What email do you use for github? (type and hit enter)")

new_file_text = """
[user]
	name = {name}
	email = {email}
""".format(name=user_full_name, email=user_gh_email)

with open("/home/{u}/.gitconfig".format(u=user), mode="w") as gitconfig_file:
	gitconfig_file.write(new_file_text)

ssh_keygen_cmd = subprocess.Popen(["ssh-keygen", "-t", "ed25519", "-C", user_gh_email])
ssh_keygen_cmd.wait()


user_has_made_key = False

while not user_has_made_key:
	print("You need to copy and paste this key into a browser at https://github.com/settings/key")
	with open("/home/{u}/.ssh/id_ed25519.pub".format(u=user)) as pub_file:
		key = pub_file.read()
		print(key)
	made_key_input = input("Have you made your key yet? (y/n/exit)")

	if made_key_input == "exit":
		print("Goodbye.")
		exit()
	elif made_key_input == "n" or made_key_input == "N":
		print("You should copy the key into https://github.com/settings/key")
		print(key)
	elif made_key_input == "y" or made_key_input == "Y":
		print("User has made their key!")
		user_has_made_key = True

user_gh_folders = input("Would you like to create a gitProjects folder in your home directory? (y/n)")
if user_gh_folders == "":
	print("The user chose default")
	default_gh_folder_cmd = subprocess.run(["mkdir", "-p" ,"/home/{u}/gitProjects/myProjects".format(u=user), 
	"/home/{u}/gitProjects/otherProjects".format(u=user)])
	print("The exit code was: {rc}".format(rc=default_gh_folder_cmd.returncode))
elif user_gh_folders == "y" or user_gh_folders == "y" :
	print("User typed y")
	y_gh_folder_cmd = subprocess.run(["mkdir", "-p", "/home/{u}/gitProjects/myProjects".format(u=user), 
	"/home/{u}/gitProjects/otherProjects".format(u=user)])
	print("The exit code was: {rc}".format(rc=y_gh_folder_cmd.returncode))
else:
	pass




if user_gh_folders == "" or user_gh_folders == "y" or user_gh_folders == "Y":
	mv_project_cmd = subprocess.run(["mv","/home/{u}/UbuntuPythonSetup/".format(u=user), 
	"/home/{u}/gitProjects/myProjects/UbuntuPythonSetup/".format(u=user)])
	print("The exit code was: {rc}".format(rc=mv_project_cmd.returncode))
