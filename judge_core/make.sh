#!/bin/bash
cd judged
make
chmod +x judged
cp judged /usr/bin
cd ../judge_client
make
chmod +x judge_client
cp judge_client /usr/bin
cd ../sim/sim_2_67
make clean
make sim_c
make sim_java
make sim_pasc
chmod +x sim*
cp sim_c /usr/bin
cp sim_java /usr/bin/sim_java
cp sim_pasc /usr/bin/sim_pas
cd ..
cp sim.sh /usr/bin
chmod +x /usr/bin/sim.sh
ln -s /usr/bin/sim_c /usr/bin/sim_cc
ln -s /usr/bin/sim_c /usr/bin/sim_rb
ln -s /usr/bin/sim_c /usr/bin/sim_sh
