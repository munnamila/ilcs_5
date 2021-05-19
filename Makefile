install_conda:
	conda install -c conda-forge opencv
	conda install -c conda-forge tqdm
	conda install -c conda-forge matplotlib

install_sshd:
	dpkg -l | grep ssh
	sudo apt-get install openssh-server
	dpkg -l | grep ssh
	ps -e | grep ssh
	sudo apt-get install net-tools
	ifconfig

install-anaconda:
	wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh

addusers:
	sudo adduser sou
	sudo adduser ta
	sudo adduser sai
	sudo adduser inohara
	sudo adduser satake
	sudo adduser hagiwara
	sudo adduser hachisuka
	sudo adduser warisawa
	sudo adduser kurita

