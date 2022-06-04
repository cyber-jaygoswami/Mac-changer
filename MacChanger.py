# final version
import subprocess
import optparse
import re
def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i","--interface", dest="interface",help="Interface to change its MAC address")
    parser.add_option("-m","--mac", dest="new_mac",help="New MAC address")

    (val,arguments)  = parser.parse_args()
    if not val.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not val.new_mac:
        parser.error("[-] Please specify an mac, use --help for more info")

    return val


def change_mac(interface , new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")

    subprocess.call(["ifconfig", interface , "down"])
    subprocess.call(["ifconfig", interface , "hw","ether", new_mac])
    subprocess.call(["ifconfig", interface , "up"])


def get_current_mac(interface):
    ifconfig_result = str(subprocess.check_output(["ifconfig",interface]))

    regex_result= re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
    # print(regex_result.group(0))  

    if regex_result:
        return regex_result.group(0)
    else:
        print("[-] This interface doesn't have MAC address :(")
        return None

val = get_arguments()
current_mac = get_current_mac(val.interface)
print(f"Current MAC addresss is : {current_mac} ")

change_mac(val.interface, val.new_mac)

current_mac = get_current_mac(val.interface)

if current_mac == val.new_mac:
    print("[+] MAC address changed :)")
    print(f"Current MAC addresss is : {current_mac} ")
else:
    print("[-] MAC address didn't get changed :(")
    print(f"Current MAC addresss is : {current_mac} ")





