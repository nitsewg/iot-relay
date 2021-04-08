Simple python script to interface a Raspberry Pi with an IoT relay power strip.

This monitors a network device, and when it detects the remote device is offline, it kills power to the IoT relay outlets.

Simple setup:

Connect ground from the relay to ground on the Raspi.  Connect positive from the relay to GPIO18 on the Raspi.

Set the IP address you want to monitor in the code.

Optional: Create crontab entry to start script on boot.
