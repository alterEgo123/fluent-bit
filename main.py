import glob
import ast
from pprint import pprint


def extract_dict(log_line):
    return ast.literal_eval(log_line.replace('\n', '').strip('][').split(', ')[1])


def collect_log():
    logs = [f for f in glob.glob("/var/logs/fluent-logs/*.log")]
    for logging in logs:
        file_name = logging.split('fluent-logs/')[-1]
        with open(logging, 'r') as file:
            lines = file.read().split(file_name + ': ')
            all_log = [extract_dict(line) for line in lines[1:]]
            yield all_log


if __name__ == '__main__':
    for log in collect_log():
        pprint(log)
