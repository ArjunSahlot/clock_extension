#!/bin/bash

download_link=https://github.com/ArjunSahlot/clock_extension/archive/main.zip
temporary_dir=$(mktemp -d) \
&& curl -LO $download_link \
&& unzip -d $temporary_dir main.zip \
&& rm -rf main.zip \
&& mv $temporary_dir/clock_extension-main $1/clock_extension \
&& rm -rf $temporary_dir
echo -e "[0;32mSuccessfully downloaded to $1/clock_extension[0m"
