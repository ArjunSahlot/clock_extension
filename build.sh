#!/bin/bash

download_link=https://github.com/ArjunSahlot/clock_extension/archive/main.zip
temporary_dir=$(mktemp -d)
echo "Checking if curl is installed"
if [ $(sudo dpkg-query -l | grep curl | wc -l) -eq 0 ];
then
  echo -e "\033[0;31mcurl is not installed\033[0m"
  echo "Installing curl..."
  sudo apt install -y curl;
  echo -e "\033[0;32mcurl was successfully installed\033[0m"
else
  echo -e "\033[0;32mcurl is already installed\033[0m"
fi
curl -LO $download_link \
&& unzip -d $temporary_dir main.zip \
&& rm -rf main.zip \
&& mkdir -p $1 \
&& cp -r $temporary_dir/clock_extension-main $1/clock_extension \
&& rm -rf $temporary_dir \
&& echo -e "\033[0;32mSuccessfully downloaded to $1/clock_extension\033[0m" \
&& echo -e "\033[0;32mDone!\033[0m"
