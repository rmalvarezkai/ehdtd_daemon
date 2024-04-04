#!/bin/bash

RM=/usr/bin/rm
SU=/usr/bin/su

USER_REPO=repository

PIPENV=/home/${USER_REPO}/.local/bin/pipenv

DIR_APP=/mnt/x50/math-trading-bot/src/usr/lib/math-trading-bot/app
REQ_FILE=${DIR_APP}/req/requirements.txt

cd ${DIR_APP}

if [ "$1" = "reinstall" ]
then
    ${SU} - ${USER_REPO} -l -c "PIPENV_VENV_IN_PROJECT=1 ${PIPENV} --rm --bare -q"
    ${RM} -f Pipfile
    ${RM} -f Pipfile.lock
    ${SU} - ${USER_REPO} -l -c "PIPENV_VENV_IN_PROJECT=1 ${PIPENV} install -q --bare -r ${REQ_FILE} --pre"
else
    ${SU} - ${USER_REPO} -l -c "PIPENV_VENV_IN_PROJECT=1 ${PIPENV} update -q --bare --pre"
fi

##/usr/local/bin/permisos.sh
##PIP_IGNORE_INSTALLED=1 





