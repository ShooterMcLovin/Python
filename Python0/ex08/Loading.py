import time


def ft_tqdm(lst: range) -> None:
    tot = len(lst)
    start_time = time.time()

    for i, elem in enumerate(lst):
        progress = (i + 1) / tot
        bar_length = 100
        num_hashes = int(progress * bar_length)
        bar = "=" * num_hashes + ">" + "." * (bar_length - num_hashes - 1)
        pct = int(progress * 100)
        eTime = time.time() - start_time
        speed = (i + 1) / eTime if eTime > 0 else 0
        remaining_time = (tot - (i + 1)) / speed if speed > 0 else 0

        print(f"\r{pct}%|{bar}| {i + 1}/{tot} [{eTime:.2f}s, {speed:.2f}it/s] "
              f"({remaining_time:.2f}s remaining)", end="")

        yield elem

    print()
