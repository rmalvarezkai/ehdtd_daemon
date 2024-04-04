#!/bin/bash
### BEGIN INIT INFO
# Provides:          math-trading-bot-init.sh
# Required-Start:    
# Required-Stop:     
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Script de inicio del firewall
# Description:       This file should be used to construct scripts to be
#                    placed in /etc/init.d.
### END INIT INFO

PATH=/sbin:/usr/sbin:/bin:/usr/bin
DESC="Math Trading Bot init"
NAME=math-trading-bot-init.sh
DAEMON_BASE=/usr/lib/math-trading-bot/bin/math-trading-bot-daemon.php
DAEMON_ARGS=""
SCRIPTNAME=/etc/init.d/$0
DEFAULT_CONF=/etc/default/math-trading-bot

. /lib/init/vars.sh
. /lib/lsb/init-functions

ROOT_DIR=""

if [ -f ${DEFAULT_CONF} ]
then
    . ${DEFAULT_CONF}
fi

DAEMON="/usr/bin/php"

if [ -n ${ROOT_DIR} ]
then
    DAEMON="${DAEMON} ${ROOT_DIR}${DAEMON_BASE}"
else
    DAEMON="${DAEMON} ${DAEMON_BASE}"
fi

if ! [ "${ENABLE}" = "yes" ]
then
    log_action_msg "Daemom is disabled please check ${DEFAULT_CONF} file"
    exit 0
fi

#
# Function that starts the daemon/service
#
do_start()
{
    RESULT=0
    log_progress_msg "Starting Math Trading Bot"
    ${DAEMON} start 1>/dev/null 2>/dev/null
    RESULT=$?
    log_progress_msg "Ready"
    return ${RESULT}
}

#
# Function that stops the daemon/service
#
do_stop()
{
    RESULT=0
    log_progress_msg "Stoping Math Trading Bot"
    ${DAEMON} stop 1>/dev/null 2>/dev/null
    RESULT=$?
    log_progress_msg "Ready"
    return ${RESULT}
}

#
# Function that sends a SIGHUP to the daemon/service
#
do_reload()
{
    do_stop
    /bin/sleep 1
    do_start
}

RESULT=0

case "$1" in
  start)
    log_daemon_msg "${NAME}"
    do_start
    RESULT=$?
        case ${RESULT} in
            0) log_end_msg 0 ;;
            1) log_end_msg 0 ;;
            2) log_end_msg 1 ;;
            *) log_end_msg 1 ;;
        esac
    ;;
  stop)
    log_daemon_msg "${NAME}"
    do_stop
    RESULT=$?
        case ${RESULT} in
            0) log_end_msg 0 ;;
            1) log_end_msg 0 ;;
            2) log_end_msg 1 ;;
            *) log_end_msg 1 ;;
        esac
    ;;
  reload|force-reload)
    log_daemon_msg "${NAME}"
    do_reload
    RESULT=$?
        case ${RESULT} in
            0) log_end_msg 0 ;;
            1) log_end_msg 0 ;;
            2) log_end_msg 1 ;;
            *) log_end_msg 1 ;;
        esac
    ;;
  restart|force-reload)
    log_daemon_msg "${NAME}"
    do_reload
    RESULT=$?
        case ${RESULT} in
            0) log_end_msg 0 ;;
            1) log_end_msg 0 ;;
            2) log_end_msg 1 ;;
            *) log_end_msg 1 ;;
        esac
    ;;
  *)
    echo "Usage: $SCRIPTNAME {start|stop|restart|force-reload}" >&2
    exit 3
    ;;
esac

exit ${RESULT}
