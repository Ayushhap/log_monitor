import time
import signal
import sys
import re
from collections import Counter


def signal_handler(sig, frame):
    print("\nMonitoring stopped.")
    if log_analysis:
        generate_summary_report()
    sys.exit(0)



def monitor_log(log_file):
    try:
        with open(log_file, 'r') as file:

            file.seek(0, 2)


            while True:
                new_line = file.readline()
                if new_line:
                    print(new_line.strip())
                    analyze_log_entry(new_line)
                else:
                    time.sleep(0.1)
    except FileNotFoundError:
        print("Error: Log file not found.")
    except Exception as e:
        print("An error occurred:", e)



def analyze_log_entry(log_entry):
    global log_analysis
    if "error" in log_entry.lower():
        log_analysis.append(log_entry.strip())



def generate_summary_report():
    error_count = len(log_analysis)
    print(f"\nSummary Report:")
    print(f"Total Error Count: {error_count}")
    if error_count > 0:
        print("\nTop Error Messages:")
        error_messages = Counter(log_analysis)
        for error_message, count in error_messages.most_common():
            print(f"{count} occurrences - {error_message}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_monitor.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]


    signal.signal(signal.SIGINT, signal_handler)

    log_analysis = []

    print(f"Monitoring log file: {log_file}")
    monitor_log(log_file)
