todo how to install and how to develop


Python 3.7

When it comes to linux on embedded boards,
"just upgrading the os" or "just installing the package"
is not an option sometimes.
For instance, I was running Rasbian Stretch that
only seemed to have Python 3.5. Installing from source
is an option, but it led to weird errors  like this one
https://github.com/numpy/numpy/issues/14553
So I'm giving pyenv a try:
https://realpython.com/intro-to-pyenv/
pyenv install -v 3.7.7
sudo apt install libatlas3-base libatlas-base-dev libgfortran-5-dev


upgrade to buster solved the problems

Follow this guide to log in without a password:
https://alvinalexander.com/linux-unix/how-use-scp-without-password-backups-copy

 https://www.pyimagesearch.com/2015/08/24/resolved-matplotlib-figures-not-showing-up-or-displaying/
sudo apt-get install tcl-dev tk-dev python3-tk


if graph is not showing do
echo $DISPLAY
should be set otherwise
export DISPLAY=:0

https://raspberry-projects.com/pi/pi-operating-systems/raspbian/screensaver