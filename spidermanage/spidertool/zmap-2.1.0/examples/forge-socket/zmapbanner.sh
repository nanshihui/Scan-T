sudo zmap -p 80 -B 10M -N 1000 -q --output-fields=classification,saddr,daddr,sport,dport,seqnum,acknum,cooldown,repeat  -o - | ./forge-socket -c 1000 -d http-req > http-banners.out




sudo zmap -p 80 -B 10M -N 1000 -q -f "classification,saddr,daddr,sport,dport,seqnum,acknum,cooldown,repeat" -O csv  -o - |sudo  ./forge-socket -c 8000 -d http-req > http-banners.out


