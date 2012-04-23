#!/bin/sh

if [ $# = 0 ]; then
    echo "error: specify a Message Family name.[Agents, Diffs, Factories, FitchTrack, Foundation, Items, KeyItems, MerchHiers, OrgHiers, POs, Stores, UDAs, Vendors]"
    exit 0
fi
message_family=${1:-"./"}
log_number=${2:-"6"}

tmp_dir=~/tmp/tmp_log_dir/
tmp_log=~/tmp/tmp_log_cp
( test -f ${tmp_log} && (( $(date +%H) - 5 <= 0 )) && (( $(date +%e) - $(date -r ${tmp_log} +%e) <= 1 )) ) || touch -t $(date +%m%d0001) ${tmp_log} 

cd /var/soa-dirs/anflog/ESB
log_files=( $(find ${message_family} -name *.xml -newer ${tmp_log}) )
echo "${#log_files[*]} log files found"

(( ${#log_files[*] > 0} )) && echo ${log_files[@]} | 
    xargs grep -L ANFTEST |
    sort -r |
#   xargs ls -ct1r |
    awk -F"/" -v log_dir="${tmp_dir}" '
               {if ($3!=prev_proj) count=0}
               {if ($3==prev_proj) count=count+1 }
               {prev_proj=$3}
               count>='${log_number}' {next}
               {file=$0; gsub(/[\/\\:-]/,"_",file); print "cp", $0, log_dir file}' | sh

#rm last '/' in ${1} if exists
ls -c1 "${tmp_dir}""${message_family%*/}"* 2>/dev/null
                       
########
# a. parameter : Msg Family, Log File Count
# b. search most recently logs (default is <=6) for each Project
########
#echo "${#log_files[*]} log files found"
