import psutil
import webbrowser
import time
import datetime
import asyncio
import matplotlib.pyplot as plt
from rich.traceback import install
from rich.console import Console
from rich.progress import Progress
from rich.progress import track
from rich.text import Text
from tqdm import tqdm
from rich.table import Table
from rich.prompt import Prompt

# System metrics checking-----------------------------------------------
console = Console()
install()

async def cpu_cores():
    give_cpu_cores = psutil.cpu_count(logical=False)

    with Progress() as progress:
        task = progress.add_task("Checking CPU cores...", total=1)
        await asyncio.sleep(1)
        progress.update(task, advance=1)

    console.print(f"CPU CORES: {give_cpu_cores}")


async def cpu_freq():
    """
    This function will return your current CPU frequency, maximum CPU frequency and minimum CPU frequency in MHz.

    For example, if you have a 2.7 GHz CPU, it will return 2700.0 as the current frequency, 2700.0 as the maximum frequency and 800.0 as the minimum frequency.
    """

    check_cpu_frq = psutil.cpu_freq()

    # for _ in track(range(1), description='Checking CPU frequency...'):
    #     await asyncio.sleep(0.5)
    #     console.print(f"Current CPU frequency checked")
    #     console.print(f"Current CPU Max frequency checked")
    #     console.print(f"Current CPU Min frequency checked")

    # console.print(f"CURRENT CPU FREQUENCY✔️: { check_cpu_frq.current} MHz", style='bold italic')
    # console.print(f"CPU MAX FREQUENCY✔️: { check_cpu_frq.max} MHz", style='bold italic')
    # console.print(f"CPU MIN FREQUENCY✔️: {check_cpu_frq.min} MHz", style='bold italic')
    for _ in track(range(1), description='Checking current CPU frequency...'):
        await asyncio.sleep(0.5)
    console.print(f"CURRENT CPU FREQUENCY✔️: {check_cpu_frq.current} MHz", style='bold italic')

    for _ in track(range(1), description='Checking CPU max frequency...'):
        await asyncio.sleep(0.5)
    console.print(f"CPU MAX FREQUENCY✔️: {check_cpu_frq.max} MHz", style='bold italic')

    for _ in track(range(1), description='Checking CPU min frequency...'):
        await asyncio.sleep(0.5)
    console.print(f"CPU MIN FREQUENCY✔️: {check_cpu_frq.min} MHz", style='bold italic')



async def cpu_usage():
    check_cpu_usage = psutil.cpu_percent(percpu=True, interval=1)
    console.print(f"Checking your CPU usage...")
    
    for _ in tqdm(range(100)):
        await asyncio.sleep(0.1)
  
    for i, usage in enumerate(check_cpu_usage):
        console.print(f"Core {i}: {usage}%", style='bold italic')


async def memory_usage():
    check_mem_usage = psutil.Process()
    mem_info = check_mem_usage.memory_info()
    
    for _ in track(range(1), description='Cheking memory usage...'):
        await asyncio.sleep(1)
    console.print(f"RSS✔️: {mem_info.rss} bytes", style='bold italic')
    console.print(f"VMS✔️: {mem_info.vms} bytes", style='bold italic')

async def log_user():
    user = psutil.users()
    
    for _ in track(range(1), description='Checking details about cuurent logged user...'):
        await asyncio.sleep(1)
        
    for current_user in user:
        console.print(f"Here is your current user: {current_user.name}", style='bold italic')
        console.print(f"Terminal {current_user.terminal}", style='bold italic')
        console.print(f"Host: {current_user.host}", style='bold italic')
        console.print(f"Started: {datetime.datetime.fromtimestamp(current_user.started)}", style='bold italic')
        console.print(f"PID: {current_user.pid}", style='bold italic')
        


async def about_memory():
    check_mem_usage = psutil.virtual_memory()
    
    for _ in track(range(1), description='Checking about your v-memory'):
        await asyncio.sleep(1)

    console.print(f"Total: {check_mem_usage.total} bytes", style='bold italic')
    console.print(f"Available: {check_mem_usage.available} bytes", style='bold italic')
    console.print(f"Used: {check_mem_usage.used} bytes", style='bold italic')
    console.print(f"Free: {check_mem_usage.free} bytes", style='bold italic')

