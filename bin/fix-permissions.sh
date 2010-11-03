#!/usr/bin/env bash
chown -R timesheet:timesheet /home/timesheet
chmod -R 770                 /home/timesheet
chown -R timesheet:timesheet /mnt/static/webapps//timesheet
chmod -R 770                 /mnt/static/webapps//timesheet

find /home/timesheet -type d -exec chmod g+s {} \;
find /mnt/static/webapps/timesheet -type d -exec chmod g+s {} \;

