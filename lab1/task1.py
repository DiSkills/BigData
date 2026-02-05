from collections import Counter

from utils import measure_time


def extract_ip(line: str) -> str | None:
    return line.split()[0] if line.strip() else None


@measure_time
def solve(filename: str, n: int) -> list[tuple[str, int]]:
    ips = Counter()
    with open(filename) as file:
        for line in file:
            if ip := extract_ip(line):
                ips[ip] += 1
    return ips.most_common(n)


def main():
    ips, execution_time = solve("access.log", 10)
    print(ips, execution_time)


if __name__ == "__main__":
    main()
