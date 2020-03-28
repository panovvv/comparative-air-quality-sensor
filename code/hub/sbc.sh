#!/usr/bin/env bash

# User-defined variables
SBC_USER=pi
SBC_IP=192.168.1.19
# End of user-defined variables

# We don't want to copy virtual environment
VENV_PATH=venv

SBC_USER_AT_IP="$SBC_USER@$SBC_IP"

THIS_SCRIPT=$(basename "$0")
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR_NAME=$(basename "$ROOT_DIR")
#echo "Root directory: ${ROOT_DIR}"

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

case $1 in
sync)
  echo -e "${GREEN}Copying the project to SBC...${NC}"
  rsync -arv --exclude="$VENV_PATH" --exclude="$THIS_SCRIPT" \
    --exclude=.idea  --exclude=__pycache__ "$ROOT_DIR" $SBC_USER_AT_IP:/home/$SBC_USER/
  echo -e "${GREEN}Done!${NC}"
  ;;
venv)
  if ssh -t $SBC_USER_AT_IP stat "/home/$SBC_USER/$ROOT_DIR_NAME/venv/bin/activate" \> /dev/null 2\>\&1; then
    echo -e "${GREEN}Remote virtual environment already exists! Nothing to do here.${NC}"
  else
    echo -e "${RED}Creating remote virtual environment...${NC}"
    ssh -t $SBC_USER_AT_IP python3.7 -m venv "/home/$SBC_USER/$ROOT_DIR_NAME/venv"
    ssh -t $SBC_USER_AT_IP "cd /home/$SBC_USER/$ROOT_DIR_NAME && . venv/bin/activate && pip3.7 install -r requirements.txt"
    echo -e "${GREEN}Done!${NC}"
  fi
  ;;
run)
  echo
  echo
  echo -e "${GREEN}Running the project on SBC...${NC}"
  echo -e "${BLUE}Arguments: ${NC}\t${RED}${@:2}${NC}"
  ssh -t $SBC_USER_AT_IP \
    ". /home/$SBC_USER/$ROOT_DIR_NAME/venv/bin/activate; python3.7 /home/$SBC_USER/$ROOT_DIR_NAME/main.py ${@:2}"
  ;;
rm-clean)
  echo -e "${RED}Removing the project directory on SBC...${NC}"
  ssh -t $SBC_USER_AT_IP "rm -rf /home/$SBC_USER/$ROOT_DIR_NAME"
  echo -e "${GREEN}Done!${NC}"
  ;;
esac
