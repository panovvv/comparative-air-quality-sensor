#!/usr/bin/env sh

# Follow this guide to log in without a password:
#https://alvinalexander.com/linux-unix/how-use-scp-without-password-backups-copy

# User-defined variables
SBC_USER=pi
SBC_IP=10.12.10.202

# We don't want to copy that over
VENV_PATH=venv
# End of user-defined variables

SBC_USER_AT_IP="$SBC_USER@$SBC_IP"
THIS_SCRIPT=$(basename "$0")
ROOT_DIR="$( cd "$( dirname "$0" )" && pwd )"
ROOT_DIR_NAME=$(basename "$ROOT_DIR")
echo "Root directory: ${ROOT_DIR}"

case $1 in
    cp)
      rsync -arv --exclude="$VENV_PATH" --exclude="$THIS_SCRIPT" \
      --exclude=.idea "$ROOT_DIR" $SBC_USER_AT_IP:/home/$SBC_USER/
    ;;
    venv)
      ssh -t $SBC_USER_AT_IP python3.7 -m venv "/home/$SBC_USER/$ROOT_DIR_NAME/venv"
      ssh -t $SBC_USER_AT_IP "cd /home/$SBC_USER/$ROOT_DIR_NAME && . venv/bin/activate && pip3.7 install -r requirements.txt"
    ;;
    run)
      ssh -t $SBC_USER_AT_IP \
      ". /home/$SBC_USER/$ROOT_DIR_NAME/venv/bin/activate; python3.7 /home/$SBC_USER/$ROOT_DIR_NAME/main.py 1"
    ;;
    clean)
      ssh -t $SBC_USER_AT_IP "rm -rf /home/$SBC_USER/$ROOT_DIR_NAME"
    ;;
esac
