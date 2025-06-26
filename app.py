import argparse
from task import Task
from utils import load_tasks, save_tasks, get_next_id, filter_today_tasks

def main():
    parser = argparse.ArgumentParser(description="📝 CLI To-Do List Manager")
    subparsers = parser.add_subparsers(dest="command")
    ...
    if __name__ == "__main__":
        main()
