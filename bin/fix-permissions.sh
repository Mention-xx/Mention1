#!/usr/bin/env bash
chown -R timesheet:timesheet /home/timesheet
chmod -R 770 /home/timesheet

find /home/timesheet -type d -exec chmod g+s {} \;

