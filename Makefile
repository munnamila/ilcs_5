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

install_tools:
	sudo apt install tmux
	sudo apt install vim


install_openface:
	conda install -c anaconda opencv
	conda install -c anaconda numpy
	conda install -c anaconda pandas
	conda install -c anaconda scipy
	conda install -c anaconda scikit-learn
	conda install -c anaconda scikit-image
	pip2 install dlib
	conda install -c conda-forge txaio
	conda install -c anaconda twisted
	conda install -c conda-forge autobahn
	conda install -c anaconda openssl
	conda install -c anaconda pyopenssl
	conda install -c conda-forge imagehash
	conda install -c anaconda service_identity

install_pytotch_GPU:
	conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
	conda install -c conda-forge opencv
        conda install -c conda-forge tqdm
        conda install -c conda-forge matplotlib
        conda install -c anaconda pandas
        conda install -c anaconda scipy
        conda install -c anaconda scikit-learn
        conda install -c anaconda scikit-image