async def system_processes():
    pids = psutil.pids()
    
    console.print("Checking your system process...")
    for _ in tqdm(range(100)):
        await asyncio.sleep(0.1)
  
    console.print("Here is the deatils about your system process")    
    console.print(f"Total number of processes: {len(pids)}", style='bold italic')
    console.print("Here are the first 10 process IDs:", pids[:10], style='bold italic')
 
        

async def disk_usage():
    check_disk_usage = psutil.disk_usage('/')

    for _ in track(range(1), description='Checking your disk usage...'):
        await asyncio.sleep(1)
        
    console.print(f"Here is your total disk space: {check_disk_usage.total}", style='bold italic')
    console.print(f"Here is your used disk space: {check_disk_usage.used}", style='bold italic')
    console.print(f"Here is your free space available in your disk: {check_disk_usage.free}", style='bold italic')
    console.print(f"Here is your percentage of your disk space that is used: {check_disk_usage.percent}", style='bold italic')

async def boot_time():

    for _ in track(range(1), description='Checking your system boot time...'):
        await asyncio.sleep(1)
        
    console.print(f"Here is your system boot time: {psutil.boot_time()}", style='bold italic')

async def battery_status():
    battery = psutil.sensors_battery()

    for _ in track(range(1), description='Checking battery status...'):
        await asyncio.sleep(1)
    console.print(f"Here is your battery status: {battery.percent}%", style='bold italic')
    console.print(f"Here is your battery power plugged in: {battery.power_plugged}", style='bold italic')
    console.print(f"Here is your battery time left: {battery.secsleft}", style='bold italic')
    

async def network_usage():
    check_network = psutil.net_io_counters()
    console.print("Checking your network usage...")

    for _ in tqdm(range(100)):
        await asyncio.sleep(0.1)
    console.print("Here is the details about your networks usage")    
    console.print(f"  Bytes sent: {check_network.bytes_sent}", style='bold italic')
    console.print(f"  Bytes received: {check_network.bytes_recv}", style='bold italic')
    console.print(f"  Packets sent: {check_network.packets_sent}", style='bold italic')
    console.print(f"  Packets received: {check_network.packets_recv}", style='bold italic')
    console.print(f"  Errors in sending: {check_network.errin}", style='bold italic')
    console.print(f"  Errors in receiving: {check_network.errout}", style='bold italic')
    console.print(f"  Drops in sending: {check_network.dropin}", style='bold italic')
    console.print(f"  Drops in receiving: {check_network.dropout}", style='bold italic')
    

async def network_connection():
    connections = psutil.net_connections(kind='inet')


    console.print("Checking your network connection...")
    for _ in tqdm(range(100)):
        await asyncio.sleep(0.1)
        
    console.print("Here is the details about your network connection")
    for conn in connections:
        console.print(f"PID: {conn.pid}, Status: {conn.status}, Local Address: {conn.laddr}, Remote Address: {conn.raddr}", style='italic')
        
        
async def internet_connection():
    addresses = psutil.net_if_addrs()
    
    console.print("Checking your internet connection...")
    for _ in tqdm(range(100)):
        await asyncio.sleep(0.1)
        
    console.print("Here is the details about your internet connection")
    

    for interface, addrs in addresses.items():
        console.print(f"Interface: {interface}", style='italic')
        for addr in addrs:
            console.print(f"  Family: {addr.family}", style='italic')
            console.print(f"  Address: {addr.address}", style='italic')
            console.print(f"  Netmask: {addr.netmask}", style='italic')
            console.print(f"  Broadcast: {addr.broadcast}", style='italic')

# Time, date -----------------------------------------------------------------------


async def time():
    """
    Prints the current time in the format "YYYY-MM-DD HH:MM:SS".
    """

    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    console.print(formatted_time)


async def date():
    """
    Prints the current date in the format "YYYY-MM-DD".

    """

    console.print(datetime.datetime.now())


async def day():
    """
    Prints the current day of the month as an integer.

    """

    console.print(datetime.datetime.now().day)


