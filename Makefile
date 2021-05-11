install_conda:
	conda install -c conda-forge opencv
	conda install -c conda-forge tqdm
	conda install -c conda-forge matplotlib

install_sshd:
	dpkg -l | grep ssh
	sudo apt-get install openssh-server
	dpkg -l | grep ssh
	ps -e | grep ssh

install-anaconda:
	wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
