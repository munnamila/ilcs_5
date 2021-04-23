install:
	conda install -c conda-forge opencv
	conda install -c conda-forge tqdm
	conda install pytorch torchvision torchaudio cpuonly -c pytorch
	conda install -c conda-forge matplotlib

ubuntu:
	sudo apt install git
	sudo apt install python3-pip


openpose_0:
	sudo apt install git
	#
	git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose

openpose_1:
	# buntu16
	# cd openpose
	sudo apt-get install cmake-qt-gui
	#
	sudo apt-get install libopencv-dev
	#
	bash ./scripts/ubuntu/install_deps.sh
	#
	sudo pip3 install numpy opencv-python
	#
	git submodule update --init --recursive --remote
	#
	mkdir build/
	

