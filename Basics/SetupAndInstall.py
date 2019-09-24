// install src: https://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/

// check version
python --version
python3 --version

// homebrew install openCV
brew tap homebrew/science

//install
brew install opencv3

// install numpy for python 2.7
pip install numpy

// install mutils for python 2.7
pip install --upgrade imutils

// install virtualenv virtualenvwrapper for python 2.7
pip install virtualenv virtualenvwrapper

// open bash profile
nano ~/.bash_profile
source ~/.bash_profile

// open virtual environment
mkvirtualenv cv -p python3

//
workon cv 
pip install requests
sudo pip3 install --upgrade imutils



# python3 download_images.py --urls urls.txt --output images/sushi

