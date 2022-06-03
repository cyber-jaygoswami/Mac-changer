import subprocess
import optparse

def get_arguments():
    #create obj of OptionParser class
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



val = get_arguments()

change_mac(val.interface, val.new_mac)



