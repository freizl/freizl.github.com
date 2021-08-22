#! /bin/bash

# --- mount share folder from Win host
# sudo mount -t vboxfs win_shared_folder /media/a_share_folder

# --- tools
sudo apt-get install emacs subversion git-core chromium-browser

folder_apps="/apps"
if [ ! -d $folder_apps ]; then
    sudo mkdir $folder_apps
fi
# --- todo: update ownship
# sudo chown $USER.$USER $folder_apps
