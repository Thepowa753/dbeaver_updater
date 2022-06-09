from subprocess import check_output
from os.path import isfile, expanduser
from os import system


get_version_string = r"""curl --silent "https://api.github.com/repos/dbeaver/dbeaver/releases/latest"  | grep "tag_name" | sed -E 's/.*"([^"]+)".*/\1/'"""
download_latest_string = r"""wget -O ~/.local/dbeaver-ce-latest-stable.x86_64.rpm https://dbeaver.io/files/dbeaver-ce-latest-stable.x86_64.rpm"""
chmodding_string = r"chmod 777 ~/.local/dbeaver-ce-latest-stable.x86_64.rpm"
install_latest_string = r"""sudo dnf install -y ~/.local/dbeaver-ce-latest-stable.x86_64.rpm && rm ~/.local/dbeaver-ce-latest-stable.x86_64.rpm"""
latest_installed_path = expanduser("~/.config/dbeaver_version")

if not isfile(latest_installed_path):
	with open(latest_installed_path, "w") as f:
		f.write("\n")

latest_version = str(check_output(get_version_string, shell=True), "utf-8")
print(f"Latest version from git: {latest_version}")
with open(latest_installed_path, "r") as f:
	if latest_version in f.readline():
		print("Already up to date!")
		exit(0)
system(download_latest_string)
system(chmodding_string)
if system(install_latest_string) == 0:
	with open(latest_installed_path, "w") as f:
		f.write(f"{latest_version}\n")
else:
	print("DNF error!")
