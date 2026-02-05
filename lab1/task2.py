from collections import Counter, defaultdict
from typing import Generator

from utils import measure_time


def extract_ip(line: str) -> str | None:
    return line.split()[0] if line.strip() else None


def chunks(filename: str, size: int) -> Generator[list[str]]:
    chunk = []
    with open(filename) as file:
        for line in file:
            chunk.append(line)
            if len(chunk) >= size:
                yield chunk
                chunk = []
    if chunk:
        yield chunk


def mapper(chunk: list[str]) -> Counter[str]:
    ips = Counter()
    for line in chunk:
        if ip := extract_ip(line):
            ips[ip] += 1
    return ips


def shuffler(mappers: list[Counter[str]]) -> dict[str, list[int]]:
    result = defaultdict(list)
    for mapper in mappers:
        for ip, count in mapper.items():
            result[ip].append(count)
    return result


def reducer(shuffler: dict[str, list[int]]) -> Counter[str]:
    result = Counter()
    for ip, counts in shuffler.items():
        result[ip] = sum(counts)
    return result


@measure_time
def solve(filename: str, n: int, size: int) -> list[tuple[str, int]]:
    mapped = []
    for chunk in chunks(filename, size):
        mapped.append(mapper(chunk))
    shuffled = shuffler(mapped)
    reduced = reducer(shuffled)
    return reduced.most_common(n)


def main():
    ips, execution_time = solve("access.log", 10, 10_000)
    print(ips, execution_time)


if __name__ == "__main__":
    main()
