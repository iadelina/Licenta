
def disable_rfid_forever():
    import os
    pid = os.system('ps aux | grep rfid_forever.py | awk \'{print $2}\' | head -1')
    os.system('kill -9 {}'.format(pid))

def write_in_file(key):
    import sys
    import os
    file_buffer = open('/home/pi/Desktop/Licenta_latest/Licenta_senzori/keys.txt', 'r+')
    file_buffer.write(str(id)+ '\n')
    file_buffer.close()
