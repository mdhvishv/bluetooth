# teacher_server.py
import bluetooth

def activate_bluetooth_server():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(("", bluetooth.PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]
    print(f"Listening on port {port}")

    # Use a valid UUID for the service
    service_uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
    bluetooth.advertise_service(
        server_sock,
        "BluetoothActivationServer",
        service_id=service_uuid,
        service_classes=[service_uuid, bluetooth.SERIAL_PORT_CLASS],
        profiles=[bluetooth.SERIAL_PORT_PROFILE],
    )

    client_sock, client_info = server_sock.accept()
    print(f"Accepted connection from {client_info}")

    # Logic to activate Bluetooth (replace with your logic)
    print("Bluetooth Activated")

    client_sock.close()
    server_sock.close()

if __name__ == "__main__":
    activate_bluetooth_server()
