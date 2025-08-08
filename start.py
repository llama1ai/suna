#!/usr/bin/env python3
import subprocess

processes = []

def main() -> None:
    try:
        backend = subprocess.Popen(["uv", "run", "api.py"], cwd="backend")
        processes.append(backend)
        frontend = subprocess.Popen(["npm", "run", "dev"], cwd="frontend")
        processes.append(frontend)
        print("\u2728 Suna uruchomiona. Przeglądarka: http://localhost:3000")
        for proc in processes:
            proc.wait()
    except KeyboardInterrupt:
        pass
    finally:
        for proc in processes:
            proc.terminate()

if __name__ == "__main__":
    main()
