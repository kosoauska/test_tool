import os
import wmi


class device_info():
    def __init__(self):
        self.c = wmi.WMI()

    def list_disk(self):
        disk_list=[]
        w = wmi.WMI()
        for physical_disk in w.Win32_DiskDrive():
            for partition in physical_disk.associators ("Win32_DiskDriveToDiskPartition"):
                for disk in partition.associators ("Win32_LogicalDiskToPartition"):
                    disklist = [disk.Caption ,
                                disk.VolumeName ,
                                "" ,
                                round((int(disk.size) / 1024 / 1024 / 1024) , 1) ,
                                disk.FileSystem ,
                                physical_disk.Caption ,
                                ""]
                    disk_list.append(disklist)
        del w
        #print(disk_list)
        return disk_list