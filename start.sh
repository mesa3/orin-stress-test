nohup stress --cpu 12 &
nohup ./gpu_burn -d 172800 &
sudo tegrastats --start --logfile ./log.txt --interval 6000
