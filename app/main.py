def copy_file(command: str) -> None:

    parts = command.strip().split()
    if len(parts) != 3:
        return

    cmd, src, dst = parts
    if cmd != "cp" or src == dst:
        return

    try:
        with open(src, "rb") as fin, open(dst, "wb") as fout:
            while True:
                chunk = fin.read(1024 * 1024)
                if not chunk:
                    break
                fout.write(chunk)
    except FileNotFoundError:
        return
