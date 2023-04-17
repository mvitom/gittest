import serial
import serial.tools.list_ports
data_kodeslani = "dawdwad"
with serial.Serial(port="COM4",baudrate=115200,bytesize=8,timeout=1,stopbits=serial.STOPBITS_ONE) as serialPort:
    while True:
        #aby mikroprocesor precetl tak se musi encodovat do jineho formatu
        #serialPort.write(data_kodeslani.encode("utf-8"))
        #promenna data ktera ceka na ukoncovaci znak (\n)
        data = serialPort.read_until()
        print(data.decode())
# ports = serial.tools.list_ports.comports()
# #zjisteni com portu
# for port in sorted(ports):
#     print("{}".format(port))
#__________________prijimani z mikroprocesoru_____________

