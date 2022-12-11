from GameFunctions.utils import get_status


def print_status():
    status = get_status()
    for task, answer in status.items():
        print(f"{task}: {answer}")
