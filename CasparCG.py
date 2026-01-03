import socket
import time

Storage1 = ''
Storage2 = ''


def VmixAction(IPSerwer, item1, item2):
    vmix_ip = IPSerwer
    vmix_port = 8099

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    global Storage1
    global Storage2

    try:
        sock.connect((vmix_ip, vmix_port))
        data = "XML\r\n"
        sock.sendall(data.encode())
        time.sleep(0.1)
        response = sock.recv(400)
        XmlResponse = response.decode()

        if "Paused" in XmlResponse:
            Storage1 = item1
            Storage2 = item2

            data = "FUNCTION settext Input=1&SelectedName=Headline.Text&Value={}\r\n".format(item1)
            sock.sendall(data.encode())
            data = "FUNCTION settext Input=1&SelectedName=Description.Text&Value={}\r\n".format(item2)
            sock.sendall(data.encode())
            data = "FUNCTION OverlayInput1 Input=1\r\n"
            sock.sendall(data.encode())

            data = "XML\r\n"
            sock.sendall(data.encode())
            time.sleep(0.2)

            response = sock.recv(1024)
            XmlResponse = response.decode()

        if "Running" in XmlResponse:

            data = "FUNCTION settext Input=1&SelectedName=Headline.Text&Value={}\r\n".format(Storage1)
            sock.sendall(data.encode())
            data = "FUNCTION settext Input=1&SelectedName=Description.Text&Value={}\r\n".format(Storage2)
            sock.sendall(data.encode())
            data = "FUNCTION OverlayInput1 Input=1\r\n"
            sock.sendall(data.encode())

            data = "XML\r\n"
            sock.sendall(data.encode())
            time.sleep(0.2)

            response = sock.recv(1024)
            XmlResponse = response.decode()


    except ConnectionRefusedError:
        print("Nie można połączyć się z serwerem vMix.")

    finally:
        sock.close()


def UpdateLabelText(IPSerwer, item1, item2):
    vmix_ip = IPSerwer
    vmix_port = 8099

    global Storage1
    global Storage2

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((vmix_ip, vmix_port))

        data = "XML\r\n"
        sock.sendall(data.encode())
        response = sock.recv(400)
        XmlResponse = response.decode()

        Storage1 = item1
        Storage2 = item2

        data = "FUNCTION settext Input=1&SelectedName=Headline.Text&Value={}\r\n".format(item1)
        sock.sendall(data.encode())
        data = "FUNCTION settext Input=1&SelectedName=Description.Text&Value={}\r\n".format(item2)
        sock.sendall(data.encode())

        data = "XML\r\n"
        sock.sendall(data.encode())

        response = sock.recv(1024)
        XmlResponse = response.decode()

    except ConnectionRefusedError:
        print("Nie można połączyć się z serwerem vMix.")

    finally:
        sock.close()
