import psutil
import time

def main():
    # vm = psutil.virtual_memory()
    # return vm.percent
    print(psutil.cpu_percent())
    return psutil.cpu_percent(interval=1)

if __name__ == "__main__":
    print("press ctrl-c to stop")
    loop_forever = True
    while loop_forever:
        health_percent = main()
        try:
            # print(f'{health_percent:.2f}' + "%")            
            # if health_percent >=  80 :
            #     print("Alert! CPU usage exceeds threshold:",health_percent)
            # else:
            #     print("Monitoring CPU usage...")

            time.sleep(1)
        except KeyboardInterrupt:
            loop_forever = False