#!/bin/sh
####################################### restriction
### it is designed for new esb project
### opts [-s] should right after the $0
#######################################

DEV_WORKSPACE="/cygdrive/c/IntegrationServices/DEV/ESB"

while getopts ":s" opt; do
	case $opt in
	b ) echo $OPTARG  ;;
	s ) singleton="true" ;;
	? ) echo "usage : $0 [-s] args .."
	    exit 1 ;;
	esac
    shift $(($OPTIND - 1))
done

project_name=${1:-"not_set"}
message_family=${2:-"not_set"}

cd ${DEV_WORKSPACE}

if [ -d ${message_family} ]; then
    cd ${message_family}
else
  echo "could find message family: ${message_family}"
  exit 0
fi

project_path=$(find -name ${project_name} -type d)
cd ${project_path}"/trunk"

### Add status=enabled to esbsvc files
constant_attr="status=\"ENABLED\""
find *.esbsvc | xargs grep "<service.*${constant_attr}" -L | xargs sed -i -e 's#^\(<service.*\)\(>\)#\1 '"${constant_attr}"'\2#g'

consumer_esb_file=$(find -name "ConsumeJMS*wsdl" | sed 's#\./\(.*\)\.wsdl#*\1.esbsvc#g' )

### Add cacheConnections properties for Consume Adapter
sed -i -e 's#</service>#<endpointProperties>\n<property name=\"cacheConnections\" value=\"false\" />\n</endpointProperties>\n&#g' ${consumer_esb_file}

### Add singleton properties if it shall be for Consumer Adapter
if [ $singleton ]; then
sed -i -e 's#<endpointProperties>#&\n<property name=\"XclusterGroupId\" value="'${project_name}'" />\n<property name=\"InstanceIdPrefix\" value="'${project_name}'" />#g' ${consumer_esb_file}
fi

### Add retry properties for Produce Adapter
producer_esb_file=$(find -name "ProduceJMS*wsdl" | sed 's#\./\(.*\)\.wsdl#*\1.esbsvc#g' )
sed -i -e 's#</service>#<endpointProperties>\n<property name=\"RetryCount\" value=\"10\" />\n<property name=\"RetryInterval\" value=\"120\" />\n<property name=\"cacheConnections\" value=\"false\" />\n</endpointProperties>\n&#g' ${producer_esb_file}


#if (( $(grep -cw cacheConnections ${consumer_esb_file}) == 0 )); then
