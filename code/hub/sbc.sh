#!/usr/bin/env bash

# User-defined variables
. sbc_vars.sh
if [ -z "${SBC_IP}" ]; then
  echo "Please set SBC_IP environment variable to contain the IP address of your single board computer."
  exit 1
else
  echo "SBC IP: ${SBC_IP}"
fi
if [ -z "${SBC_USER}" ]; then
  echo "Please set SBC_USER environment variable to contain Linux user name on your single board computer."
  exit 1
else
  echo "SBC username: ${SBC_USER}"
fi
# End of user-defined variables

# We don't want to copy virtual environment
VENV_PATH=venv

SBC_USER_AT_IP="${SBC_USER}@${SBC_IP}"

THIS_SCRIPT=$(basename "$0")
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR_NAME=$(basename "${ROOT_DIR}")

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

case $1 in
sync)
  if command -v rsync; then
    echo -e "${GREEN}Copying the project to SBC...${NC}"
    rsync -arv \
      --exclude="${VENV_PATH}" --exclude="${THIS_SCRIPT}" --exclude="Makefile" \
      --exclude=".idea" --exclude="__pycache__" --exclude="requirements_dev.txt" \
      --exclude=".*" --exclude="tox.ini" --exclude="README.md" \
      "$ROOT_DIR" "${SBC_USER_AT_IP}:/home/${SBC_USER}/"
    echo -e "${GREEN}Done!${NC}"
  else
    echo "This script relies on rsync program. Please install it and ensure it's in PATH"
    exit 1
  fi
  ;;
venv)
  if ssh -t "${SBC_USER_AT_IP}" stat "/home/${SBC_USER}/${ROOT_DIR_NAME}/venv/bin/activate" \> /dev/null 2\>\&1; then
    echo -e "${GREEN}Remote virtual environment already exists! Nothing to do here.${NC}"
  else
    echo -e "${RED}Creating remote virtual environment...${NC}"
    ssh -t "${SBC_USER_AT_IP}" \
      "python3.7 -m venv /home/$SBC_USER/$ROOT_DIR_NAME/venv"
    echo -e "${GREEN}Done!${NC} ${RED}Now installing the dependencies...${NC}"
    ssh -t "${SBC_USER_AT_IP}" \
      "cd /home/$SBC_USER/$ROOT_DIR_NAME && . venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt"
    echo -e "${GREEN}Done!${NC}"
  fi
  ;;
run)
  echo
  echo
  echo -e "${GREEN}Running the project on SBC...${NC}"
  echo -e "${BLUE}Arguments: ${NC}\t${RED}${@:2}${NC}"
  ssh -t "${SBC_USER_AT_IP}" \
    "export DISPLAY=:0 && cd /home/${SBC_USER}/${ROOT_DIR_NAME} && . venv/bin/activate && python main.py ${@:2}"
  ;;
rm-clean)
  echo -e "${RED}Removing the project directory on SBC...${NC}"
  ssh -t "${SBC_USER_AT_IP}" "rm -rf /home/${SBC_USER}/${ROOT_DIR_NAME}"
  echo -e "${GREEN}Done!${NC}"
  ;;
shutdown)
  echo -e "${RED}Sending shutdown command to SBC...${NC}"
  ssh -t "${SBC_USER_AT_IP}" "sudo shutdown -h now"
  echo -e "${GREEN}Done!${NC}"
  ;;
esac
