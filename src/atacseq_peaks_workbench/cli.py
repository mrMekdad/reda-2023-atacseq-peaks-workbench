import argparse
from atacseq_peaks_workbench.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Workbench for peak-set bookkeeping, annotations, and comparative exports.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
