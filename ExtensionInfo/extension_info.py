#!/usr/bin/python3
# Copyright© 2023 LinuxUsersLinuxMint
# PyTerm Support Extension Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
# PyTerm Support Extension All Rights Reserved under the GPL(General Public License).
# Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
# A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint

from ext_info import *
import time

def Ext_info():
    print("[PyTerm_Ext]: Installation information is being prepared to be listed...")
    time.sleep(2)
    print("Name: {0}". format(name))
    print("\nVersion: {0}". format(ver))
    print("\nVersion_Type: {0}". format(ver_type))
    print("\nAbout: {0}". format(about))
    print("\nAuthor: {0}". format(author))
    print("\nAuthor Web Site: {0}". format(authorwebsite))
    time.sleep(2)
    print("[PyTerm_Ext]: Installation information is listed...")