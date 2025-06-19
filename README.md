# pingstat: Ping Statistics Script 

This Python script pings a specified IP address (default: `8.8.8.8`) once per second and provides detailed latency statistics in real-time, including mean, standard deviation, median, interquartile range (IQR), and outlier percentage.

## Features

- Sends a single ping every second.
- Displays the current ping time along with running statistics:
  - **Mean (average) ping time**
  - **Standard deviation**
  - **Median ping time**
  - **Interquartile range (IQR)**
  - **Percentage of outlier pings** (based on Tukey's fences)
- Timestamp in ISO 8601 format (`YYYY-MM-DDThh:mm:ss`).
- Incrementing counter for each ping.
- Handles ping timeouts gracefully.

## Requirements

- Python 3.6 or higher.
- Works on Unix-like systems (Linux, macOS). Uses `ping` command with `-c 1`.
- No additional Python packages needed.

## Usage

1. Clone or download this repository.
2. Run the script using Python:

```bash
python ping_statistics.py
```

3. To stop the script, press `Ctrl+C`.

## Example Output

```
Pinging 8.8.8.8 once per second. Press Ctrl+C to stop.

 No.          Timestamp      Ping     Mean   StdDev   Median      IQR   Outl%
------------------------------------------------------------------------------------
   1  2025-06-19T15:41:12    23.50    23.50     0.00    23.50     0.00    0.000
   2  2025-06-19T15:41:13    24.10    23.80     0.42    23.80     0.60    0.000
```

## Customization

* Change the target IP address by modifying the `host` variable in the script.
* Adjust ping interval by changing the `time.sleep(1)` duration.

## License

This project is provided under the MIT License. See the [LICENSE.txt](LICENSE.txt) file for details.
Feel free to open issues or pull requests for improvements!

## Acknowledgments

Script and documentation assisted by [ChatGPT](https://openai.com/chatgpt).
