#!/bin/bash
sleep 10

run_count=0  # Counter for total potion uses
wait_time=2100  # 35 minutes (in seconds)

while true; do
    xdotool mousedown 3; sleep 2; xdotool mouseup 3  # Holds and releases right-click
    sleep 5  # Waits for the drinking animation

    # Increase run count
    ((run_count++))
    echo "Potion drunk! Total runs: $run_count"

    # Countdown timer
    for ((i=wait_time; i>0; i--)); do
        echo -ne "Next potion in: $i seconds\r"
        sleep 1
    done
    echo ""  # Clear the line after countdown
done
