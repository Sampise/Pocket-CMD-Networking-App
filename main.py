import subprocess
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def get_ip():
    clear_screen()
    ipconfig_process = subprocess.Popen(['ipconfig'], stdout=subprocess.PIPE, text=True)
    ipconfig_output, _ = ipconfig_process.communicate()
    for line in ipconfig_output.splitlines():
        if 'IPv4 Address' in line:
            print(line)

def trace(site):
    clear_screen()
    print(f'Tracing route to "{site}", please wait...')
    trace_process = subprocess.Popen(['tracert', site], stdout=subprocess.PIPE, text=True)
    trace_output, _ = trace_process.communicate()
    if 'Unable to resolve target' in trace_output:
        print(f'Unable to trace "{site}", please make sure you have entered the target correctly!')
    else:
        clear_screen()
        print(f'Trace complete:\n{trace_output}')

def ping(target):
    clear_screen()
    print(f'Pinging "{target}", please wait...')
    ping_process = subprocess.Popen(['ping', target], stdout=subprocess.PIPE, text=True)
    ping_output, _ = ping_process.communicate()
    if 'Ping request could not find host' in ping_output:
        print(f'Unable to ping "{target}", please make sure you have entered the target correctly!')
    else:
        clear_screen()
        print(f'Pinging complete:\n{ping_output}')

def main_menu():
    while True:
        print('''    ----------------
    1. Get your IP
    2. Trace route
    3. Ping
    ----------------
    0. Exit
    ''')
        choice = input('Choose a command: ')
        try:
            choice = int(choice)
            if choice == 1:
                get_ip()
            elif choice == 2:
                site_input = input('Please enter tracing target: ')
                trace(site_input)
            elif choice == 3:
                ping_target = input('Please enter ping target: ')
                ping(ping_target)
            elif choice == 0:
                clear_screen()
                break
            else:
                clear_screen()
                print(f'"{choice}" was not found, please try again.')
        except ValueError:
            clear_screen()
            print(f'"{choice}" is invalid input. Please enter a valid number.')

if __name__ == "__main__":
    clear_screen()
    main_menu()