async def year():
    """
    Prints the current year as an integer.

    """

    console.print(datetime.datetime.now().year)


async def month():
    """
    Prints the current month as an integer.

    """
    console.print(f"Here is your current month: {datetime.datetime.now().month}")


async def full_date():
    """
    Prints the current date and time in the format "DD/MM/YYYY, HH:MM:SS".

    """
    console.print(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))

# webbrowser --------------------------------------------------------------------------------


async def open_any():
    class InvalidUrl(Exception):
        pass
    
    while True:
        ask_user = Prompt.ask("[blue]Enter the URL here[/blue] (or type 'quit' to exit): ", console=console)

        if ask_user.lower() == 'quit':
            console.print("[bold green]Goodbye![/bold green]")
            break

        if ask_user.startswith(('https://', 'http://')):
            console.print(f"[bold blue]Opening {ask_user}...[/bold blue]")
            webbrowser.open(ask_user)
        else:
            try:
                raise InvalidUrl(f"'{ask_user}' is not a valid URL. Please include 'http://' or 'https://'.")
            except InvalidUrl as e:
                console.print(f"[bold red]Error:[/bold red] {str(e)}", style="red")
                continue  

# Matplotlib graphs ---------------------------------------------------------------------

async def make_graphs():
    """
    Create a graph based on user input.

    Asks the user for comma-separated x and y values, and then for the type of graph to
    create ("Plot-chat", "Scatter chart", or "Stem plot").

    Prints the graph to the console.

    If the user enters invalid input, prints an error message and continues to the next iteration.

    If the user enters 'quit' (case-insensitive), exits the loop and returns control to the caller.

    """
    while True:
   # Styled prompt for x values input
        x_input = Prompt.ask("[blue]Enter the x values (comma-separated)[/blue]", console=console)
        y_input = Prompt.ask("[blue]Enter the y values (comma-separated)[/blue]", console=console)


        try:
            x = list(map(float, x_input.split(',')))
            y = list(map(float, y_input.split(',')))

            if len(x) != len(y):
                console.print("The number of x and y values must be the same. Please try again.", style='red')
                continue

            choice = Prompt.ask(
                "[bold blue]Which type graph to you want to need\n \"Plot-chart\"\n \"Scatter chart\"\n \"Stem plot\[/bold blue]", console=console)
            
            if choice not in ["Plot-chart", "Scatter chart", "Stem plot"]:
                console.print("Invalid choice. Please choose:\n- Plot-chart\n- Scatter chart\n- Stem plot\n try again ;-;", style='red')
                continue
            
            for _ in track(range(1), description='Creating Plot...'):
                await asyncio.sleep(0.5)
            
            else:

                if choice == "Plot-chart":
                    plt.plot(x, y)
                    plt.title("Here is your Plot chart")
                    plt.grid(True)
                    plt.show()
                elif choice == "Scatter chart":
                    plt.scatter(x, y)
                    plt.title("Here is your Scatter chart")
                    plt.grid(True)
                    plt.show()
                elif choice == "Stem plot":
                    plt.stem(x, y)
                    plt.title("Here is your Stem plot")
                    plt.grid(True)
                    plt.show()
        

            cont = input(
                "Do you want to create another graph? (yes/no): ").strip().lower()
            if cont != 'yes':
                break

        except ValueError:
            console.print("Please enter valid numbers separated by commas.", style='red')
            continue
        except Exception as e:
            console.print(f"An unexpected error occurred: {str(e)}", style='red')


