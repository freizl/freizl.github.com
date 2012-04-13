#!/bin/sh
### ls MsgFamily which has logs, excluding TEST files, older than /tmp/tmp_log_cp
### Refer to find_logs.sh of how to generate the tmp_log_cp or copy the scripts here.

cd "/var/soa-dirs/anflog/ESB"
day=${1:-"$(date +%d)"}

log_files=( $(find ./ -name *.xml -newer /tmp/tmp_log_cp) )
echo "${#log_files[*]} log files found"

(( ${#log_files[*] > 0} )) && echo ${log_files[@]} |
  xargs grep -L ANFTEST |
  xargs ls -l |
  awk '$7=='${day## }' {print $9}' |
  awk -F"/" '{print $2}' |
  sort |
  uniq
