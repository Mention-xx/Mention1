#!/usr/bin/env bash
sudo chown -R timesheet:timesheet /mnt/static/webapps/timesheet
sudo chmod -R 770 /mnt/static/webapps/timesheet
sudo chmod g+s /home/timesheet

sudo chown timesheet:timesheet /home/timesheet
sudo chmod 770 /home/timesheet

chown timesheet:timesheet /mnt/static/conf/apache/sites-available/*timesheet.monokro.me
chmod 770 /mnt/static/conf/apache/sites-available/*timesheet.monokro.me

sudo find /mnt/static/webapps/timesheet -type d -exec chmod g+s {} \;