async def make_table():
    while True:
        
        user_title = Prompt.ask(
            'Enter the title here for your table: ', console=console)
        user_col1 = Prompt.ask('Enter the col 1 name', console=console)
        user_col2 = Prompt.ask('Enter the col 2 name', console=console)
        user_col3 = Prompt.ask('Enter the col 3 name', console=console)
        user_col4 = Prompt.ask('Enter the col 3 name', console=console)


        user_r1_col1 = Prompt.ask('Enter the row1/1 as per your col1', console=console)
        user_r1_2_col2 = Prompt.ask('Enter the row1/2 for your col2', console=console)
        user_r1_3_col3 = Prompt.ask('Enter the row1/3 for your col3', console=console)
        user_r1_4_col4 = Prompt.ask('Enter the row1/4 for your col4', console=console)

        user_r2_col1 = Prompt.ask('Enter the row2/1 as per your col1', console=console)
        user_r2_col2 = Prompt.ask('Enter the row2/2 for your col2', console=console)
        user_r2_col3 = Prompt.ask('Enter the row2/3 for your col3', console=console)
        user_r2_col4 = Prompt.ask('Enter the row2/4 for your col4', console=console)

        user_r3_col1 = Prompt.ask('Enter the row3/1 as per your col1', console=console)
        user_r3_2_col2 = Prompt.ask('Enter the row3/2 for your col2', console=console)
        user_r3_2_col3 = Prompt.ask('Enter the row3/3 for your col3', console=console)
        user_r3_2_col4 = Prompt.ask('Enter the row3/4 for your col4', console=console)

        user_r4_col1 = Prompt.ask('Enter the row4/1 as per your col1', console=console)
        user_r4_2_col2 = Prompt.ask('Enter the row4/2 for your col2', console=console)
        user_r4_2_col3 = Prompt.ask('Enter the row4/3 for your col3', console=console)
        user_r4_2_col4 = Prompt.ask('Enter the row4/4 for your col4', console=console)
        
        for _ in track(range(1), description='Creating table...'):
            await asyncio.sleep(0.5)


        table = Table(title=user_title, border_style='yellow')

        table.add_column(user_col1, justify='left')
        table.add_column(user_col2, justify='left')
        table.add_column(user_col3, justify='left')
        table.add_column(user_col4, justify='left')

        table.add_row(user_r1_col1, user_r1_2_col2, user_r1_3_col3, user_r1_4_col4)
        table.add_row(user_r2_col1, user_r2_col2, user_r2_col3, user_r2_col4)
        table.add_row(user_r3_col1, user_r3_2_col2, user_r3_2_col3, user_r3_2_col4)
        table.add_row(user_r4_col1, user_r4_2_col2, user_r4_2_col3, user_r4_2_col4)

        console.print(table)
        
        class UserError(Exception):
            pass

        user_ask = input("Did you want to make more tables? 'yes' or 'no': ")
        
        try:
            if user_ask.lower() == 'no':
                console.print("👋🏻")
                break
            elif user_ask.lower() == 'yes':
                console.print("Proceeding with table creation...", style='italic cyan')
            else:
                raise UserError("Invalid command. If you want to quit table creation, then enter 'no'")
        except UserError:
            console.print('Please enter \'yes\' or \'no\'', style='red')

# COMMANDS-----------------------------------------------------------------------------

async def handle_command(command):
    """
    Handle a command by executing the corresponding function.

    The function takes a command name as a string and executes the
    corresponding function. If the command is unknown, it prints an
    "Unknown command" message.

    Parameters
    ----------
    command : str
        The name of the command to execute

    Returns
    -------
    None
    """
    commands = {
        'CPU-CORES': cpu_cores,
        'CPU-USAGE': cpu_usage,
        'CPU-FREQ': cpu_freq,
        'MEMORY-USAGE': memory_usage,
        'MY-MEMORY': about_memory,
        'DISK-USAGE': disk_usage,
        'BOOT-TIME': boot_time,
        'CH-BATTERY': battery_status,
        'SYS-PROCESS': system_processes,
        'C-USER': log_user,
        'NETWORK-USAGE': network_usage,
        'NETWORK-CONNECTION': network_connection,
        'INTERNET-CONNECTION': internet_connection,
        'T?': time,
        'D?': date,
        'd?': day,
        'Y?': year,
        'M?': month,
        'C-D?M?Y': full_date,
        "OPEN-URL": open_any,
        "GRAPH": make_graphs,
        'M-TABLE': make_table


    }
    
    class UnknownCommand(Exception):
        pass

    func = commands.get(command)

    if func:
        await func()
    else:
        try:
            raise UnknownCommand("Unknown command entered ;-;")
        except UnknownCommand as e:
            console.print(e, style='red')
            
