import time
import signal
import sys



def signal_handler(sig, frame):
    print("\nMonitoring stopped.")
    sys.exit(0)



def monitor_log(log_file):
    try:
        with open(log_file, 'r') as file:

            file.seek(0, 2)

            while True:
                new_line = file.readline()
                if new_line:
                    print(new_line.strip())
                else:
                    time.sleep(0.1)
    except FileNotFoundError:
        print("Error: Log file not found.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_monitor.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]


    signal.signal(signal.SIGINT, signal_handler)

    print(f"Monitoring log file: {log_file}")
    monitor_log(log_file)
