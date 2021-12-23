#!/usr/bin/python3
import libtorrent
from os import getcwd
from time import time,sleep
from datetime import datetime

link = "magnet:?xt=urn:btih:B6E24F701BF82EA3E8014428B09912556C40D93D&dn=WinToHDD+v5.4.1+Technician+Portable+Cracked+%7BCracksHash%7D&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.pirateparty.gr%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fipv4.tracker.harry.lu%3A80%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.open-internet.nl%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce"
session = libtorrent.session()
session.listen_on(6881,6891)
# params = {
#     "save_path":str(getcwd()),
#     "storage_mode":libtorrent.storage_mode_t(2),
#     "paused":False,
#     "auto_managed":True,
#     "duplicate_is_error":True
# }
params = {
    "save_path":str(getcwd()),
    "storage_mode":libtorrent.storage_mode_t(2),
}
handel = libtorrent.add_magnet_uri(session,link,params)
session.start_dht()
begin = time()
print(datetime.now())
print("[+] Downloading Metadata......")
while (not handel.has_metadata()):
    sleep(1)

print("[+] Got Metadata, Starting Downloading File......")
print("Starting ",handel.name())
while (handel.status().state != libtorrent.torrent_status.seeding):
    s = handel.status()
    status_str = ["queued","checking","downloading metadata","downloading","finished","seeding","allocating"]
    print("% .2f %% Complete (down: %.1f kb/s up: %.1f kb/s, peers:%d) %s" % (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,s.num_peers,status_str[s.state]))
    sleep(3)

end = time()
print(handel.name(),"Completed")
print("Time Elapsed: ",int((end-begin) // 60))