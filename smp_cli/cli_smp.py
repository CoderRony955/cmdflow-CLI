import sys
import asyncio
from all_func import handle_command
from rich.console import Console
from rich.table import Table

console = Console()


def all_commands():
    system_metrics_check = {
        "know about your cpu cores": "CPU-CORES",
        "know about your cpu usage": "CPU-USAGE",
        "know about your cpu frequency": "CPU-FREQ",
        "know about your memory usage": "MEMORY-USAGE",
        "know about your memory": "MY-MEMORY",
        "know about your disk usage": "DISK-USAGE",
        "check system boot time": "BOOT-TIME",
        "check about current user who loged in system": "C-USER",
        "check your battery status": "CH-BATTERY",
        "chek your system process": "SYS-PROCESS",
        "know about your network usage": "NETWORK-USAGE",
        "know about your network connection": "NETWORK-CONNECTION",
        "know about your internet connection": "INTERNET-CONNECTION",
    }

    time_cmds = {
        "know about current time": "T?",
        "know about current date": "D?",
        "know about current day": "D?",
        "know about current month": "M?",
        "know about current year": "Y?",
        "get you current DD/MM/YYYY ": "C-D?M?Y"

    }

    web_browser_cmd = {
        "Open any web-based document and web-application using there URL": "OPEN-URL"
    }

    graph_cmd = {
        "Make scatter chart, plot chart and ste, chart": "GRAPH"
    }
    table_creation_cmd = {
        "Make table just entering the table title and columns and rows": "M-TABLE"
    }

    table = Table(title='All commands', border_style='blue')

    print("System Metrics Commands:")
    for description, command in system_metrics_check.items():
        table.add_row(description, command)

    print("\nTime Commands:")
    for description, command in time_cmds.items():
        table.add_row(description, command)

    print("\nWeb browser command:")
    for description, command in web_browser_cmd.items():
        table.add_row(description, command)

    print("\nGraph command:")
    for description, command in graph_cmd.items():
        table.add_row(description, command)
        
    print("\nTable creation command:")
    for description, command in table_creation_cmd.items():
        table.add_row(description, command)

    console.print(table)


async def user_input_loop():
    """
    An infinite loop that waits for user input to execute a command.

    The user can enter any of the available commands to execute them.
    The loop will exit when the user presses Ctrl+C or type 'exit'.
    """
    print("For commands type help :)")
    while True:
        try:
            user_command = input('Enter the command here: ')
            if user_command == 'exit':
                sys.exit()
            elif user_command == 'help':
                all_commands()
            else:
                print()
                await handle_command(user_command)
                print()
        except KeyboardInterrupt:
            print("\nExiting...")
            break


def main():
    if __name__ == "__main__":
        asyncio.run(user_input_loop())


if __name__ == "__main__":
    main()
