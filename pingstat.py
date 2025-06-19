import subprocess
import time
import statistics
from datetime import datetime

def ping_once(host):
    try:
        output = subprocess.check_output(
            ["ping", "-c", "1", host],
            stderr=subprocess.DEVNULL,
            universal_newlines=True
        )
        for line in output.split("\n"):
            if "time=" in line:
                time_ms = float(line.split("time=")[1].split(" ")[0])
                return time_ms
    except subprocess.CalledProcessError:
        return None

def quantile(data, q):
    if not data:
        return None
    data_sorted = sorted(data)
    index = q * (len(data_sorted) - 1)
    lower = int(index)
    upper = min(lower + 1, len(data_sorted) - 1)
    weight = index - lower
    return data_sorted[lower] * (1 - weight) + data_sorted[upper] * weight

def count_outliers(data, q1, q3):
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return sum(1 for x in data if x < lower_bound or x > upper_bound)

def iso_timestamp():
    return datetime.now().isoformat(sep='T', timespec='seconds')

def main():
    host = "8.8.8.8"
    ping_times = []
    counter = 1

    print(f"Pinging {host} once per second. Press Ctrl+C to stop.\n")
    print(f"{'No.':>4}  {'Timestamp':>19}  {'Ping':>8}  {'Mean':>8}  {'StdDev':>8}  {'Median':>8}  {'IQR':>8}  {'Outl%':>8}")
    print("-" * 86)

    try:
        while True:
            now = iso_timestamp()
            ping_time = ping_once(host)

            if ping_time is not None:
                ping_times.append(ping_time)
                avg = statistics.mean(ping_times)
                stddev = statistics.stdev(ping_times) if len(ping_times) > 1 else 0.0
                q1 = quantile(ping_times, 0.25)
                q2 = quantile(ping_times, 0.50)
                q3 = quantile(ping_times, 0.75)
                iqr = q3 - q1
                n_out = count_outliers(ping_times, q1, q3)
                outlier_pct = (n_out / len(ping_times)) * 100

                print(f"{counter:4}  {now:>19}  {ping_time:8.2f}  {avg:8.2f}  {stddev:8.2f}  {q2:8.2f}  {iqr:8.2f}  {outlier_pct:8.3f}")
            else:
                print(f"{counter:4}  {now:>19}  {'Timeout':>8}  {'-':>8}  {'-':>8}  {'-':>8}  {'-':>8}  {'-':>8}")

            counter += 1
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    main()
