# Synology SRM AdBlocker
This is a simple implementation of a Synology SRM Ad Blocker.  
__You can use it, but it’s at your own risk.__ The worst case scenario is that you will end up with an unusable Safe Search app, but this can be fixed by reinstalling it.

## Installation
- Install `Safe Access` from `Package Center`
- Activate `root` account
- Copy `main.py`, `urls.txt` and `exceptions.txt` to your router using `scp` (You can use whatever tool do you like to copy the files into the rooter)
    - `scp main.py root@<router_ip_address>:/root/adblocker/main.py`
    - `scp urls.txt root@<router_ip_address:/root/adblocker/urls.txt`
    - `scp exceptions.txt root@<router_ip_address:/root/adblocker/exceptions.txt`
- SSH into your router using `root`
   - `ssh root@<router_ip_address>`
- Go to `adblocker folder` 
    - `cd /root/adblocker`
- Execute `main.py` using python. 
    - `> python main.py`
## How to activate the ad blocker
- Open `Safe Search`
- Go to `Profile`
- Select `Web Filter` tab
- Add a new filter with category `Advertising` selected
- Select `Profile` tab
- Create a new profile of type `My Local Network (LAN) Profile`
- Edit `My Network (LAN)`
- Activate `Web Filter`
- Select `Custom` and then select your previously created web filter

#### Don't forget to disable admin account and SSH service if they were disabled (I prefer to keep them disabled for security reasons)

## How to update the ad blocking list
- Execute `main.py` using python as `root`. 
    - `> python main.py`
## FAQ
__Q: How do I activate SSH?__  
A: Go to `Control Panel -> Services -> SSH`  
__Q: How to I activate `root` account?__  
A: Go to `Control Panel -> User` and activate `admin` account  
__Q: What is the password for `root` account?__  
 A: Same password that you've set for `admin` account  
 
## List of hosts used to create the database:
- http://winhelp2002.mvps.org/hosts.txt
- https://v.firebog.net/hosts/AdguardDNS.txt
- https://adaway.org/hosts.txt
- https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt
- https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt
- https://hosts-file.net/ad_servers.txt
- https://raw.githubusercontent.com/quidsup/notrack/master/trackers.txt
- https://v.firebog.net/hosts/Easylist.txt
- https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts;showintro=0
- https://v.firebog.net/hosts/Easyprivacy.txt
- https://v.firebog.net/hosts/Prigent-Ads.txt
- https://raw.githubusercontent.com/EnergizedProtection/block/master/spark/formats/hosts
- https://mirror.cedia.org.ec/malwaredomains/immortal_domains.txt

## You can also enable multiple sources by uncommenting them from urls.txt file
- https://raw.githubusercontent.com/StevenBlack/hosts/master/data/add.2o7Net/hosts
- https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt
- https://v.firebog.net/hosts/Airelle-trc.txt
- https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/android-tracking.txt
- https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV.txt
- https://hosts-file.net/exp.txt
- https://hosts-file.net/emd.txt
- https://hosts-file.net/psh.txt
- https://v.firebog.net/hosts/Prigent-Malware.txt
- https://v.firebog.net/hosts/Prigent-Phishing.txt
- https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt
- https://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt
- https://ransomwaretracker.abuse.ch/downloads/CW_C2_DOMBL.txt
- https://ransomwaretracker.abuse.ch/downloads/LY_C2_DOMBL.txt
- https://ransomwaretracker.abuse.ch/downloads/TC_C2_DOMBL.txt
- https://ransomwaretracker.abuse.ch/downloads/TL_C2_DOMBL.txt
- https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist
- https://v.firebog.net/hosts/Shalla-mal.txt
- https://raw.githubusercontent.com/StevenBlack/hosts/master/data/add.Risk/hosts
- https://www.squidblacklist.org/downloads/dg-malicious.acl
- https://v.firebog.net/hosts/Airelle-hrsk.txt
- https://raw.githubusercontent.com/HorusTeknoloji/TR-PhishingList/master/url-lists.txt
- https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-blocklist.txt

License

This code is distributed under the terms and conditions of the MIT license.
