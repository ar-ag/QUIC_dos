#Opening a new terminal for every subprocess
# import subprocess
# import time

# # Initial queue number
# queue_num = 1

# # Number of times to run the script
# num_runs = 3

# # List to keep track of subprocesses
# processes = []

# for i in range(num_runs):
#     # Define the command with the incremented queue number
#     queue_num_str = str(queue_num)
#     script_command = f"sudo /home/ar-ag/projects/.venv/bin/python3 request_forgery.py cm -l 2 -q {queue_num_str} 127.0.0.1 10.10.159.186"
    
#     # Define the terminal command to open a new terminal and run the script
#     terminal_command = ['gnome-terminal', '--', 'bash', '-c', f'{script_command}; exec bash']
#     print(terminal_command)
#     # Start the subprocess
#     process = subprocess.Popen(terminal_command)
#     processes.append(process)

#     # Increment the queue number for the next run
#     queue_num += 1

#     time.sleep(5)

# # Optionally, wait for all subprocesses to finish
# for process in processes:
#     process.wait()



#terminating all subprocesses at once and running subprocesses in the background
import subprocess
import time
import signal
import os

# List to keep track of subprocesses
processes = []

# Signal handler for terminating all subprocesses
def terminate_subprocesses(signum, frame):
    print("Terminating all subprocesses...")
    for process in processes:
        try:
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        except Exception as e:
            print(f"Error terminating process {process.pid}: {e}")
    exit(1)

# Register the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, terminate_subprocesses)

# Initial queue number
queue_num = 1

# Number of times to run the script
num_runs = int(input("Enter the number of times to run the script: "))

for i in range(num_runs):
    # Define the command with the incremented queue number
    queue_num_str = str(queue_num)
    script_command = [
        'sudo', '/home/ar-ag/projects/.venv/bin/python3', 'request_forgery.py', 
        'cm', '-l', '2', '-q', queue_num_str, '127.0.0.1', '10.10.159.186'
    ]
    
    # Start the subprocess
    process = subprocess.Popen(script_command, preexec_fn=os.setsid)
    processes.append(process)

    # Increment the queue number for the next run
    queue_num += 1

    # Wait for 5 seconds before starting the next process
    time.sleep(5)

# Optionally, wait for all subprocesses to finish
for process in processes:
    process.wait()



