#!/bin/sh

if [ $# = 0 ]; then
    echo "usage: specify project path like POs/Consume/RIB_RIBPOs, with multiple env: dev/qa/test/prod"
    exit 0
fi

#remove postfix '/' if exists
project_path=${1%*/}

shift
envs=$(echo $* | tr [a-z] [A-Z])

init_directory()
{
  #TODO error if parameter 1 was not passed
  WORKSPACE="/cygdrive/c/IntegrationServices/"
  if [ ! pwd = $WORKSPACE ]; then
  	cd $WORKSPACE
  fi
  
  ENV=${2:-"false"}
  PROJECT_PATH=$ENV"/ESB/"$1
  SAMPLE_BUILD=$WORKSPACE"DEV/ESB/Builds/trunk/build/SAMPLES/Sample_build.xml"
  SAMPLE_PROPERTIES=$WORKSPACE"DEV/ESB/Builds/trunk/build/SAMPLES/Sample_build_"${ENV}".properties"
  
  mkdir -p ${PROJECT_PATH}"/branches"
  mkdir -p ${PROJECT_PATH}"/tags"
  mkdir -p ${PROJECT_PATH}"/trunk/build"

  proj_name=${1##*/}
  proj_repos=${1%*/$proj_name}
  cp $SAMPLE_PROPERTIES ${PROJECT_PATH}"/trunk/build/build_"${ENV}".properties"
  sed -e "s#\[PROJECT NAME\]#$proj_name#g" -e "s#\[PROJECT REPOSITORY PATH\]#$proj_repos#g" $SAMPLE_BUILD >${PROJECT_PATH}"/trunk/build/build.xml"
}

for env in $envs; do
#    echo "init_directory $project_path $env"
     init_directory $project_path $env
done

############################# not used
mcd ()
{
  for s in $*; do
    #if [ ! -d $s ]; then 
    mkdir -p $s && cd $s
    #fi
  done
}
