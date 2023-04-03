import os



filepath = r'./log.txt' 
log=open(filepath,encoding='utf-8')
n=0
GPU1sum = 0
GPU2sum =0
CPUsum=0
SOC1sum=0
SOC2sum=0
SOC0sum=0
    
for eachline in log:
    if 'EMC_FREQ' in eachline:
        n=n+1
        (A,SOC0)=eachline.split('SOC0@')
        (SOC0,A)=SOC0.split('C CV1')
        (A,SOC1)=eachline.split('SOC1@')
        (SOC1,A)=SOC1.split('C CV2')
        (A,SOC2)=eachline.split('SOC2@')
        (SOC2,A)=SOC2.split('C Tdiode')
        (A,GPU)=eachline.split('GR3D_FREQ')
        (GPU,A)=GPU.split(' NVJPG1')
        (GPU1,GPU2)=GPU.split(' GR3D2_FREQ')
        (A,GPU1)=GPU1.split('@')
        (A,GPU2)=GPU2.split('@')
        (CPU,A)=eachline.split('] EMC_FREQ')
        (A,CPU1,CPU2,CPU3,CPU4,CPU5,CPU6,CPU7,CPU8)=CPU.split('@')
        (CPU1,A)=CPU1.split(',')
        (CPU2,A)=CPU2.split(',')
        (CPU3,A)=CPU3.split(',')
        (CPU4,A)=CPU4.split(',')
        (CPU5,A)=CPU5.split(',')
        (CPU6,A)=CPU6.split(',')
        (CPU7,A)=CPU7.split(',')
        GPU1sum=GPU1sum+float(GPU1)
        GPU2sum=GPU2sum+float(GPU2)
        CPUsum0=float(CPU1)+float(CPU2)+float(CPU3)+float(CPU4)+float(CPU5)+float(CPU6)+float(CPU7)+float(CPU8)
        CPUsum0=CPUsum0/8
        CPUsum=CPUsum+CPUsum0
        SOC0sum=SOC0sum+float(SOC0)
        SOC1sum=SOC1sum+float(SOC1)
        SOC2sum=SOC2sum+float(SOC2)
GPU1avg=GPU1sum/n
GPU2avg=GPU2sum/n
CPUavg=CPUsum/n
SOC0avg=SOC0sum/n
SOC1avg=SOC1sum/n
SOC2avg=SOC2sum/n
SOCavg=(SOC0avg+SOC1avg+SOC2avg)/3
print('CPU avg= ',CPUavg,' GPU1 avg= ',GPU1avg,' GPU2 avg= ',GPU2avg,' SOC avg= ',SOCavg,'C')
log.close

