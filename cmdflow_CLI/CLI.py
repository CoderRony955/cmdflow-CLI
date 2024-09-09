import argparse
import asyncio
from rich.console import Console
from rich.traceback import install
from rich.progress import track
from cmdflow_CLI.cmdflow_allfunc import all_commands
from pyfiglet import Figlet


console = Console()
install()

f = Figlet(font='3-d', width=400)
render = f.renderText('<MD_FLOW')
console.print(render)

parser = argparse.ArgumentParser(description="CMD>_FLOW")

# Positional argument for command
parser.add_argument('command', type=str, nargs='?',
                    default=None, help="Enter the command to execute")


parser.add_argument('cpu-usage', action='store_true', help="Check CPU usage")
parser.add_argument('cpu_cores', action='store_true', help="Check CPU cores")
parser.add_argument('cpu_freq', action='store_true',
                    help="Check current CPU usage")
parser.add_argument('mem_usage', action='store_true',
                    help="Check current memory usage")
parser.add_argument('my_mem', action='store_true',
                    help="Know about your memory")
parser.add_argument('disk_usage', action='store_true',
                    help="Know about your disk usage")
parser.add_argument('boot_time', action='store_true',
                    help="Check system boot time")
parser.add_argument('ch_battery', action='store_true',
                    help="Check your battery status")
parser.add_argument('sys_process', action='store_true',
                    help="Check your system process")
parser.add_argument('c_user', action='store_true',
                    help="Check about current user who loged in system")
parser.add_argument('net_usage', action='store_true',
                    help="Check your network usage")
parser.add_argument('net_connection', action='store_true',
                    help="Know about your network connection")
parser.add_argument('internet_con', action='store_true',
                    help="Know about your internet connection")
parser.add_argument('t?', action='store_true', help="Check your current time")
parser.add_argument('d?', action='store_true', help="Check your current date")
parser.add_argument('day?', action='store_true', help="Check your current day")
parser.add_argument('y?', action='store_true', help="Check your current yeay")
parser.add_argument('m?', action='store_true', help="Check your current month")
parser.add_argument('c-d?m?Y', action='store_true',
                    help="Check your current dd/mm/yyyy")
parser.add_argument('open_url', action='store_true',
                    help="Open any web-based document and web-application using there vaild URL")
parser.add_argument('graph', action='store_true',
                    help="Make scatter chart, plot chart and stem chart just entering x and y comma separated values")
parser.add_argument('m_table', action='store_true',
                    help="Make table in your terminal just entering the table title and their column names and row names")
parser.add_argument('cmds', action='store_true',
                    help="get all cmds in table format")
parser.add_argument('c_ascii_text', action='store_true',
                    help="create a ASCII Text")


args = parser.parse_args()


# async def main():
#     await all_commands(args.command)
    # try:
    #     # Determine which command to run
    #     if args.cpu_cores:
    #         console.print("Running cpu_cores")
    #         await all_commands('cpu_cores')
    #     elif args.cpu_usage:
    #         console.print("Running cpu_usage")
    #         await all_commands('cpu_usage')
    #     elif args.cpu_freq:
    #         console.print("Running cpu_freq")
    #         await all_commands('cpu_freq')
    #     else:
    #         if args.command:
    #             console.print(f"Running command: {args.command}")
    #             await all_commands(args.command)
    #         else:
    #             console.print("No valid command provided", style='yellow')

    # except Exception as e:
    #     console.print(f"Error: {e}", style='red')

async def main():
    await all_commands(args.command)

def main_entry_point():
    asyncio.run(main())

if __name__ == "__main__":
    main_entry_point()
