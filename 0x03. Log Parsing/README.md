
# Log Generation and Metrics Calculation

This project demonstrates log generation and metrics calculation in Python. The script generates simulated log data and computes metrics such as total file size and counts of specific status codes.

## Getting Started

To run the script and generate log data, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/log-metrics.git
   ```

2. Navigate to the project directory:

   ```bash
   cd log-metrics
   ```

3. Run the script:

   ```bash
   python generate_logs.py > data.log
   ```

## Script Description

The `generate_logs.py` script generates simulated log data in the specified format and outputs it to stdout. The log format includes IP addresses, timestamps, request methods, status codes, and file sizes.

## Metrics Calculation

The script calculates the following metrics:

- Total file size: The sum of all file sizes in the generated logs.
- Number of lines by status code: Counts of specific status codes (e.g., 200, 301, 404) in the log data.

## Saving Logs

The generated log data is saved to a file named `data.log` using redirection (`>`).

## Requirements

- Python 3.x
- Standard Python libraries

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


You can customize this README template by replacing placeholders like `your_username`, adding more detailed instructions, or including additional sections relevant to your project.
